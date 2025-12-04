from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from django.core.paginator import Paginator
from wagtailmarkdown.fields import MarkdownField
from home.models import SeoFields


class BlogIndexPage(SeoFields, Page):
    """
    Blog index page that lists all blog posts with pagination.
    
    Displays blog posts in reverse chronological order (newest first)
    with 5 posts per page.
    """
    template = "blog/blog_index.html"

    subpage_types = ['blog.BlogPage']

    def get_context(self, request, *args, **kwargs):
        """Add paginated blog posts to template context."""
        context = super().get_context(request, *args, **kwargs)
        
        posts = (
            self.get_children()
            .live()
            .specific()
            .order_by('-first_published_at')
        )
        
        paginator = Paginator(posts, 5)
        page = request.GET.get("page")
        
        context["posts"] = paginator.get_page(page)
        return context

    class Meta:
        verbose_name = "Blog Index"


class BlogPage(SeoFields, Page):
    """
    Individual blog post page with markdown content.
    
    Supports markdown formatting with syntax-highlighted code blocks,
    includes publication date and reading time estimate.
    """
    date = models.DateField("Post date")
    body = MarkdownField()

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []