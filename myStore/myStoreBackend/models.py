import uuid

from django.db import models


# Create your models here.
class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    phone = models.CharField(max_length=13)
    email = models.EmailField(blank=True)
    moneyGiven = models.FloatField(default=0)
    moneyOwed = models.FloatField(default=0)

    class Meta:
        db_table = "Client"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    price = models.FloatField()

    class Meta:
        db_table = "Product"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    paid = models.BooleanField()

    class Meta:
        db_table = "Order"
