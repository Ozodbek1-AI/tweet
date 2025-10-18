from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pages.models import Tweet
from apps.pages.serializer import CreateUserCommitSerializer


class CreateUserCommentAPIView(APIView):
    serializer_class = CreateUserCommitSerializer
    permission_classes = [IsAuthenticated]


    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data={"message":"Comment is created","comment":serializer.data},status=201)
        return Response(data={"message":"Comment does not created","errors":serializer.errors},status=404)

class UserCommentListAPIView(APIView):
    serializer_class = CreateUserCommitSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request):

        user = request.user
        comments = Tweet.objects.filter(user=user)

        if not comments.exists():
            return Response({"message": "User has no comments"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

