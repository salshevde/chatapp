#!/bin/bash
# Apply database migrations
python manage.py migrate --noinput

# Start server
exec "$@"