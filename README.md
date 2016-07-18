# blog
A blog written in Django and hosted on aws

# TODO
Setup a user without sudo for hosting webapps

# AWS Virtual Environment Setup

## Install Virtual Environment Wrapper
sudo pip-3.4 install virtualenvwrapper

###### Add the following to .bashrc
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh


###### Reset Environment
. ~/.bashrc

## Environment Setup
mkvirtualenv blog
workon blog
vi ~/.virtualenvs/blog/bin/postactivate
```
#!/bin/bash
# This hook is sourced after this virtualenv is activated.
# PostgreSQL
export POSTGRES_PASSWORD=#########
export POSTGRES_USER=blog
export DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@127.0.0.1:5432/blog

# General settings
export DJANGO_ADMIN_URL=
export DJANGO_SETTINGS_MODULE=config.settings.local
export DJANGO_SECRET_KEY=#########################
export DJANGO_ALLOWED_HOSTS=######################

# AWS Settings
export DJANGO_AWS_ACCESS_KEY_ID=
export DJANGO_AWS_SECRET_ACCESS_KEY=
export DJANGO_AWS_STORAGE_BUCKET_NAME=

# Used with email
export DJANGO_MAILGUN_API_KEY=
export DJANGO_SERVER_EMAIL=

# Security! Better to use DNS for this task, but you can use redirect
export DJANGO_SECURE_SSL_REDIRECT=False

# django-allauth
export DJANGO_ACCOUNT_ALLOW_REGISTRATION=True
# Sentry
export DJANGO_SENTRY_DSN=
```
vi ~/.virtualenvs/blog/bin/postdeactivate
```
#!/bin/bash
# This hook is sourced after this virtualenv is deactivated.

unset POSTGRES_PASSWORD
unset POSTGRES_USER
unset DATABASE_URL

# General settings
unset DJANGO_ADMIN_URL
unset DJANGO_SETTINGS_MODULE
unset DJANGO_SECRET_KEY
unset DJANGO_ALLOWED_HOSTS

# AWS Settings
unset DJANGO_AWS_ACCESS_KEY_ID
unset DJANGO_AWS_SECRET_ACCESS_KEY
unset DJANGO_AWS_STORAGE_BUCKET_NAME

# Used with email
unset DJANGO_MAILGUN_API_KEY
unset DJANGO_SERVER_EMAIL

# Security! Better to use DNS for this task, but you can use redirect
unset DJANGO_SECURE_SSL_REDIRECT

# django-allauth
unset DJANGO_ACCOUNT_ALLOW_REGISTRATION
# Sentry
unset DJANGO_SENTRY_DSN
```

## Install Requirements
deactivate
workon blog
###### Pillow Requirements
sudo yum install zlib zlib-devel
sudo yum install libjpeg-turbo libjpeg-turbo-devel

pip install -r requirements/production.txt

## Setup Databse
sudo -u postgres createuser -D -A -P blog
sudo -u postgres createdb -O blog blog

## Start Server
gunicorn config.wsgi:application --bind 0.0.0.0:8000
sudo yum install nginx
sudo service httpd stop
sudo service nginx stop
