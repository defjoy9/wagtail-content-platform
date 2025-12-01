# wagtail_content_platform/dev.py
from .base import *
import os
from dotenv import load_dotenv

load_dotenv(BASE_DIR / ".env")

DEBUG = True
ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret-key")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "dev.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"