from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
