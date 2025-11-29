from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField


class SeoFields(models.Model):
    """
    Abstract model providing SEO meta fields for pages.
    """
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        help_text="Override the default page title for SEO"
    )
    meta_description = models.TextField(
        blank=True,
        help_text="A brief description for search engines (150-160 characters recommended)"
    )

    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel('meta_title'),
                FieldPanel('meta_description'),
            ],
            heading="SEO Settings",
        ),
    ]

    class Meta:
        abstract = True


class HomePage(SeoFields, Page):
    pass


class AboutPage(SeoFields, Page):
    template = "home/about.html"

    class Meta:
        verbose_name = "About"


class StandardPage(SeoFields, Page):
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