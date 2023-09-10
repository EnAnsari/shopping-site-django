from django.urls import path
from .views import *


urlpatterns = [
    path('product/list/', product_list, name='product-list'),
    path('product/detail/<int:pk>/', product_detail, name='product-detail'),
    path('category/<int:pk>/products', category_products, name='category-products'),
]