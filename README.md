# Wagtail Content Platform

A production-ready content management system built with Django and Wagtail CMS, demonstrating modern web development practices, RESTful API design, and containerized deployment infrastructure.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Wagtail](https://img.shields.io/badge/Wagtail-7.2-teal.svg)](https://wagtail.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Live Demo:** [defjoy.site](https://defjoy.site)

---

## 🎯 Overview

This platform is a full-featured CMS designed for technical content publishing, showcasing enterprise-level Django/Wagtail development with emphasis on:

- **Content Management**: Hierarchical page structures with custom page types and rich text editing
- **REST API**: Django REST Framework endpoints for headless CMS capabilities
- **Authentication**: User registration, role-based permissions, and staff dashboards
- **Production Infrastructure**: Docker containerization, Nginx reverse proxy, PostgreSQL database
- **Developer Experience**: Markdown support with syntax highlighting, SEO optimization, and comprehensive admin tools

---

## ✨ Key Features

### Content Management
- **Wagtail CMS Integration**: Hierarchical page models with draft/publish workflows
- **Custom Page Types**: Blog posts, standard pages, about pages with SEO fields
- **Markdown Support**: Full markdown editing with syntax-highlighted code blocks
- **Media Management**: Image uploads with automatic optimization
- **Search Functionality**: Full-text search across all content

### REST API
- **Django REST Framework**: JSON endpoints for content distribution
- **List & Detail Views**: Paginated blog post listing and individual post retrieval
- **Serializers**: Clean data representation with nested relationships
- **Browsable API**: Interactive API documentation at `/api/posts/`

### Authentication & Authorization
- **User Registration**: Custom signup with email validation
- **Login System**: Session-based authentication
- **Role-Based Access**: Staff-only dashboards and content management
- **Profile Management**: User account settings

### Admin & Dashboard
- **Staff Dashboard**: Content statistics, time-series data, recent activity
- **Wagtail Admin**: Enhanced with custom CSS for markdown editor visibility
- **Content Analytics**: Post counts, publishing metrics, user engagement

### Developer Features
- **macOS Terminal Code Blocks**: Styled code blocks with copy-to-clipboard
- **Reading Time Calculator**: Template tag for estimated reading duration
- **Navigation Tags**: Reusable template tags for site navigation
- **Environment-Based Settings**: Separate dev/production configurations

---

## 🛠️ Tech Stack

### Backend
- **Django 5.2** - Web framework with ORM, authentication, middleware
- **Wagtail 7.2** - Enterprise CMS with hierarchical page models
- **Django REST Framework 3.16** - RESTful API toolkit
- **PostgreSQL** - Production database (SQLite for development)
- **Gunicorn 20.0** - WSGI HTTP server

### Frontend
- **Vanilla JavaScript** - No framework dependencies
- **CSS3** - Custom styling with CSS variables and grid layouts
- **Wagtail Templates** - Server-side rendering with Django template language

### Infrastructure
- **Docker** - Containerization for consistent environments
- **Nginx** - Reverse proxy and static file serving
- **Let's Encrypt** - Automated SSL/TLS certificates
- **DigitalOcean** - Cloud hosting (Ubuntu 24.04 LTS)

### Development Tools
- **python-dotenv** - Environment variable management
- **Markdown & Pygments** - Content formatting and syntax highlighting
- **wagtail-markdown** - Markdown field support in Wagtail admin

---

## 📋 Prerequisites

- **Python 3.12+**
- **PostgreSQL 14+** (for production)
- **Docker & Docker Compose** (for containerized deployment)
- **Git**

---

## 🚀 Quick Start

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/defjoy9/wagtail-content-platform.git
   cd wagtail-content-platform
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - **Frontend**: http://localhost:8000
   - **REST API**: http://localhost:8000/api/posts/

---

### Complete Production Setup

For a comprehensive production deployment guide including:
- DNS configuration (Namecheap)
- DigitalOcean droplet setup
- PostgreSQL database configuration
- Nginx reverse proxy with SSL
- Docker networking and volumes
- Troubleshooting common issues

**See:** [Complete Production Deployment Guide](blog-posts/05-complete-deployment-guide.md)

---

## 📁 Project Structure

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

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Django/Wagtail
DJANGO_SECRET_KEY=
DJANGO_SETTINGS_MODULE=w

# PostgreSQL
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

### Development vs Production

- **Development**: Uses `dev.py` settings with SQLite, DEBUG=True, and local static files
- **Production**: Uses `production.py` settings with PostgreSQL, DEBUG=False, and collected static files

Switch between environments:
```bash
# Development
export DJANGO_SETTINGS_MODULE=wagtail_content_platform.settings.dev

# Production
export DJANGO_SETTINGS_MODULE=wagtail_content_platform.settings.production
```

---

## 📚 API Documentation

### Endpoints

#### List All Blog Posts
```http
GET /api/posts/
```

**Response:**
```json
{
  "count": 10,
  "next": "http://localhost:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Getting Started with Wagtail",
      "slug": "getting-started-with-wagtail",
      "date": "2024-12-01",
      "body": "Content here...",
      "url": "/blog/getting-started-with-wagtail/"
    }
  ]
}
```

#### Get Single Blog Post
```http
GET /api/posts/{id}/
```

**Response:**
```json
{
  "id": 1,
  "title": "Getting Started with Wagtail",
  "slug": "getting-started-with-wagtail",
  "date": "2024-12-01",
  "body": "Full content...",
  "url": "/blog/getting-started-with-wagtail/",
  "meta_title": "Getting Started with Wagtail - Wagtail CMS",
  "meta_description": "Learn the basics of Wagtail CMS..."
}
```

## 📝 Management Commands

### Create Homepage (if not exists)
```bash
python manage.py create_homepage
```

### Sync Navigation Pages
```bash
python manage.py sync_nav
```
Creates required site pages (About, Blog Index) if they don't exist under HomePage.

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Database Operations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

---

## 🎨 Customization

### Adding New Page Types

1. Create model in `home/models.py` or `blog/models.py`:
   ```python
   from wagtail.models import Page
   from wagtail.fields import RichTextField
   from wagtail.admin.panels import FieldPanel

   class CustomPage(Page):
       body = RichTextField()
       
       content_panels = Page.content_panels + [
           FieldPanel('body'),
       ]
   ```

2. Create template in `templates/app_name/custom_page.html`

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Custom Template Tags

Create reusable template tags in `templatetags/` directory:
```python
from django import template

register = template.Library()

@register.simple_tag
def custom_tag(value):
    return f"Processed: {value}"
```

---

## 🚦 Deployment Checklist

- [ ] Set `DEBUG = False` in production settings
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set strong `SECRET_KEY`
- [ ] Configure PostgreSQL database
- [ ] Run `collectstatic` for static files
- [ ] Set up Nginx reverse proxy
- [ ] Configure SSL certificates (Let's Encrypt)
- [ ] Set up database backups
- [ ] Configure logging and monitoring
- [ ] Test all functionality in production environment

---

## 📄 License

This project is licensed under the MIT License.