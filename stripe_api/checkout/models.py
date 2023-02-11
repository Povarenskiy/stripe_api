from django.db import models
from django.urls import reverse


class Item(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    CURRENCY_CHOICES = [
        ("USD", "usd"),
        ("RUB", "rub"),
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def get_checkout_url(self):
        return reverse('buy', kwargs={'pk': self.id})

    def get_price(self):
        return int(self.price) / 100
    


class Discount(models.Model):
    """Модель скидки к заказу"""
    percent_off = models.FloatField()

    def get_attributes(self):
        return dict(percent_off = self.percent_off)
    

class Tax(models.Model):
    """Модель налогов к заказу"""
    display_name = models.CharField(max_length=50)
    inclusive = models.BooleanField()
    percentage = models.FloatField()
   
    def get_attributes(self):
        return dict(
            display_name = self.percentage,
            inclusive = self.inclusive,
            percentage = self.percentage,
        )


class Order(models.Model):
    """Модель заказа"""
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, null=True)
    tax = models.ForeignKey(Tax, on_delete=models.DO_NOTHING, null=True)

    def get_checkout_url(self):
        return reverse('buy_order', kwargs={'pk': self.id})





