from rest_framework import serializers

from apps.pages.models import Tweet


class CreateUserCommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['user','id','content','likes','created_at']
        read_only_fields = ['user','id','created_at','updated_at']

