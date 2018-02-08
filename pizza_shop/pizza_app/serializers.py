from rest_framework import serializers
from pizza_app.models import Ingredient,Pizza,PizzaVariation

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ()

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza,
        exclude = ()
class PizzaSerializerVariation(serializers.ModelSerializer):
    class Meta:
        model = PizzaVariation
        exclude = ()