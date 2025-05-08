# ==============================================================================
# Development Environment (macOS)
# ==============================================================================

[macos]
run:
    uv run python main.py

[macos]
sync:
    uv sync --no-group prod

# ==============================================================================
# Production Environment (Linux)
# ==============================================================================

[linux]
run:
    uv run gunicorn -b unix:/tmp/names.sock main:app

[linux]
sync:
    uv sync --no-dev --group prod

# ==============================================================================
# Miscellaneous
# ==============================================================================

deploy: && sync
    git pull
    supervisorctl restart names
