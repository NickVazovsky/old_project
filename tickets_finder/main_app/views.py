from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView
from main_app.serializers import (
    RouteSerializer,
    TicketSerializer,
    UserSerializer,
)
from main_app.models import Route, Ticket, User


class UserView(GenericViewSet,
               mixins.ListModelMixin,  # TODO: remove after tests are completed
               mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RouteView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class TicketView(GenericViewSet,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

