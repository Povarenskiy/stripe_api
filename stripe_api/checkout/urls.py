from django.urls import path, include
from .views import ItemView, OrderView, BuyView

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view()),
    path('buy/<int:pk>/', BuyView.as_view()),
    path('order/<int:pk>/', OrderView.as_view())

]
