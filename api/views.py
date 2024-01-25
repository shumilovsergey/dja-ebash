from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScriptSerializer
from .serializers import TemplateSerializer
from .models import Script
from .models import Template
from django.http import HttpResponse

BASH_BEGINING = "#!/bin/bash\r\n"
BASH_SPLITER = "\r\necho \"----------------------------------------------------------------\""

# Routs INFO
@api_view(['GET'])
def getRouts(request):
    routs = [
        {
            "endpoint": "//",
            "method" : "GET",
            "body": "dick",
            "description": "rout map"
        }
    ]
    return Response(routs)

#SCRIPT
@api_view(["GET"])
def getScripts(request):
    scripts = Script.objects.all()
    serializer = ScriptSerializer(scripts, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getScript(request, pk):
    script = Script.objects.get(id=pk)
    serializer = ScriptSerializer(script, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createSkript(request):
    data = request.data

    script = Script.objects.create(
        name=data["name"],
        author_id=data["author_id"],
        body=data["body"]
    )
    serializer = ScriptSerializer(script, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateSkript(request, pk):
    data = request.data

    script = Script.objects.get(id=pk)
    serializer = ScriptSerializer(script, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteScript(request, pk):
    script = Script.objects.get(id=pk)
    script.delete()
    return Response("Skript delete sucksesfuly")

@api_view(["GET"])
def rawScript(request, pk):
    script = Script.objects.get(id=pk)
    raw_script_name = f"\r\necho \"complited {script.name} \" "
    raw = BASH_BEGINING + script.body + BASH_SPLITER + raw_script_name + BASH_SPLITER
    return HttpResponse(raw, content_type='text/plain')

#TEMPLATE
@api_view(["GET"])
def getTemplates(request):
    templates = Template.objects.all()
    serializer = TemplateSerializer(templates, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getTemplate(request, pk):
    template = Template.objects.get(id=pk)
    serializer = TemplateSerializer(template, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createTemplate(request):
    data = request.data
    template = Template.objects.create(
        name=data["name"],
        author_id=data["author_id"],
        body=data["body"]
    )
    serializer = TemplateSerializer(template, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateTemplate(request, pk):
    template = Template.objects.get(id=pk)
    serializer = TemplateSerializer(template, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteTemplate(request, pk):
    template = Template.objects.get(id=pk)
    template.delete()
    return Response("Template delete suck-sesfuly")

@api_view(["GET"])
def rawTemplate(request, pk):
    template = Template.objects.get(id=pk)
    json_data = template.body
    raw = ""
    
    for i in range(len(json_data)):
        script = Script.objects.get(id=json_data[str(i)])
        raw_script_name = f"\r\necho \"complited {script.name} \" "
        raw_script_name = BASH_SPLITER + raw_script_name + BASH_SPLITER
        raw = raw + "\r\n" + script.body + raw_script_name
    
    raw = BASH_BEGINING + raw
    return HttpResponse(raw, content_type='text/plain')