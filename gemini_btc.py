# gemini_btc.py

import requests

# Modification for Gemini to get both bid and ask prices
def get_bitcoin_prices_gemini():
    url = 'https://api.gemini.com/v1/pubticker/btcusd'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        bid_price = data['bid']
        ask_price = data['ask']
        return float(bid_price), float(ask_price)
    except requests.RequestException as e:
        return f"Error: {e}", f"Error: {e}"
