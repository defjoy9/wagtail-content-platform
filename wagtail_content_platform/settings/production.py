# wagtail_content_platform/settings/production.py
from .base import *
import os
from dotenv import load_dotenv

load_dotenv(BASE_DIR / ".env")

DEBUG = False

ALLOWED_HOSTS = [
    "defjoy.site",
    "www.defjoy.site",
    "localhost",
    "127.0.0.1",
    "64.226.105.246",
]

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# -------------------------------------------------------------------
# STATICFILES
# -------------------------------------------------------------------

STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES["staticfiles"]["BACKEND"] = (
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
)

# -------------------------------------------------------------------
# DATABASE (Postgres)
# -------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# -------------------------------------------------------------------
# LOGGING
# -------------------------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "django.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {"handlers": ["file"], "level": "INFO", "propagate": True},
    },
}