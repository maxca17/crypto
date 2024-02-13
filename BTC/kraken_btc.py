import requests
# Modification for Kraken to get both bid and ask prices
def get_bitcoin_prices_kraken():
    url = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        ask_array = data['result']['XXBTZUSD']['a']
        bid_array = data['result']['XXBTZUSD']['b']
        ask_price = ask_array[0]
        bid_price = bid_array[0]
        return float(bid_price), float(ask_price)
    except requests.RequestException as e:
        return f"Error: {e}", f"Error: {e}"
