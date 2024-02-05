from  rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Profile
        fields = ["user", "profile_name", "color", "avatar", "auth_status"]
