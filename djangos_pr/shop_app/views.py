from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


from .serializers import (
    UserSerializer,
    ProductSerializer,
    CategorySerializer,
    ExampleSerializer
)
from .models import User, Product, Category, ExampleBasket
# Create your views here.


class UserView(GenericViewSet,
               mixins.ListModelMixin,  # TODO: remove after tests are completed
               mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProductView(GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,):
    permission_classes = (IsAdminUser, )
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ExampleView(GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = ExampleBasket.objects.all()
    serializer_class = ExampleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)





class CategoryView(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    permission_classes = (IsAdminUser, )
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

