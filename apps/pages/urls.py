from django.urls import path

from apps.pages.views import CreateUserCommentAPIView, UserCommentListAPIView, UserCommentDetailAPIView, \
    UserCommentUpdateAPIView

app_name = 'pages'

urlpatterns = [
    path('user-create-comment/',CreateUserCommentAPIView.as_view()),
    path('user-list-comment/',UserCommentListAPIView.as_view()),
    path('user-detail-comment/<int:pk>/',UserCommentDetailAPIView.as_view()),
    path('user-update-comment/<int:pk>/',UserCommentUpdateAPIView.as_view()),

]