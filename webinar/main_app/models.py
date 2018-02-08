from django.db import models



from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=450, unique=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers')
    in_stock = models.IntegerField()
    categorys = models.ForeignKey(Category, to_field='name', related_name='category',)

    def __str__(self):
        return self.name


class ExampleBasket(models.Model):
    owner = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, to_field='name')
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.product.name


class Basket(models.Model):
    user = models.ForeignKey('auth.User',related_name='user', on_delete=models.CASCADE)
    elements = models.ForeignKey(ExampleBasket,related_name='elements')
    status = models.BooleanField(default=True)
