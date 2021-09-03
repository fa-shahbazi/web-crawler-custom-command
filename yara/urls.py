
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crawler.urls', namespace='crawler')),
    path('account/', include('users.urls', namespace='users')),

]
