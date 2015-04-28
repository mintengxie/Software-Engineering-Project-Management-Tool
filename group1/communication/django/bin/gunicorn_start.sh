#!/bin/bash
source /home/cs673/.virtualenvs/cs673/bin/activate
cd /home/cs673/Comm-Tool/django/
gunicorn group2.wsgi:application --bind 0.0.0.0:8000 --workers=3 --reload
