from django.shortcuts import render
from rest_framework.decorators import api_view ,throttle_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
# Create your views here.

@api_view()
def helloworld(request):
    return Response({"message":"Hello,World"},status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '5/day'

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})