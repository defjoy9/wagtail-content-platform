# Base image
FROM python:3.12-slim-bookworm

# Add app user
RUN useradd wagtail

# Avoid buffering
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Install system dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Gunicorn
RUN pip install "gunicorn==20.0.4"

# Install Python deps
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Set work directory
WORKDIR /app

# Set permissions
RUN chown -R wagtail:wagtail /app

# Copy source code
COPY --chown=wagtail:wagtail . .

# Switch to wagtail user
USER wagtail

# Expose port
EXPOSE 8000

CMD set -xe; \
    python manage.py migrate --noinput; \
    gunicorn wagtail_content_platform.wsgi:application