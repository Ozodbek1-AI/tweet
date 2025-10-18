from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.accounts.models import CreateUserModel


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUserModel
        fields = ['id','username','email','password','first_name','last_name','phone']
        read_only_fields = ['id']
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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUserModel
        fields = ['id','username','first_name','last_name','email','phone']

