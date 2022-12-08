#!/bin/bash

source ~/.pyenv/versions/names/bin/activate
cd "$(dirname "$0")"
exec gunicorn -c gunicorn.conf.py main:app
