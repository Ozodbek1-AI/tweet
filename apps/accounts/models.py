from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

class CreateUserModel(AbstractUser):
    full_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)

    def get_tokens(self):
        if not self.is_active:
            raise AuthenticationFailed("User is not active")

        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def __str__(self):
        return self.username


