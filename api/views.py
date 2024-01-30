from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScriptSerializer
from .serializers import TemplateSerializer
from .models import Script
from .models import Template
from django.http import HttpResponse


from ebash.serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# auth decors
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



DOMAIN_NAME = "http://127.0.0.1:8000/"
BASH_BEGINING = "#!/bin/bash\r\n\r\n"
BASH_SPLITER = "\r\n\r\necho \"----------------------------------------------------------------\""

# Routs INFO
@api_view(['GET'])
def getRouts(request):
    routs = [
        {
            "endpoint": "/",
            "method" : "GET",
            "required": "none",
            "description": "список всех роутов",
            "auth": "none"
        },
        {
            "endpoint": "login/",
            "method" : "POST",
            "required": "username(str), password(str)",
            "description": "логинимся тут",
            "auth": "none"
        },
        {
            "endpoint": "signup/",
            "method" : "POST",
            "required": "username(str), password(str), email(str)",
            "description": "регаемся тут",
            "auth": "none"
        },
        {
            "endpoint": "logout/",
            "method" : "GET",
            "required": "none",
            "description": "отрицательно логинимся тут",
            "auth": "обязательно"
        },
        {
            "endpoint": "scripts/",
            "method" : "GET",
            "required": "none",
            "description": "вывод всех скриптов пользователя",
            "auth": "обязательно"
        },
        {
            "endpoint": "scripts/<id>/",
            "method" : "GET",
            "required": "none",
            "description": "вывод скрипта <id>",
            "auth": "none"
        },
        {
            "endpoint": "scripts/create/",
            "method" : "POST",
            "required": "name(str), body(str)",
            "description": "создание скрипта",
            "auth": "обязательно"
        },
        {
            "endpoint": "scripts/<id>/update/",
            "method" : "PUT",
            "required": "name(str), body(str), color(str)",
            "description": "редактирование скрипта <id>",
            "auth": "обязательно"
        },
        {
            "endpoint": "scripts/<id>/delete/",
            "method" : "DELETE",
            "required": "none",
            "description": "удаление скрипта <id>",
            "auth": "обязательно"
        },
        {
            "endpoint": "scripts/<id>/raw/",
            "method" : "GET",
            "required": "none",
            "description": "вывод RAW скрипта <id>",
            "auth": "none"
        },
        {
            "endpoint": "templates/",
            "method" : "GET",
            "required": "none",
            "description": "вывод всех шаблонов пользователя",
            "auth": "обязательно"
        },
        {
            "endpoint": "templates/<id>/",
            "method" : "GET",
            "required": "none",
            "description": "вывод шаблона <id>",
            "auth": "none"
        },
        {
            "endpoint": "templates/create/",
            "method" : "POST",
            "required": "name(str), body(json)",
            "description": "создание шаблона. структура json. ключ (str) - порядковый номер выполнения, значение (str) - id скрипта",
            "auth": "обязательно"
        },
        {
            "endpoint": "templates/<id>/update/",
            "method" : "PUT",
            "required": "name(str), body(json)",
            "description": "редактирование шаблона <id>. структура json. ключ (str) - порядковый номер выполнения, значение (str) - id скрипта",
            "auth": "обязательно"
        },
        {
            "endpoint": "templates/<id>/delete/",
            "method" : "DELETE",
            "required": "none",
            "description": "удаление шаблона <id>",
            "auth": "обязательно"
        },
        {
            "endpoint": "templates/<id>/raw/",
            "method" : "GET",
            "required": "none",
            "description": "вывод RAW шаблона <id>",
            "auth": "none"
        },   
           {
            "endpoint": "templates/<id>/raw/",
            "method" : "GET",
            "required": "none",
            "description": "вывод RAW шаблона <id>",
            "auth": "none"
        },
    ]
    return Response(routs)

##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__

# GET SCRIPTS
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getScripts(request):
    user_id = request.user.id
    scripts = Script.objects.filter(author_id=user_id)
    serializer = ScriptSerializer(scripts, many=True)
    return Response(serializer.data)

# GET SCRIPT
@api_view(["GET"])
def getScript(request, pk):
    script = get_object_or_404(Script, id=pk)    
    serializer = ScriptSerializer(script, many=False)
    return Response(serializer.data)

# CREATE SCRIPT
@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def createSkript(request):
    data = request.data
    user_id = request.user.id
    

    serializer = ScriptSerializer(data=data)
    if serializer.is_valid():
        script = Script.objects.create(
            name=data["name"],
            author_id=user_id,
            body=data["body"],
            color=data["color"]
        )
        
        url = f"sudo wget -0 {script.name}.sh " + DOMAIN_NAME + f"scripts/{script.id}/raw && chmod +x {script.name}.sh && ./{script.name}.sh" 
        script.url = url
        script.save()

        return Response(ScriptSerializer(script).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UPDATE SKRIPT
@api_view(["PUT"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateSkript(request, pk):
    data = request.data
    script = get_object_or_404(Script, id=pk)
    if script.author_id != request.user.id:
        return Response("this is not you script. GTFO!", status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ScriptSerializer(script, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE SCRIPT
@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteScript(request, pk):
    script = get_object_or_404(Script, id=pk)
    if script.author_id != request.user.id:
        return Response("this is not you script. GTFO!", status=status.HTTP_400_BAD_REQUEST)
    
    script.delete()
    return Response("Skript delete sucksesfuly")

# GET RAW SCRIPT
@api_view(["GET"])
def rawScript(request, pk):
    try:
        script = Script.objects.get(id=pk)
    except:
        return Response("Этот скрипт отсутствует в базе!", status=status.HTTP_400_BAD_REQUEST)

    raw_script_name = f"\r\necho \"complited {script.name} \" "
    raw = BASH_BEGINING + script.body + BASH_SPLITER + raw_script_name + BASH_SPLITER
    return HttpResponse(raw, content_type='text/plain')

##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__

# GET TEMPLATES
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getTemplates(request):
    user_id=request.user.id
    templates = Template.objects.filter(author_id=user_id)
    serializer = TemplateSerializer(templates, many=True)
    return Response(serializer.data)

# GET TEMPLATE
@api_view(["GET"])
def getTemplate(request, pk):
    template = get_object_or_404(Template, id=pk)
    serializer = TemplateSerializer(template, many=False)
    return Response(serializer.data)

# CREATE TEMPLATE
@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def createTemplate(request):
    data = request.data
    user_id = request.user.id
    serializer = TemplateSerializer(data=data)

    if serializer.is_valid():
        template = Template.objects.create(
            name=data["name"],
            author_id=user_id,
            body=data["body"],
        )
        url = f"sudo wget -0 {template.name}.sh " + DOMAIN_NAME + f"templates/{template.id}/raw && chmod +x {template.name}.sh && ./{template.name}.sh"
        template.url = url
        template.save()

        return Response(ScriptSerializer(template).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TEMPLATES UPDATE
@api_view(["PUT"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateTemplate(request, pk):
    data=request.data
    template = get_object_or_404(Template, id=pk)
    if template.author_id != request.user.id:
        return Response("this is not you template. GTFO!", status=status.HTTP_400_BAD_REQUEST)
    
    serializer = TemplateSerializer(template, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE TEMPLATE
@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteTemplate(request, pk):
    template = get_object_or_404(Template, id=pk)
    if template.author_id != request.user.id:
        return Response("this is not you template. GTFO!", status=status.HTTP_400_BAD_REQUEST)
    
    template.delete()
    return Response("Template delete suck-sesfuly")

# GET RAW TEMPLATE
@api_view(["GET"])
def rawTemplate(request, pk):
    try:
        template = Template.objects.get(id=pk)
    except:
        return Response("Такого шаблона не существует!", status=status.HTTP_400_BAD_REQUEST)
    
    json_data = template.body
    raw = ""
    
    for i in range(len(json_data)):
        try:
            script = Script.objects.get(id=json_data[str(i)])
        except:
            return Response("В шаблоне обнаружен удаленный скрипт! Отредактируйте шаблон и повторите попытку ", status=status.HTTP_400_BAD_REQUEST)

        raw_script_name = f"\r\necho \"complited {script.name} \" "
        raw_script_name = BASH_SPLITER + raw_script_name + BASH_SPLITER
        raw = raw + "\r\n" + script.body + raw_script_name
    
    raw = BASH_BEGINING + raw
    return HttpResponse(raw, content_type='text/plain')