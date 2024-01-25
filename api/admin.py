from django.contrib import admin
from .models import Script
from .models import Template

admin.site.register(Script)
admin.site.register(Template)