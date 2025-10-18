from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import CreateUserModel
from apps.accounts.serializer import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer


class UserRegisterAPIView(generics.GenericAPIView):
    queryset = CreateUserModel.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully","user": serializer.data},status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)



class UserProfileAPIView(generics.GenericAPIView):
    queryset = CreateUserModel.objects.all()
    serializer_class = UserProfileSerializer

    def get(self,request,pk):
        try:
            user = CreateUserModel.objects.get(pk=pk)
        except CreateUserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class UserLoginAPIView(generics.GenericAPIView):
    queryset = CreateUserModel.objects.all()
    serializer_class = UserLoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            tokens = serializer.validated_data['user'].get_tokens()
            return Response(data=tokens,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)