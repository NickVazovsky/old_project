from django.shortcuts import render
from rest_framework.viewsets import  GenericViewSet, mixins
from pizza_app.models import Ingredient, Pizza
from pizza_app.serializers import IngredientSerializer,PizzaSerializer,PizzaSerializerVariation
# Create your views here.

class IngredientView(GenericViewSet,mixins.ListModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.CreateModelMixin):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

class PizzaView(GenericViewSet,mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.CreateModelMixin):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

class PizzaVariable(GenericViewSet,mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.CreateModelMixin):
    serializer_class = PizzaSerializerVariation
    queryset = Pizza.objects.all()




