#!/bin/bash

# Wait for postgres
while ! nc -z db 5432; do
    echo "Waiting for postgres..."
    sleep 1
done

echo "PostgreSQL started"

# Apply database migrations
python manage.py migrate --noinput

# Start server
exec "$@"