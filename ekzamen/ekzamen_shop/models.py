from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=450, unique=True)
    category = models.ForeignKey(Category, to_field='name', related_name='category', )

    def __str__(self):
        return self.name


class ProductCard(models.Model):
    product = models.ForeignKey(Product, to_field='name', )
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.CharField(max_length=255, )
    product = models.ForeignKey(ProductCard, to_field='title', related_name='element')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.product.title


class Order(models.Model):
    user = models.ForeignKey('auth.User', related_name='User')
    address = models.CharField(max_length=255)
    date_delivery = models.DateTimeField()
    product = models.ForeignKey(Basket)
