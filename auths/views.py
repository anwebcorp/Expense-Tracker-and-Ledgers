from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class LoginAPIView(APIView):
  def post(self , request):
    serializer = LoginSerializers(data = request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    user = authenticate(username=username , password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'access' : str(refresh.access_token),
        'refresh' : str(refresh)
      }, status=status.HTTP_200_OK)

    return Response({'Error' : serializer.errors} , status=status.HTTP_400_BAD_REQUEST)  