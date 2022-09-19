import stripe
import os

from dotenv import load_dotenv
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Items


load_dotenv()
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')


class ItemView(generics.RetrieveAPIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, **kwargs):

        item = Items.objects.filter(id=kwargs['pk']).first()
        return Response({'item': item}, template_name='checkout/buy_form.html')


class BuyView(APIView):
    def get(self, request, **kwargs):

        item = Items.objects.filter(id=kwargs['pk']).first()

        stripe.api_key = STRIPE_SECRET_KEY

        session = stripe.checkout.Session.create(
            line_items=[{
              'price_data': {
                'currency': 'usd',
                'product_data': {
                  'name': item.name,
                },
                'unit_amount': item.price,
              },
              'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',)

        return JsonResponse(
            {
                "session_id": session.id,
                "stripe_public_key": STRIPE_PUBLIC_KEY
            })
