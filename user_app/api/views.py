from django.shortcuts import render
from rest_framework.decorators import api_view ,authentication_classes , permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, BaseAuthentication

class Noauthentication(BaseAuthentication):
    def authenticate(self, request):
        return None

@api_view(['POST',])
@authentication_classes([TokenAuthentication])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# Create your views here.
# @api_view(['POST',])
# @authentication_classes([Noauthentication])
# @permission_classes([AllowAny])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'User Created'})
        
class Registration_view(APIView):
    # authentication_classes=[Noauthentication]
    permission_classes=[AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'User Created'},status=status.HTTP_201_CREATED)
        
        