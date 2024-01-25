from django.urls import path
from . import views

urlpatterns = [
    # ROUTS INFO
    path("", views.getRouts),
    # SCRIPTS
    path("scripts/", views.getScripts),
    path("scripts/create/", views.createSkript),
    path("scripts/<str:pk>/update/", views.updateSkript),
    path("scripts/<str:pk>/delete/", views.deleteScript),
    path("scripts/<str:pk>/raw/", views.rawScript),
    path("scripts/<str:pk>/", views.getScript),
    # TEMPLATES
    path("templates/", views.getTemplates),
    path("templates/create/", views.createTemplate),
    path("templates/<str:pk>/update/", views.updateTemplate),
    path("templates/<str:pk>/delete/", views.deleteTemplate),
    path("templates/<str:pk>/raw/", views.rawTemplate),
    path("templates/<str:pk>/", views.getTemplate),
]