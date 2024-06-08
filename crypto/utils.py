import requests


def get_crypto_prices(symbols):
    url = 'https://api.binance.com/api/v3/ticker/price'
    prices = {}

    for symbol in symbols:
        params = {
            'symbol': symbol.upper()
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            prices[symbol] = float(data['price'])
        else:
            prices[symbol] = 'Error'

    return prices
