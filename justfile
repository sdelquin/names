# ==============================================================================
# Development Environment (macOS)
# ==============================================================================

# Run program
[macos]
run:
    uv run python main.py

# Run program
[linux]
run:
    uv run gunicorn -b unix:/tmp/names.sock main:app

# Sync uv
[macos]
sync:
    uv sync --no-group prod

# Sync uv
[linux]
sync:
    uv sync --no-dev --group prod

# Deploy program
deploy:
    git pull
    just sync
    supervisorctl restart names
