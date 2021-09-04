from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [

    path('product-detail/<int:id>/', views.product_detail, name='product-detail'),
    path('category-list/', views.category_list, name='category-list'),
    path('category_product_list/<int:cat_id>/', views.category_product_list, name='category-product-list'),

]