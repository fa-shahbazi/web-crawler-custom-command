from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category)
    return render(request, 'crawler/category_product_list.html', {'data':data})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'crawler/category_list.html', {'categories':categories})



def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'crawler/product_detail.html', context)
