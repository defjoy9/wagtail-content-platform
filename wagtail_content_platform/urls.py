# wagtail_content_platform/urls.py
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap as wagtail_sitemap
from django.conf.urls.static import static
from search import views as search_views

urlpatterns = [
    # Django admin
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),

    # Public accounts system
    path("accounts/", include("accounts.urls")),
    
    # Staff dashboard
    path("dashboard/", include("dashboard.urls")),
    
    # REST API
    path("api/", include("blog.api_urls")),
    
    # SEO
    path("sitemap.xml", wagtail_sitemap, name="sitemap"),

    # Wagtail FRONTEND (must always be last)
    path("", include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)