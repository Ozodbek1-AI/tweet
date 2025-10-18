from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import CreateUserModel
from apps.accounts.serializer import UserRegisterSerializer, UserLoginSerializer



class UserRegisterAPIView(generics.CreateAPIView):
    queryset = CreateUserModel.objects.all()
    serializer_class = UserRegisterSerializer

    @swagger_auto_schema(
        tags=['Accounts']
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # def get(self,request):
    #     pass

class UserLoginAPIView(APIView):
    queryset = CreateUserModel.objects.all()
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(
        tags=['Accounts'],
        request_body=UserLoginSerializer,
        responses={200: UserLoginSerializer}
    )
    def post(self,request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            tokens = serializer.validated_data['user'].get_tokens()
            return Response(data=tokens,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
