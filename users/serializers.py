from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError('User already exists')
        return username


class UserAuthorizeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
