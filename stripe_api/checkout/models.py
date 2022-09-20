from django.db import models


# Модель Item, включает основные характеристики товара
class Item(models.Model):
    USD = "USD"
    RUB = "RUB"

    STATUS_CHOICES = [
        (USD, "usd"),
        (RUB, "rub"),
    ]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    currency = models.CharField(verbose_name='currency for payment', max_length=3, choices=STATUS_CHOICES)

    objects = models.Manager()


# Модель Order, включает список товаров для покупки
class Order(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, verbose_name='Items in order')

    objects = models.Manager()


# Модель Discount, включает размер скидки и order к которому прикрепляется
class Discount(models.Model):
    percent_off = models.FloatField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True,
                                 verbose_name='Order id for discount')

    objects = models.Manager()


# Модель Discount, включает основные характеристики налога и order к которому прикрепляется
class Tax(models.Model):
    display_name = models.CharField(max_length=50)
    inclusive = models.BooleanField()
    percentage = models.FloatField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True,
                                 verbose_name='Order id for tax')

    objects = models.Manager()






