from django.urls import path

from apps.pages.views import CreateUserCommentAPIView, UserCommentListAPIView

app_name = 'pages'

urlpatterns = [
    path('user-create-comment/',CreateUserCommentAPIView.as_view()),
    path('user-detail-comment/',UserCommentListAPIView.as_view()),
]