from django.urls import path
from django.views.decorators.http import require_POST
from django.contrib.auth.views import LogoutView
from .views import RegisterView, LoginView, ProfileUpdateView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", require_POST(LogoutView.as_view()), name="logout"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]
