from django.urls import path

from apps.pages.views import CreateUserCommentAPIView

app_name = 'pages'

urlpatterns = [
    path('user-create-comment/',CreateUserCommentAPIView.as_view())
]