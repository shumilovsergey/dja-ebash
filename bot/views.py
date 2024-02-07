from django.shortcuts import render
from ebash.const import TOKEN
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from user_profile.models import Profile
from .serializers import telegram_format

import json

KEYMOARD = {
        "inline_keyboard" :  [
            [
                {'text': '◀', 'callback_data': json.dumps({"menu":"menu"})}
            ]
        ]
}

@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)
    
    # print(r)






#     json = flatten_json(request.data)
#     if "message.text" in json:
#         text = json["message.text"]
#         if "/start" in text and len(text) > 8:
#             key = text.replace("/start ", "")
#             chat_id = json["message.from.id"]
#             info = user_info(json)

# # IS USER EXIST?
#             try:
#                 user = User.objects.get(username=chat_id)
#             except:
#                 user = ""

# # DELETE OLD TOKEN OF EXIST USER
#             try:  
#                 token = Token.objects.get(user=user)
#                 token.delete()
#             except:
#                 pass

# # REFRASH NEW TOKEN OF EXIST USER
#             try:
#                 token = Token.objects.get(key=key)
#                 old_user = token.user
#                 token.user = user
#                 profile = Profile.objects.get_or_create(user=user)
#                 token.save()
#                 old_user.delete()
#             except:
#                 pass     
# # CTEATE NEW USER AND SET TOKEN
#             try:
#                 token = Token.objects.get(key=key)
#                 user = token.user
#                 user.username = chat_id
#                 profile = Profile.objects.get_or_create(user=user)
#                 user.save()
#             except:
#                 # BAD TOKEN BUT EXIST USER
#                 token = Token.objects.create(user=user)
                
    return Response("ok", status=200)
# 
# 
# https://t.me/wget_bash_bot?start=81479fd7094e7adade40261a8eda663769efbb8f

