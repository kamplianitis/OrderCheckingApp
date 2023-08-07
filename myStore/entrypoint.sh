#!/bin/bash

  python manage.py makemigrations
  python manage.py migrate
  # run django rest api
  python manage.py runserver 0.0.0.0:$DJANGO_PORT
