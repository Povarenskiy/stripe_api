from django.urls import path, include
from . import views

urlpatterns = [
    path('item/<int:pk>/', views.ItemView.as_view()),
    path('buy/<int:pk>/', views.BuyView.as_view())

]
