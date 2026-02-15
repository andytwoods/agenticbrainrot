from django.core.management.base import BaseCommand

from agenticbrainrot.helpers.export_helpers import run_export


class Command(BaseCommand):
    help = "Export anonymised dataset (CSV + Parquet) with codebook and manifest."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-dir",
            type=str,
            default=None,
            help="Override the output directory (default: exports/vYYYY-MM-DD/)",
        )

    def handle(self, *args, **options):
        output_dir, manifest = run_export(output_dir=options["output_dir"])

        self.stdout.write(self.style.SUCCESS(f"Export complete: {output_dir}"))
        self.stdout.write(f"Version: {manifest['version']}")
        for table, count in manifest["row_counts"].items():
            self.stdout.write(f"  {table}: {count} rows")
