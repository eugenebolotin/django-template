#!/bin/sh

# Change to project root
cd "$(dirname "$0")/.."

echo "Waiting for db"
uv run scripts/wait_for_db.py

echo "Collecting static"
uv run manage.py collectstatic --noinput

echo "Migrating DB"
uv run manage.py migrate

echo "Creating superuser"
uv run scripts/create_superuser.py

echo "Starting app"
uv run uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --workers 4 --log-level info --access-log --log-config=scripts/uvicorn_log_config.yaml --proxy-headers