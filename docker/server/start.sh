#!/usr/bin/env bash
# start.sh

MIGRATE="${APPLY_MIGRATION:-false}"

if [ "$MIGRATE" = "true" ]; then
    echo "Applying migration"
    (cd photogram; python manage.py wait_for_db)
    (cd photogram; python manage.py migrate --no-input)
fi

(cd photogram; gunicorn photogram.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3)