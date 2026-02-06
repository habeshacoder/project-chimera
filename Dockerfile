FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# 1. Copy ONLY the dependency files first
COPY pyproject.toml ./
# If you have a lockfile, copy it too:
# COPY uv.lock ./

# 2. Create venv and install dependencies
# We use --system or --clear to ensure a clean slate
RUN uv venv .venv && \
    . .venv/bin/activate && \
    uv pip install -r pyproject.toml

# 3. Now copy the rest of the project code
COPY . .

# Default command
CMD ["pytest"]