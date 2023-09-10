from django.contrib import admin
from django.contrib.admin import register
from django.http.request import HttpRequest
from catalogue.models import *

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'upc', 'is_active', 'product_type', 'category', 'brand')
    list_filter = ('is_active',)
    search_fields = ('upc', 'title', 'category__name', 'brand__name')
    list_editable = ('is_active',)
    actions = ('active_all',)

    def active_all(self, request, queryset):
        pass

    # def has_delete_permission(self, request, obj=None):
    #     return True


# class ProductAttributeInline(admin.StackedInline):
class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0

@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_type', 'attribute_type')


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (ProductAttributeInline,)

admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(ProductAttribute)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductType)