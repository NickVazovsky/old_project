from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated


from .serializers import (
    ProductSerializers,
    BasketSerializers,
    ProductCardSerializers,
    OrderSerializers,
    ProfileOrderSerializer,
    ProfileSerializer
)
from .models import User, Product, Basket, ProductCard, Order


class ProductView(GenericViewSet,
                  mixins.ListModelMixin):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


class ProductCardView(GenericViewSet,
                      mixins.ListModelMixin):
    serializer_class = ProductCardSerializers
    queryset = ProductCard.objects.all()


class BasketView(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin):
    serializer_class = BasketSerializers
    queryset = Basket.objects.all()


class OrderView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializers

    def get_queryset(self):
        username = self.request.user
        if username is not None:
            queryset = Order.objects.filter(user_id=username)
            return queryset
        else:
            queryset = Order.objects.all()
            return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileOrderView(GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin):
    serializer_class = ProfileOrderSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        username = self.request.user
        if username is not None:
            queryset = Order.objects.filter(user_id=username)
            return queryset
        else:
            queryset = Order.objects.all()
            return queryset


class ProfileInformView(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        username = self.request.user
        if username is not None:
            queryset = User.objects.filter(username=username)
            return queryset
        else:
            queryset = User.objects.all()
            return queryset
