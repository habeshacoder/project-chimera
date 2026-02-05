# Base image for Python 3.12 on Windows-compatible (use Linux container if needed)
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Install uv for env management
RUN pip install uv

# Copy project files
COPY . .

# Setup virtual env and install deps
RUN uv venv .venv && \
    . .venv/bin/activate && \
    uv pip install -r pyproject.toml

# Default command: Run tests
CMD ["pytest"]