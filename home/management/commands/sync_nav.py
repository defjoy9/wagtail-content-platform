# home/management/commands/sync_nav.py
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from wagtail.models import Page, Site

from home.models import HomePage, AboutPage
from blog.models import BlogIndexPage

PAGES = {
    "about": AboutPage,
    "blog": BlogIndexPage,
}

class Command(BaseCommand):
    """
    Django management command to create required site pages.
    
    Creates About and Blog Index pages under HomePage if they don't exist.
    Ensures consistent site structure for navigation.
    
    Usage:
        python manage.py sync_nav
    """
    help = "Automatically creates required pages if missing"

    def handle(self, *args, **options):
        """
        Create missing pages under HomePage.
        
        Checks for existing pages by slug and creates them if missing.
        Publishes new pages immediately after creation.
        """
        home = HomePage.objects.first()
        if not home:
            self.stderr.write("HomePage not found.")
            return
        
        for slug, model in PAGES.items():
            wagtail_slug = slugify(slug).replace("_", "-")
            existing = home.get_children().filter(slug=wagtail_slug).first()

            if not existing:
                title = slug.replace("_", " ").title()
                page = model(title=title, slug=wagtail_slug)
                home.add_child(instance=page)
                page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS(f"Created: {slug}"))
            else:
                self.stdout.write(f"Exists: {slug}")
