"""Send the end-of-study debrief email to eligible participants."""

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from agenticbrainrot.accounts.models import Participant
from agenticbrainrot.consent.models import ConsentRecord
from agenticbrainrot.consent.models import DebriefRecord


class Command(BaseCommand):
    help = (
        "Send the end-of-study debrief email to participants who have given consent "
        "and have not yet received a debrief. Records each send in DebriefRecord."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print who would be emailed without sending anything or writing to the DB.",
        )
        parser.add_argument(
            "--resend",
            action="store_true",
            help="Send to participants who have already received a debrief.",
        )
        parser.add_argument(
            "--participant-id",
            type=int,
            dest="participant_id",
            help="Limit to a single participant ID (useful for testing).",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        resend = options["resend"]
        participant_id = options.get("participant_id")

        # Participants who have ever given consent
        consented_ids = (
            ConsentRecord.objects.filter(consented=True)
            .values_list("participant_id", flat=True)
            .distinct()
        )
        qs = Participant.objects.filter(pk__in=consented_ids).select_related("user")

        if participant_id:
            qs = qs.filter(pk=participant_id)

        if not resend:
            already_debriefed_ids = DebriefRecord.objects.values_list("participant_id", flat=True).distinct()
            qs = qs.exclude(pk__in=already_debriefed_ids)

        total = qs.count()
        if total == 0:
            self.stdout.write("No eligible participants found.")
            return

        action = "Would send" if dry_run else "Sending"
        self.stdout.write(f"{action} debrief to {total} participant(s).")

        site_url = getattr(settings, "SITE_URL", "https://canistillcode.org")
        contact_email = getattr(settings, "CONTACT_EMAIL", settings.ADMINS[0][1])
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", contact_email)

        subject = render_to_string("consent/emails/debrief_subject.txt").strip()

        sent = 0
        failed = 0

        for participant in qs:
            email_address = participant.user.email
            participant_name = participant.user.name or email_address

            context = {
                "participant": participant,
                "participant_name": participant_name,
                "contact_email": contact_email,
                "site_url": site_url,
            }
            html_body = render_to_string("consent/emails/debrief_body.html", context)

            if dry_run:
                self.stdout.write(f"  [dry-run] {email_address}")
                continue

            try:
                msg = EmailMultiAlternatives(
                    subject=subject,
                    body=html_body,
                    from_email=from_email,
                    to=[email_address],
                )
                msg.attach_alternative(html_body, "text/html")
                msg.send()
                DebriefRecord.objects.create(participant=participant)
                sent += 1
                self.stdout.write(f"  Sent → {email_address}")
            except Exception as exc:  # noqa: BLE001
                failed += 1
                self.stderr.write(f"  FAILED → {email_address}: {exc}")

        if not dry_run:
            self.stdout.write(self.style.SUCCESS(f"Done. Sent: {sent}  Failed: {failed}"))
