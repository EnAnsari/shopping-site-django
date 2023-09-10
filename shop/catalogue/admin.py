from django.contrib import admin
from catalogue.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'upc', 'is_active', 'product_type', 'category', 'brand')
    list_filter = ('is_active',)
    search_fields = ('upc', 'title', 'category__name', 'brand__name')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)