from django.shortcuts import render 
from rest_framework.decorators import api_view ,throttle_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .models import Carlist , showRoomList
from .serializers import CarSerializers , showRoomSerializer
from django.http import JsonResponse
from rest_framework.exceptions import bad_request 
from rest_framework.views import APIView

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
        try: 
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            # else:
            #     return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk):
    
    if request.method == 'GET': 
        try: 
            car = Carlist.objects.get(pk=pk)
        except Exception as e:
            return Response({"Error":e.args},status=404)
        Serializers = CarSerializers(car)
        return Response(Serializers.data)
    
    
   
    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        Serializers=CarSerializers(car,data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data)
        else:
            return Response(Serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        car =Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class showRoom_view(APIView):

    def get(self,request):
        showroom = showRoomList.objects.all()
        serializer = showRoomSerializer(showroom,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = showRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class showRoom_details(APIView):
    def get(self,request,pk):
        try:
            showroom = showRoomList.objects.get(pk=pk)
        except showRoomList.DoesNotExist:
            return Response({'Error':'showroom not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = showRoomSerializer(showroom)
        return Response(serializer.data)
    
    def put(self,request,pk):
        showroom =showRoomList.objects.get(pk=pk)
        serializer = showRoomSerializer(showroom,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request,pk):
        showroom = showRoomList.objects.get(pk = pk)
        showroom.delete()
        return Response({'Error':'Not found'},status=status.HTTP_204_NO_CONTENT)
    

        
    

# @api_view()
# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)

#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status_code'] = response.status_code

#     return response