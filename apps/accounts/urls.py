from django.urls import path

from apps.accounts.views import UserRegisterAPIView, UserLoginAPIView, UserProfileAPIView

app_name = 'accounts'

urlpatterns = [
    path('register-user/',UserRegisterAPIView.as_view()),
    path('login-user/',UserLoginAPIView.as_view()),
    path('user-profile/<int:pk>/',UserProfileAPIView.as_view()),
]