from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import random
import requests

from ebash.const import BOT_URL
# auth decors
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def login(request):
    data = request.data
    user = get_object_or_404(User, username=data["username"])

    if not user.check_password(data["password"]):
        return Response({"detail": "Not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    s = UserSerializer(instance=user)
    return Response({"token": token.key, "user": s.data})

@api_view(["POST"])
def signup(request):
    data = request.data
    s = UserSerializer(data=data)
    if s.is_valid():
        s.save()
        user = User.objects.get(username=data["username"])
        user.set_password(data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": s.data})
    
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("pased for {}".format(request.user.username))


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.auth.delete()
    return Response("logout for {}".format(request.user.username))

@api_view(["GET"])
def tg_login(request):
    username = str(random.randint(1, 1000000))
    password = str(random.randint(1, 1000000))

    data = {
        "username":username,
        "password":password
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        serializer
        user = User.objects.get(username=username)
        token = Token.objects.create(user=user)
    return Response(f"https://t.me/wget_bash_bot?start={token.key}")