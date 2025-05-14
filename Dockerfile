FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Crear directorios necesarios (media y migrations)
RUN mkdir -p /app/media/uploads
RUN mkdir -p /app/files/migrations

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]