from rest_framework import serializers
from .models import User, Category, Product, Basket, ProductCard, Order


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class ProductCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductCard
        exclude = ()


class BasketSerializers(serializers.ModelSerializer):

    price = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=6)

    class Meta:
        model = Basket
        exclude = ()
        fields = ('user', 'product', 'price', 'quantity', )

    def create(self, validated_data):
        user = validated_data['user']
        product = validated_data['product']
        quantity = validated_data['quantity']
        increase = ProductCard.objects.get(title=product)
        basket = Basket(
            user=user,
            product=product,
            quantity=quantity,
            price=increase.price*quantity,

        )
        basket.save()
        return basket


class OrderSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        exclude = ()
        fields = ('user', 'address', 'date_delivery', 'product')

    def create(self, validated_data):
        user = validated_data['user']
        address = validated_data['address']
        date_delivery = validated_data['date_delivery']
        product = validated_data['product']
        order = Order(
            user=user,
            address=address,
            date_delivery=date_delivery,
            product=product
        )
        order.save()
        return order


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ()


class ProfileOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ()
