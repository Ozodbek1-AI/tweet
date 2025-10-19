from django.urls import path
from .views import CommentsListAPIView, CommentLikeAPIView

app_name = 'comments'

urlpatterns = [
    path('all-comments/', CommentsListAPIView.as_view(), name='all-comments'),
    path('like/<int:pk>/', CommentLikeAPIView.as_view(), name='comment-like'),
]