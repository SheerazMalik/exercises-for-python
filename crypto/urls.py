# crypto/urls.py
from django.urls import path
from .views import crypto_prices_view

urlpatterns = [
    path('', crypto_prices_view, name='crypto_price'),
]