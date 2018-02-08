from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    is_vegeterian = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    ingredient = models.ManyToManyField(Ingredient,db_column=name)


class PizzaVariation(models.Model):
    pizza = models.ForeignKey(Pizza,related_name='variations')
    price = models.IntegerField()
    _sizes = (('SM','Small'),('MD','Medium'),('BG','BIG'))
    size = models.CharField(max_length=2,choices=_sizes)

