# home/management/commands/sync_nav.py
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from wagtail.models import Page, Site

from home.models import HomePage, AboutPage

PAGES = {
    "about": AboutPage,
}

class Command(BaseCommand):
    help = "Automatically creates required pages if missing"

    def handle(self, *args, **options):
        home = HomePage.objects.first()
        if not home:
            self.stderr.write("HomePage not found.")
            return
        
        for slug, model in PAGES.items():
            wagtail_slug = slugify(slug).replace("_", "-")
            existing = home.get_children().filter(slug=wagtail_slug).first()

            if not existing:
                page = model(title=slug.replace("_", " ").title(), slug=wagtail_slug)
                home.add_child(instance=page)
                page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS(f"Created: {slug}"))
            else:
                self.stdout.write(f"Exists: {slug}")
