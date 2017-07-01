#!/usr/bin/env bash

rm -rf app/app/db.sqlite3

pip install -U pip \
    && pip install -Ur requirements.txt

cd app/

python manage.py migrate \
    && python manage.py createadminuser

python manage.py runserver 0.0.0.0:8000