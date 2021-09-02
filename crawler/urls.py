from django.urls import path
from . import views

app_name = 'crawler'
urlpatterns = [
    path('product-list',views.product_list, name='product_list'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail')
]