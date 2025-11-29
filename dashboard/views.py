# dashboard/views.py
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models.functions import TruncMonth
from django.db.models import Count
from wagtail.models import Page
from blog.models import BlogPage


@staff_member_required
def dashboard_view(request):
    """
    Dashboard view for staff members showing site statistics and latest content.
    """
    # Total blog posts
    total_blog_posts = BlogPage.objects.live().count()
    
    # Posts per month
    posts_per_month = (
        BlogPage.objects.live()
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('-month')[:6]
    )

    total_pages = Page.objects.live().count()

    latest_posts = BlogPage.objects.live().order_by('-date')[:5]

    total_users = User.objects.count()
    
    context = {
        'total_blog_posts': total_blog_posts,
        'posts_per_month': posts_per_month,
        'total_pages': total_pages,
        'latest_posts': latest_posts,
        'total_users': total_users,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

