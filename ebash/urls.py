from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # MAIN PATH
    path("", include("api.urls")),

    # PROFILE
    path("profile/", include("user_profile.urls")),

    # BOT
    path("bot/", include("bot.urls")),

    # ADMIN
    path('admin/', admin.site.urls),

    # USER MANAGER
    re_path("test_token", views.test_token),
    re_path("tg_login", views.tg_login),
    re_path("tg_logout", views.tg_logout),
]
