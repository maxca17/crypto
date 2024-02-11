import requests

def get_bitcoin_prices_crypto_com():
    url = 'https://api.crypto.com/v1/ticker?instrument_name=BTC_USD'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Assuming 'result' contains the ticker info and 'data' contains the bid and ask
        bid_price = data['result']['data']['b']
        ask_price = data['result']['data']['a']
        return float(bid_price), float(ask_price)
    except requests.RequestException as e:
        return f"Error: {e}", f"Error: {e}"
