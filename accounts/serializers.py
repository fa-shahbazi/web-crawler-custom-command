from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import Profile
from rest_framework import serializers
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'age',
            'bio',
            'phone_number',
        )
        extra_kwargs = {
            'user': {'required': False}
        }


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'profile']

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile)
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context['request']
        Token.objects.get_or_create(user=instance)
        if request.user == instance:
            data['token'] = instance.auth_token.key
        return data
