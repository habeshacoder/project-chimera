FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency files
COPY pyproject.toml ./

# Install dependencies globally (system-wide) inside the container
# --system tells uv to ignore virtualenvs
RUN uv pip install --system -r pyproject.toml

# Copy the rest of the code
COPY . .

# Now pytest will be in the system PATH
CMD ["pytest"]