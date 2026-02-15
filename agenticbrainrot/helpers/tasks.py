from huey import crontab
from huey.contrib.djhuey import periodic_task

from .task_helpers import abandon_stale_sessions
from .task_helpers import cleanup_pii_retention
from .task_helpers import send_reminder_emails


@periodic_task(crontab(minute="0", hour="*"))
def abandon_stale_sessions_task():
    """Hourly: mark in-progress sessions older than timeout as abandoned."""
    return abandon_stale_sessions()


@periodic_task(crontab(minute="0", hour="8"))
def send_reminder_emails_task():
    """Daily at 08:00: send reminder emails to eligible participants."""
    return send_reminder_emails()


@periodic_task(crontab(day_of_week="0", hour="3", minute="0"))
def cleanup_pii_retention_task():
    """Weekly on Sunday at 03:00: purge PII older than 24 months."""
    return cleanup_pii_retention()
