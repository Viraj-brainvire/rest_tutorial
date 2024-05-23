from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view ,throttle_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.throttling import UserRateThrottle
from rest_framework import status , generics , mixins , viewsets
from .models import Carlist , showRoomList,Review
from .serializers import CarSerializers , showRoomSerializer , ReviewSerializer
from django.http import JsonResponse
from rest_framework.exceptions import bad_request ,ValidationError
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser , AllowAny ,DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter

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

# @api_view(['GET','POST'])
# def car_list(request):
#     # data = {
#     #     'cars':list(cars.values()),
#     # } In django
       
#     if request.method == 'GET': 
#         cars = Carlist.objects.all()
#         serializer = CarSerializers(cars,many=True)
#         return Response(serializer.data)
       
#     if request.method == 'POST':
#         serializer = CarSerializers(data = request.data)
#         try: 
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             # else:
#             #     return Response(status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({'message':'Error'},status=status.HTTP_400_BAD_REQUEST)
        
class car_list(generics.ListCreateAPIView):
    queryset = Carlist.objects.all()
    serializer_class=CarSerializers
    filter_backends = [SearchFilter] 
    search_fields=['^name']
    # def get_queryset(self):
    #     user=self.request.user
    #     return Carlist.objects.filter(passby=user)


@api_view(['GET','PUT','DELETE','PATCH'])
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
        
    if request.method == 'PATCH':
        car = Carlist.objects.get(pk=pk)
        Serializers=CarSerializers(car,data=request.data,partial=True)
        if Serializers.is_valid(raise_exception=True):
            Serializers.save()
            return Response(Serializers.data)
        # else:
        #     return Response(Serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        car =Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ShowRoom_viewset(viewsets.ModelViewSet):
    queryset = showRoomList.objects.all()
    serializer_class = showRoomSerializer
    
    # Creating Viewset
# class ShowRoom_viewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = showRoomList.objects.all()
#         serializer = showRoomSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = showRoomList.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = showRoomSerializer(user)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serialzer = showRoomSerializer(data=request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data)
#         else:
#             return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def update(self,request,pk):
#         showroom =showRoomList.objects.get(pk=pk)
#         serializer = showRoomSerializer(showroom,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class ShowRoom_view(APIView):
    # authentication_classes=[BasicAuthentication]
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]


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
        
class ShowRoom_details(APIView):
    def get(self,request:Request,pk):
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
    
    # Mixins
# class ReviewList_detail(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[DjangoModelPermissions]
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args,**kwargs)
    
    # Generic Api
class ReviewList_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args,**kwargs)

class ReviewList(generics.ListAPIView):
    serializer_class=ReviewSerializer
    def get_queryset(self):
        pk =self.kwargs['pk']
        return Review.objects.filter(car=pk)

class Reviewlist(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class Reviewcreate(generics.CreateAPIView):

    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self,serialzer):
        pk=self.kwargs['pk']
        cars = Carlist.objects.get(pk=pk)
        useredit=self.request.user
        Review_queryset = Review.objects.filter(car=cars,apiuser=useredit)
        if Review_queryset.exists():
            raise ValidationError("You have already reviewd this car ")

    serializer_class = ReviewSerializer
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        cars = Carlist.objects.get(pk = pk)
        serializer.save(car=cars)
        
    

# @api_view()
# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)

#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status_code'] = response.status_code

#     return response