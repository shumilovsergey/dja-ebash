from django.shortcuts import render
from ebash.const import TOKEN
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from user_profile.models import Profile
from .serializers import telegram_format
import json
from dataclasses_serialization.json import JSONSerializer


@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)

    if message.error:
        serializer = JSONSerializer.serialize(message)
        return Response("ok", status=200)
    
    if message.text and "/start" in message.text and len(message.text) > 8:
        tokenStart(message)

    if message.text:
        message.sendAudio()

    return Response("ok", status=200)


###
###   ENDPOINTS
###

def tokenStart(message):
    text=message["text"]
    key = text.replace("/start ", "")
    chat_id = message["chat_id"]

# IS USER EXIST?
    try:
        user = User.objects.get(username=chat_id)
    except:
        user = ""

# DELETE OLD TOKEN OF EXIST USER
    try:  
        token = Token.objects.get(user=user)
        token.delete()
    except:
        pass

# REFRASH NEW TOKEN OF EXIST USER
    try:
        token = Token.objects.get(key=key)
        old_user = token.user
        token.user = user
        profile = Profile.objects.get_or_create(user=user)
        token.save()
        old_user.delete()
    except:
        pass     
# CTEATE NEW USER AND SET TOKEN
    try:
        token = Token.objects.get(key=key)
        user = token.user
        user.username = chat_id
        profile = Profile.objects.get_or_create(user=user)
        user.save()
    except:
        # BAD TOKEN BUT EXIST USER
        token = Token.objects.create(user=user)
                



