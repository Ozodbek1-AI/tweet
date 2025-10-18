from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.accounts.models import CreateUserModel


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUserModel
        fields = ['username','email','password','full_name','phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CreateUserModel.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = CreateUserModel
        fields = ['username','password']

    def validate(self, attrs):
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password')
        }
        user = authenticate(request=self.context['request'], **credentials)
        if user is None:
            raise serializers.ValidationError('Username or password is incorrect')
        else:
            attrs['user'] = user
            return attrs

