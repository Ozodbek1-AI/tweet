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

# Hamma commentni get qilish
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


#1-ta commentni get qilish
class UserCommentDetailAPIView(APIView):
    serializer_class = CreateUserCommitSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):

        try:
            comment = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response({"message":"Comment not found"},status=status.HTTP_404_NOT_FOUND)

        serializer = CreateUserCommitSerializer(comment)
        return Response(serializer.data)

class UserCommentUpdateAPIView(APIView):
    serializer_class = CreateUserCommitSerializer
    permission_classes = [IsAuthenticated]

    def put(self,request,pk):
        user = request.user

        try:
            comment = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response({"message":"Comment not found"},status=status.HTTP_404_NOT_FOUND)

        if comment.user != user:
            return Response({"message": "This comment is not your comment"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CreateUserCommitSerializer(comment,data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":"Comment updated","comment":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


    def patch(self,request,pk):
        user = request.user

        try:
            comment = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response({"message":"Comment not found"},status=status.HTTP_404_NOT_FOUND)

        if comment.user != user:
            return Response({"message": "This comment is not your comment"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CreateUserCommitSerializer(comment,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":"Comment updated","comment":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


    def delete(self,request, pk):
        user = request.user

        try:
            comment = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response({"message": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        if comment.user != user:
            return Response({"message": "This comment is not your comment"}, status=status.HTTP_400_BAD_REQUEST)

        comment.delete()
        return Response({"message":"Comment deleted"},status=status.HTTP_200_OK)

