#!/bin/bash

# Django командасын иштетүү
./manage.py collectstatic --noinput
./manage.py makemigrations
./manage.py migrate
gunicorn -b 0.0.0.0:8000 core.wsgi:application