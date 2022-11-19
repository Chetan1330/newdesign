from django.urls import path
from .views import login_view, register_user, register_admin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('register1/', register_admin, name="register1"),
    path("logout/", LogoutView.as_view(), name="logout")
]
