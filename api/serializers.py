from rest_framework.serializers import ModelSerializer
from  rest_framework import serializers
from .models import Script
from .models import Template

class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = "__all__"

    name = serializers.CharField(required=True)
    body = serializers.CharField(required=True)

class TemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"

    name = serializers.CharField(required=True)
    body = serializers.JSONField(required=True)
