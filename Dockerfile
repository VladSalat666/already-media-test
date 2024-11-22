FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PROD=True
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=already_media_test.settings
ENV MONGO_HOST=host.docker.internal
ENV DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1


CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
