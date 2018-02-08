from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=450)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()
    in_stock = models.IntegerField()
    categorys = models.ForeignKey(Category,related_name='category')

    def __str__(self):
        return self.name

class ExampleBasket(models.Model):
    owner = models.ForeignKey('auth.User', related_name='users',on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product)
    price = models.DecimalField(decimal_places=2, max_digits=6)




class Basket(models.Model):
    user = models.OneToOneField(User,related_name='user')
    elements = models.ManyToManyField(ExampleBasket,related_name='elements')



