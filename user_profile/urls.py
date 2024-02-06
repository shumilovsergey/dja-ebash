from django.urls import path
from . import views

urlpatterns = [
    path("", views.getProfile),
    path("logout", views.logout),
    path("available_colors", views.getColors),
    path("available_avatars", views.getAvatars),
]