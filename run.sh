#!/bin/bash

cd "$(dirname "$0")"
exec uv run gunicorn -b unix:/tmp/names.sock main:app
