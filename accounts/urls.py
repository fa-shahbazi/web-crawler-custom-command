from django.urls import path
from . import views

app_name= 'accounts'
urlpatterns=[
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name="user_register"),
    path('logout/', views.user_logout, name="user_logout"),
    path('profile/<int:user_id>/', views.user_profile, name="user_profile"),
]