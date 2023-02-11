from django.urls import path
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='item'),
    path('order/<int:pk>/', OrderView.as_view(), name='order'),
    path('buy/<int:pk>/', item_session, name='buy'),
    path('buy/order/<int:pk>/', order_session, name='buy_order')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
