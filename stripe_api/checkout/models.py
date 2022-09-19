from django.db import models
from django_mysql.models import ListCharField


class Items(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=20)

    objects = models.Manager()


class Orders(models.Model):

    list_items = models.CharField(max_length=50)