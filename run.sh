#!/bin/bash
# Master script.

cd "$(dirname "$0")"
PYTHON_VENV=$(pipenv --venv)
SOCKET=$(cat .env | grep UWSGI_PORT | cut -f 2 -d '=' | xargs)
exec uwsgi --home $PYTHON_VENV --socket :$SOCKET --ini uwsgi.ini
