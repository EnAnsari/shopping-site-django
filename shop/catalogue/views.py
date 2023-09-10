from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def product_list(request):
    products = Product.objects.select_related('category').all()
    context = "<br>".join([f'{product.title}, {product.upc} - category: {product.category.name}' for product in products])
    return HttpResponse(context)

def product_detail(request, pk):
    try:
        product = Product.objects.filter(is_active=True).get(Q(pk=pk) | Q(upc=pk))
    except Product.DoesNotExist:
        return HttpResponse('This product doesn\'t exist!')
    
    # queryset = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    # if queryset.exists():
    #     product = queryset.first()
    #     return HttpResponse(f'title: {product.title}')
    # else:
    #     return HttpResponse('This product doesn\'t exist!')

    return HttpResponse(f'title: {product.title}')


def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse('This category doesn\'t exist!')
    
    products = category.products.all()
    context = '<br>'.join(f'{product.title}, {product.upc}' for product in products)
    return HttpResponse(context)