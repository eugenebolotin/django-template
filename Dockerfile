FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app
ENV PYTHONPATH="/app"

# Install system dependencies (suppose to use Postgres by default)
RUN apt-get update && apt-get install -y build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and install project dependencies
COPY pyproject.toml /app/

RUN uv venv
RUN uv pip install .

# Copy the rest of the project source code
COPY . /app/

# Expose the port and define the application start command
EXPOSE 8000
CMD ["/app/scripts/run.sh"]