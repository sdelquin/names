# ==============================================================================
# Development Environment (macOS)
# ==============================================================================

[macos]
run:
    uv python main.py

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

deploy: && sync
    git pull
