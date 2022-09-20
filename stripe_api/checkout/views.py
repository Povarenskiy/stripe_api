import stripe
import os

from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
from django.http import JsonResponse
from django.db import models

from .models import Item, Order, Tax, Discount

# считывание переменных из environment
load_dotenv()
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')


class ItemView(View):

    def get(self, request, **kwargs):

        # ищем item по переданному первичному ключу
        item = Item.objects.filter(id=kwargs['pk']).first()

        # Данные для рендеринга html страницы
        context = {
            'id': item.id,
            'price': item.price,
            'name': item.name,
            'description': item.description,
            'type': 'Item',
            'currency': item.currency
        }

        return render(request, 'checkout/buy_form.html', context)


class OrderView(View):

    def get(self, request, **kwargs):

        # ищем выбранный order по переданному первичному ключу
        order = Order.objects.filter(id=kwargs['pk']).first()

        # Находим общую стоимость товаров
        order_info = order.items.aggregate(price=models.Sum('price'))

        # Данные для рендеринга html страницы
        context = {
            'id': order.id,
            'name': 'Order ' + str(order.id),
            'price': order_info.get('price'),
            'type': 'Order'
        }

        return render(request, 'checkout/buy_form.html', context)


class BuyView(View):

    def get(self, request, **kwargs):
        """
        Метод создает сессию stripe.checkout.Session для оплаты выбранного item или order
        Создание сессии для оплаты происходит по переданным с request параметрам price и name
        Если данные параметры не заданы, сессия создается для оплаты item с указанным pk
        Метод возвращает значение id созданной сессии и публикуемый ключ
        """
        if request.GET:
            name = request.GET['name']
            price = request.GET['price']
            purchase_type = request.GET['type']
            currency = request.GET['currency'] if purchase_type == 'Item' else 'usd'
        else:
            item = Item.objects.filter(id=kwargs['pk']).first()
            name = item.name
            price = item.price
            currency = item.currency
            purchase_type = 'Item'

        # настройка сессии Stripe
        stripe.api_key = STRIPE_SECRET_KEY

        # Создадим налог и скидку для указанной оплаты order если существуют
        tax_id = []
        discount_id = None
        if purchase_type == 'Order':
            tax_model = Tax.objects.filter(order=kwargs['pk']).first()
            if tax_model:
                tax_stripe = stripe.TaxRate.create(
                    display_name=tax_model.display_name,
                    inclusive=tax_model.inclusive,
                    percentage=tax_model.percentage,
                    )
                tax_id = [tax_stripe.id]

            discount_model = Discount.objects.filter(order=kwargs['pk']).first()
            if discount_model:
                discount = stripe.Coupon.create(percent_off=discount_model.percent_off, duration="once")
                discount_id = discount.id

        session = stripe.checkout.Session.create(
            line_items=[{
              'price_data': {
                'currency': currency,
                'product_data': {
                  'name': name,
                },
                'unit_amount': price,

              },
              'quantity': 1,
              'tax_rates': tax_id,

            }],
            mode='payment',
            discounts=[{'coupon': discount_id}],
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',)

        return JsonResponse(
            {
                "session_id": session.id,
                "stripe_public_key": STRIPE_PUBLIC_KEY
            })
