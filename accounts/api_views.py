from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.conf import settings
from django.contrib import auth
import jwt
from django.contrib.auth import get_user_model

from rest_framework import generics
from .serializers import UserSerializer


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


User = get_user_model()


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = TokenAuthentication,

