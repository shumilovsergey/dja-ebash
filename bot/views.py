from django.shortcuts import render
from ebash.const import TOKEN
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def getMessage(request):
    return