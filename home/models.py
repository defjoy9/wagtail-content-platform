from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

class HomePage(Page):
    pass

class AboutPage(Page):
    template = "home/about.html"

    class Meta:
        verbose_name = "About"

class StandardPage(Page):
    """
    A generic, reusable content page.
    Suitable for all simple informational pages.
    """
    template = "home/standard_page.html"

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Standard Page"
        verbose_name_plural = "Standard Pages"