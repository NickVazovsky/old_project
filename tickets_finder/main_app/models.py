import uuid

from django.db import models
from django.contrib.auth.models import User


class Route(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    depature_from = models.CharField(max_length=150)
    depature_at = models.DateTimeField()

    destination = models.CharField(max_length=150)
    number_of_seats = models.IntegerField()

    price = models.DecimalField(max_digits=8, decimal_places=2)


class Ticket(models.Model):
    passenger = models.ForeignKey(User, related_name='tickets')
    route = models.ForeignKey(Route, related_name='tickets')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
