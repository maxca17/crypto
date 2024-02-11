import requests

def get_bitcoin_prices_huobi():
    url = 'https://api.huobi.pro/market/depth'
    params = {'symbol': 'btcusdt', 'type': 'step0'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        bid_price = data['tick']['bids'][0][0]  # First bid price
        ask_price = data['tick']['asks'][0][0]  # First ask price
        return bid_price, ask_price
    except requests.RequestException as e:
        return f"Error: {e}"
