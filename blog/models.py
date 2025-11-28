from django.db import models
from wagtail.models import Page


class BlogIndexPage(Page):
    template = "blog/blog_index.html"

    class Meta:
        verbose_name = "Blog Index"