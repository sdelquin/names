#!/bin/bash

cd $(dirname $0)
source .venv/bin/activate
exec gunicorn -b unix:/tmp/names.sock main:app
