from django.urls import path
from . import views

urlpatterns = [
    path("", views.getProfile),
    path("login/username", views.username),
    path("login/password", views.password),
    path("logout", views.logout),
    path("available_colors", views.getColors),
    path("available_avatars", views.getAvatars),
]