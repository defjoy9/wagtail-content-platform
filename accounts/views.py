# accounts/views.py
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def signup_view(request):
    """
    Handle user registration with Django's built-in UserCreationForm.
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
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("accounts:profile")


class LogoutPage(LogoutView):
    next_page = "/"
    http_method_names = ["get", "post", "options"]


@login_required
def profile_view(request):
    """
    Simple user profile page.
    Shows username, email, and any other fields you decide to add later.
    """
    return render(request, "accounts/profile.html", {"user": request.user})