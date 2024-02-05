from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from ebash.const import AVATARS
from ebash.const import COLORS
from .serializers import ProfileSerializer

from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# auth decors
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user_id = request.user.id
    user = get_object_or_404(User, id=user_id)
    profile = Profile.objects.get_or_create(user=user)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def username(request):
    return

@api_view(["POST"])
def password(request):
    return

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.auth.delete()
    return Response("logout for {}".format(request.user.username))

@api_view(["GET"])
def getColors(request):
    return Response({'available_colors': COLORS})

@api_view(["GET"])
def getAvatars(request):
    return Response({'available_avatars': AVATARS})