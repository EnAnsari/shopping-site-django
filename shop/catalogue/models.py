from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductTypes'

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3

    ATTRIBUTE_TYPES_FIELDS = [
        (INTEGER, 'Integer'),
        (STRING, 'String'),
        (FLOAT, 'Float'),
    ]

    title = models.CharField(max_length=32, blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPES_FIELDS)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='Prodects')
    upc = models.PositiveBigIntegerField(unique=True)
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attribute_values')
    value = models.CharField(max_length=48)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name='values')

    def __str__(self):
        return f'{self.product}({self.attribute}): {self.value}'