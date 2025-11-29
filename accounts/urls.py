# accounts urls.py
from django.urls import path
from .views import signup_view, LoginPage, LogoutPage, profile_view

app_name = "accounts"

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", LoginPage.as_view(), name="login"),
    path("logout/", LogoutPage.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
]