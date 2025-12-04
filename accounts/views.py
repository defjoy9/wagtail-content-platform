# accounts/views.py
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def signup_view(request):
    """
    User registration view with auto-login after signup.
    
    Args:
        request: HttpRequest object
    
    Returns:
        HttpResponse: Signup form (GET) or redirect to home (POST success)
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


class LoginPage(LoginView):
    """
    Custom login view with redirect for authenticated users.
    
    Redirects authenticated users to their profile page.
    Uses accounts/login.html template.
    """
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("accounts:profile")


class LogoutPage(LogoutView):
    """
    Logout view that redirects to homepage.
    
    Supports GET and POST methods for flexibility.
    """
    next_page = "/"
    http_method_names = ["get", "post", "options"]


@login_required
def profile_view(request):
    """
    Display user profile information.
    
    Requires:
        login_required: User must be authenticated
    
    Args:
        request: HttpRequest object
    
    Returns:
        HttpResponse: Profile page with user information
    """
    return render(request, "accounts/profile.html", {"user": request.user})