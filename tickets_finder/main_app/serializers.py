from rest_framework import serializers

from main_app.models import Route, Ticket, User


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        exclude = ()


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ()


class UserSerializer(serializers.ModelSerializer):
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
