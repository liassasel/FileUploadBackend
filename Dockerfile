FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    gcc \
    python3-dev \
    libpq-dev && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    echo "deb http://apt.postgresql.org/pub/repos/apt bookworm-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client-17 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt



FROM python:3.11-slim


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    libpq5 \
    netcat-openbsd && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    echo "deb http://apt.postgresql.org/pub/repos/apt bookworm-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client-17 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN mkdir -p /backups && chmod 777 /backups

WORKDIR /app


COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PGDUMP_PATH="/usr/lib/postgresql/17/bin/pg_dump"  

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
