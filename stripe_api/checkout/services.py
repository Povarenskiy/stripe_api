import stripe
from django.conf import settings


def create_checkout_session_from(items, tax=None, discount=None):    
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if tax:
        tax_stripe = stripe.TaxRate.create(**tax.get_attributes())

    if discount:
        coupons = stripe.Coupon.create(**discount.get_attributes())

    session_parameters = {
        'line_items' : [{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
            'tax_rates': [tax_stripe.id] if tax else None,
        } for item in items],
        'discounts': [{'coupon': coupons.id}] if discount else None,
        'mode':'payment',
        'success_url':'http://localhost:4242/success',
        'cancel_url':'http://localhost:4242/cancel',
    }
    
    session = stripe.checkout.Session.create(**session_parameters)
    return session