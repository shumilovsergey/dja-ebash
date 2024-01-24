from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRouters),
    path("scripts/", views.getScripts),
    path("scripts/create/", views.createSkript),
    path("scripts/<str:pk>/update/", views.updateSkript),
    path("scripts/<str:pk>/delete/", views.deleteScript),
    path("scripts/<str:pk>/", views.getScript),
]