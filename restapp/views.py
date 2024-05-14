from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view()
def helloworld(request):
    return Response({"message":"Hello,World"})