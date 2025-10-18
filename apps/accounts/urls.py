from django.urls import path

from apps.accounts.views import UserRegisterAPIView, UserLoginAPIView

app_name = 'accounts'

urlpatterns = [
    path('register-user/',UserRegisterAPIView.as_view(),name='register-user'),
    path('login-user/',UserLoginAPIView.as_view(),name='login-user'),
]