from django.conf import settings
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Item, Order
from .services import create_checkout_session_from


class ItemView(DetailView):
    """Отображение товара"""
    model = Item
    template_name = 'checkout/item.html'

    @property
    def stripe_public_key(self):
        return settings.STRIPE_PUBLIC_KEY
    


class OrderView(ItemView):
    """Отображение заказа"""
    model = Order
    template_name = 'checkout/order.html'

    def get_queryset(self):
        return Order.objects.prefetch_related('items').all()
    

def item_session(request, pk):
    """оздание stripe сесии для товара"""
    item = get_object_or_404(Item, pk=pk)
    session = create_checkout_session_from([item])
    return JsonResponse({"_id": session.id})
 

def order_session(request, pk):
    """Создание stripe сесии для заказа"""
    order = get_object_or_404(Order.objects.prefetch_related('items'), pk=pk)
    data = {
        'items': order.items.all(),
        'tax': order.tax,
        'discount': order.discount,
    }
    session = create_checkout_session_from(**data) 
    return JsonResponse({"_id": session.id})


