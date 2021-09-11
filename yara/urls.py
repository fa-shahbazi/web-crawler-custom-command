
from django.contrib import admin
from django.urls import path, include
# from.api_urls import router
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)

]
