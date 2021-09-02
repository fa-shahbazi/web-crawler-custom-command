from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'crawler/product_list.html', {'categories':categories})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'crawler/product_list.html', {'products':products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'crawler/product_detail.html', context)
