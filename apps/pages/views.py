from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pages.serializer import CreateUserCommitSerializer


class CreateUserCommentAPIView(APIView):
    serializer_class = CreateUserCommitSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            print(request.data)
            print(serializer.data)
            return Response(data={"message":"Comment is created","comment":serializer.data},status=201)
        return Response(data={"message":"Comment does not created","errors":serializer.errors},status=404)