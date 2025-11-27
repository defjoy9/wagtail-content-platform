# home/templatetags/nav_tags.py
from django import template
from wagtail.models import Page, Site

register = template.Library()

def _find_page_by_slug_for_request(slug, request=None):
    """
    Find a live page by slug, preferring pages that belong to the current Site root.
    Returns a specific page instance or None.
    """
    qs = Page.objects.live().filter(slug=slug).specific()

    if request is not None:
        # try to find site for request first
        try:
            site = Site.find_for_request(request)
        except Exception:
            site = None

        if site:
            # prefer pages that are descendants of the site's root_page
            root = site.root_page
            candidate = qs.filter(path__startswith=root.path).first()
            if candidate:
                return candidate

    # fallback to first live page with that slug anywhere
    return qs.first()

@register.simple_tag(takes_context=True)
def page_url(context, slug, fallback="/"):
    """
    Return the url for the page with `slug` relative to the current Site, or fallback.
    Usage: {% page_url "healthy-brains" "/" %}
    """
    request = context.get("request")
    p = _find_page_by_slug_for_request(slug, request=request)
    if not p:
        return fallback
    # ensure absolute URL (use .url)
    url = p.url
    return url if url else fallback

@register.simple_tag(takes_context=True)
def nav_title(context, slug, fallback):
    """
    Return the page title if it exists on the current Site, otherwise return fallback.
    Usage: {% nav_title "healthy-brains" "Healthy Brains" %}
    """
    request = context.get("request")
    p = _find_page_by_slug_for_request(slug, request=request)
    return p.title if p else fallback