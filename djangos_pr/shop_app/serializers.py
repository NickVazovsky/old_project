from rest_framework import serializers
from .models import User, Basket, ExampleBasket, Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        exclude = ()


class ExampleSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=6)
    class Meta:
        model = ExampleBasket
        exclude = ()
        field = ('quantity', 'product','owner','price')

    def create(self, validated_data):
        owner=validated_data['owner']
        product = validated_data['product']
        cost=Product.objects.get(name=product)
        quantity=validated_data['quantity']
        #F('price') * F('stock'), output_field = DecimalField()
        user = ExampleBasket(
            quantity=quantity,
            product=product,
            price=cost.price*quantity,
            owner=owner

        )
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    example = serializers.PrimaryKeyRelatedField(many=True, queryset=ExampleBasket.objects.all())
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
            'user_permissions',
        )

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
