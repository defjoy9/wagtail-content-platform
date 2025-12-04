# home/templatetags/nav_tags.py
from django import template
from wagtail.models import Page, Site

register = template.Library()

def _find_page_by_slug_for_request(slug, request=None):
    """
    Find a live page by slug within the current site context.
    
    Prioritizes pages that belong to the current site's root page tree,
    falling back to any live page with matching slug.
    
    Args:
        slug: Page slug to search for
        request: HttpRequest object for site detection (optional)
    
    Returns:
        Page: Specific page instance or None if not found
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
    Get page URL by slug with fallback for missing pages.
    
    Returns absolute URL for page matching slug within current site context.
    Falls back to provided URL if page not found.
    
    Args:
        context: Template context with request
        slug: Page slug to look up
        fallback: URL to return if page not found (default: "/")
    
    Returns:
        str: Page URL or fallback URL
    
    Example:
        {% page_url "blog" "/" %}
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
    Get page title by slug with fallback text.
    
    Returns page title if found within current site context,
    otherwise returns fallback text for display.
    
    Args:
        context: Template context with request
        slug: Page slug to look up
        fallback: Text to return if page not found
    
    Returns:
        str: Page title or fallback text
    
    Example:
        {% nav_title "blog" "Blog" %}
    """
    request = context.get("request")
    p = _find_page_by_slug_for_request(slug, request=request)
    return p.title if p else fallback