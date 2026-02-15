# Database Backup & Restore

## Automated Daily Backups

Production PostgreSQL backups should run daily via Appliku's managed backup feature or a cron job:

```bash
# Example cron entry (runs at 02:00 UTC daily)
0 2 * * * pg_dump "$DATABASE_URL" | gzip > /backups/agenticbrainrot-$(date +\%Y\%m\%d).sql.gz
```

Retain at least 30 days of daily backups. Store backups in S3-compatible object storage with server-side encryption enabled.

## Manual Backup

```bash
pg_dump "$DATABASE_URL" --format=custom --file=backup.dump
```

## Restore

```bash
# 1. Stop the application
# 2. Create a fresh database (or drop/recreate)
dropdb agenticbrainrot && createdb agenticbrainrot

# 3. Restore from dump
pg_restore --dbname=agenticbrainrot --no-owner --no-acl backup.dump

# 4. Run migrations (in case the backup predates a migration)
python manage.py migrate

# 5. Restart the application
```

## Quarterly Restore Test

Schedule a quarterly restore test to verify backup integrity:

1. Download the latest backup to a staging environment.
2. Restore into a fresh PostgreSQL instance.
3. Run `python manage.py check` and `python manage.py migrate --check`.
4. Verify key data (participant count, session count) matches production.
5. Document the test date and result.
