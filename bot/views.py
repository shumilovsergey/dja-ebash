from django.shortcuts import render
from ebash.const import TOKEN
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def getMessage(request):
    json = flatten_json(request.data)
    if "message.text" in json:
        text = json["message.text"]
        if "/start" in text and len(text) > 8:
            key = text.replace("/start ", "")
            chat_id = json["message.from.id"]
            info = user_info(json)

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
                token.save()
                old_user.delete()
            except:
                pass     
# CTEATE NEW USER AND SET TOKEN
            try:
                token = Token.objects.get(key=key)
                user = token.user
                user.username = chat_id
                user.save()
            except:
                # BAD TOKEN BUT EXIST USER
                token = Token.objects.create(user=user)
                
    return Response()
# 
# 
# https://t.me/wget_bash_bot?start=81479fd7094e7adade40261a8eda663769efbb8f

def flatten_json(json_obj, prefix=''):
    flat_json = {}
    for key, value in json_obj.items():
        new_key = f"{prefix}{key}"
        if isinstance(value, dict):
            flat_json.update(flatten_json(value, f"{new_key}."))
        else:
            flat_json[new_key] = value
    return flat_json

def user_info(json):
    if "message.from.first_name" in json:
        user_info = json["message.from.first_name"]
    elif "message.from.last_name" in json:
        user_info = json["message.from.last_name"]
    elif "message.from.username" in json:
        user_info = json["message.from.username"]

    else:
        user_info = "anonym user"
    return user_info