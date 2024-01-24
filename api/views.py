from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScriptSerializer
from .models import Script

@api_view(['GET'])
def getRouters(request):
    routs = [
        {
            "endpoint": "//",
            "method" : "GET",
            "body": "dick",
            "description": "rout map"
        }
    ]
    return Response(routs)

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
    data = request.data
    script = Script.objects.get(id=pk)
    script.delete()
    return Response("Deleted sucksesfuly")