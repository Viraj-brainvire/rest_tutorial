from django.shortcuts import render 
from rest_framework.decorators import api_view ,throttle_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .models import Carlist
from .serializers import CarSerializers
# from django.http import JsonResponse
# Create your views here.

@api_view()
def home(request):
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

@api_view(['GET','POST'])
def car_list(request):
    # data = {
    #     'cars':list(cars.values()),
    # } In django
    if request.method == 'GET': 
        cars = Carlist.objects.all()
        serializer = CarSerializers(cars,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view()
def car_detail_view(request,pk):
    car = Carlist.objects.get(pk=pk)
    Serializers = CarSerializers(car)
    return Response(Serializers.data)