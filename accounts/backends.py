import jwt
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User


class UserAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user is None:
            return
        if user.check_password(password):
            return user


# class JWTAuthentication(authentication.BaseAuthentication):
#
#     def authenticate(self, request):
#         auth_data = authentication.get_authorization_header(request)
#
#         if not auth_data:
#             return None
#
#         prefix, token = auth_data.decode('utf-8').split(' ')
#         try:
#             payload = jwt.decode(token, settings.JWT_SECRET_KEY)
#             user = User.objects.get(username=payload['username'])
#             return (user, token)
#
#         except jwt.DecodeError as identifier:
#             raise exceptions.AuthenticationFailed('ur token is invalid')
#         except jwt.ExpiredSignatureError as identifier:
#             raise exceptions.AuthenticationFailed('ur token is expired')
#
#         return super().authenticate(request)

