from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from django.http import HttpResponse


# from ebash.serializers import UserSerializer
from rest_framework import status
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# auth decors
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getProfile(request):

    return Response("ok")

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