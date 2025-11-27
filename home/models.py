from django.db import models
from wagtail.models import Page


class HomePage(Page):
    pass

class AboutPage(Page):
    template = "home/about.html"

    class Meta:
        verbose_name = "About"