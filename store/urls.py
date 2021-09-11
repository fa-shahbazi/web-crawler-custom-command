from django.urls import path
from . import views
from .api_views import CategoryListApiView, CategoryDetailApiView, ProductDetailApiView, ProductListApiView

app_name = 'store'
urlpatterns = [

    path('product-detail/<int:id>/', views.product_detail, name='product-detail'),
    path('category-list/', views.category_list, name='category-list'),
    path('category_product_list/<int:cat_id>/', views.category_product_list, name='category-product-list'),


    path('api/category-list/', CategoryListApiView.as_view(), name='category_list'),
    path('api/category-detail/<int:pk>/', CategoryDetailApiView.as_view(), name='category_detail'),
    path('api/product-detail/<int:pk>/', ProductDetailApiView.as_view(), name='product_detail'),
    path('api/product-list/', ProductListApiView.as_view(), name='product_list'),

]
