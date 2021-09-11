from django.urls import path
from . import views
from .api_views import RegisterView, UserListCreateAPIView

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name="user_register"),
    path('logout/', views.user_logout, name="user_logout"),
    path('register-view/', RegisterView.as_view()),
    path('login-view/', UserListCreateAPIView.as_view()),
    path('confirm-register/', views.confirm_registration, name='confirm'),
]
