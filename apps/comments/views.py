from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pages.models import Tweet
from apps.pages.serializer import CreateUserCommitSerializer


class CommentsListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        comments = Tweet.objects.all()
        serializer = CreateUserCommitSerializer(comments,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        try:
            comment = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response({"message": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        if user in comment.likes.all():
            comment.likes.remove(user)
            return Response({"message": "Unliked"}, status=status.HTTP_200_OK)
        else:
            comment.likes.add(user)
            return Response({"message": "Like"}, status=status.HTTP_200_OK)
