# Wagtail Content Platform

A content management and publishing system I built using **Django**, **Wagtail**, **DRF**, **PostgreSQL**, **Docker**, and **Nginx**.
This project represents how I approach backend development—from structuring the architecture to deploying it on a real server.

**Live demo:** [https://defjoy.site](https://defjoy.site)

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![Wagtail](https://img.shields.io/badge/Wagtail-7.2-teal.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

# 1. Why I Built This

I created this project as a realistic backend portfolio piece.
My goals were to:

* Build a flexible CMS with Wagtail and custom page types
* Expose a clean REST API for headless use cases
* Implement authentication, permissions, and dashboards
* Deploy the platform using Docker, Nginx, Gunicorn, and PostgreSQL
* Document the full process, including production deployment

This project helped me strengthen my understanding of **system design, operations, testing, and production environments**.

---

# 2. Architecture Overview

```
                Client
                  │  HTTPS
                  ▼
            ┌────────────┐
            │    Nginx   │ (reverse proxy + SSL + static/media)
            └──────┬─────┘
                   │
              Gunicorn WSGI
                   │
                   ▼
        ┌────────────────────────┐
        │ Django + Wagtail App   │
        └──────────┬─────────────┘
                   │ ORM
                   ▼
            PostgreSQL Database
```

### Why I structured it this way:

* **Nginx** handles HTTPS, static/media, and request buffering
* **Gunicorn** runs Django efficiently
* **Docker** keeps dev and prod environments predictable
* **PostgreSQL** is production-ready compared to SQLite
* **Environment-based settings** keep configuration clean and secure

---

# 3. Key Features

## Content & Page Management

* Custom Wagtail page models
* Markdown support with syntax highlighting
* SEO fields on key page types
* Reading-time calculation
* Template tags for navigation

## REST API (DRF)

* Paginated post listing
* Individual post retrieval
* Serializer-based content shaping
* Browsable API UI

## Authentication & Permissions

* User signup and login
* Staff-only dashboard
* Role-based access

## Staff Dashboard

* Content statistics
* Post publishing analytics
* Recent activity overview

## Infrastructure & Deployment

* Dockerized multi-service environment
* Nginx reverse proxy
* Gunicorn for application serving
* PostgreSQL with persistent storage
* Environment-based production configuration
* HTTPS via Let’s Encrypt

---

# 4. Design Decisions

### Why Wagtail?

I wanted a CMS that lets me define structured page types while still giving me a powerful admin UI without writing it myself.

### Why DRF?

I wanted the content to be reusable for possible headless or external consumers.

### Why Docker?

I wanted identical environments for dev and production and a clear separation of services.

### Why Nginx + Gunicorn?

This is a standard, reliable Python production stack I wanted to gain real experience with.

---

# 5. Security Considerations

* HTTPS via Let’s Encrypt
* Strict `ALLOWED_HOSTS` in production
* CSRF protection via Django middleware
* Sanitized rich text from Wagtail
* Secure cookie settings in production
* Django-managed password hashing

---

# 6. Performance Considerations

* Static/media served by Nginx
* Pagination on API endpoints
* Prefetch/select_related on expensive queries
* Wagtail image renditions for optimized images
* GZip compression enabled in Nginx

---

# 7. Local Development Setup

```bash
git clone https://github.com/defjoy9/wagtail-content-platform.git
cd wagtail-content-platform

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access locally:

* [http://localhost:8000](http://localhost:8000)
* [http://localhost:8000/admin](http://localhost:8000/admin)
* [http://localhost:8000/api/posts/](http://localhost:8000/api/posts/)

---

# 8. Environment Configuration

Create a `.env` file:

```env
# Django
DJANGO_SECRET_KEY=
DJANGO_SETTINGS_MODULE=wagtail_content_platform.settings.dev

# Database
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

## Switching Environments

**Development:**

```bash
export DJANGO_SETTINGS_MODULE=wagtail_content_platform.settings.dev
```

**Production:**

```bash
export DJANGO_SETTINGS_MODULE=wagtail_content_platform.settings.production
```

---

# 9. Production Deployment (with Docker)

I documented my full deployment process—including DNS, Nginx, SSL, Docker networking, and troubleshooting—in my blog:

**Full deployment guide:**
[https://defjoy.site/blog/complete-deployment-guide/](https://defjoy.site/blog/complete-deployment-guide/)

Start production services:

```bash
docker compose up -d --build
```

This runs:

* Nginx
* Django + Gunicorn
* PostgreSQL

---

# 10. API Documentation

### List Posts

```
GET /api/posts/
```

### Post Detail

```
GET /api/posts/{id}/
```

### Example error response

```json
{ "detail": "Not found." }
```

Pagination is enabled by default.

---

# 11. Project Structure

```
wagtail-content-platform/
├── accounts/               # User authentication and registration
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── blog/                   # Blog application
│   ├── models.py          # BlogIndexPage, BlogPage
│   ├── api_views.py       # REST API views
│   ├── serializers.py     # DRF serializers
│   ├── templatetags/      # Custom template tags
│   └── templates/
├── dashboard/              # Staff dashboard
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── home/                   # Homepage and core pages
│   ├── models.py          # HomePage, AboutPage, StandardPage
│   ├── templatetags/      # Navigation tags
│   └── templates/
├── search/                 # Search functionality
│   ├── views.py
│   └── templates/
├── wagtail_content_platform/
│   ├── settings/
│   │   ├── base.py        # Base settings
│   │   ├── dev.py         # Development settings
│   │   └── production.py  # Production settings
│   ├── urls.py            # URL configuration
│   └── wsgi.py            # WSGI application
├── static/                 # Static assets (CSS, JS, images)
├── media/                  # User-uploaded files
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── manage.py              # Django management script
└── README.md             # This file
```

---

# 12. Management Commands

### Create Homepage

```bash
python manage.py create_homepage
```

### Sync Navigation Pages

```bash
python manage.py sync_nav
```

### Static Collection

```bash
python manage.py collectstatic --noinput
```

---

# 13. Future Improvements

* Token-based API authentication
* API versioning
* Comment system
* Redis caching
* Celery background tasks
* More dashboard analytics

---

# 14. License

MIT License.
