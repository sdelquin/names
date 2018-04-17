#!/bin/bash
# Master script.

cd "$(dirname "$0")"
source ~/.virtualenvs/names/bin/activate
exec uwsgi --ini uwsgi.cfg
