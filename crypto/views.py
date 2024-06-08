# crypto/views.py
from django.shortcuts import render
from .utils import get_crypto_prices

def crypto_prices_view(request):
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'FETUSDT', 'XRPUSDT']  # List of Binance symbols for cryptocurrencies
    prices = get_crypto_prices(symbols)
    context = {
        'prices': prices
    }
    return render(request, 'prices.html', context)
