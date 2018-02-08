from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


from .serializers import (
    UserSerializer,
    ExampleSerializer,
    ProductSerializer,
    CategorySerializer,
    BasketSerializer,
)
from .models import User, Product, Category, ExampleBasket, Basket
# Create your views here.


class CategoryView(GenericViewSet,
                   mixins.ListModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductView(GenericViewSet,
                  mixins.ListModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BasketView(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = BasketSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
       # queryset = Basket.objects.all()
        username = self.request.user
        if username is not None:
            queryset = Basket.objects.filter(user_id=username)
            return queryset
        else:
            queryset = Basket.objects.all()
            return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserView(GenericViewSet,
               mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ExampleView(GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    permission_classes = (IsAuthenticated, )
    queryset = ExampleBasket.objects.all()
    serializer_class = ExampleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
