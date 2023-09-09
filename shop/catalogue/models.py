from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)


class ProductAttribute(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)