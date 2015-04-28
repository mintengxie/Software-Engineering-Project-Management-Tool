#!/bin/bash
source /home/pgmvt/sites/pre.3blueprints.com/virtualenv/bin/activate
cd /home/pgmvt/sites/pre.3blueprints.com/source/Final_Project/group1
gunicorn group1.wsgi:application --bind 0.0.0.0:8000 --workers=3 --reload
