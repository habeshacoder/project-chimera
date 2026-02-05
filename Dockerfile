FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --no-cache-dir pip && pip install --no-cache-dir poetry || true
COPY . /app
CMD ["python", "-m", "pytest"]
