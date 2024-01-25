from rest_framework.serializers import ModelSerializer
from .models import Script
from .models import Template

class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = "__all__"

class TemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"


