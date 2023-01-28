#!/bin/bash

export PYTHONUNBUFFERED=1
apk add --no-cache python3 postgresql-libs
apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
pip install -r requirements.txt
apk --purge del .build-deps

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000