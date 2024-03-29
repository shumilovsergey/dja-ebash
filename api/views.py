from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScriptSerializer
from .serializers import TemplateSerializer
from .models import Script
from .models import Template
from django.http import HttpResponse


# from ebash.serializers import UserSerializer
from rest_framework import status
# from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

# auth decors
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#const 
from ebash.const import DOMAIN_NAME
from ebash.const import BASH_BEGINING
from ebash.const import BASH_SPLITER
from ebash.info import ROUT_INFO


# Routs INFO
@api_view(['GET'])
def getRouts(request):
    return Response(ROUT_INFO)

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