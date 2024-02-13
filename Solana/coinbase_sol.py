import requests
# Modification for Coinbase to get both bid and ask prices for Solana
def get_solana_prices_coinbase():
    ask_url = 'https://api.coinbase.com/v2/prices/SOL-USD/sell'
    bid_url = 'https://api.coinbase.com/v2/prices/SOL-USD/buy'
    try:
        ask_response = requests.get(ask_url)
        ask_response.raise_for_status()  # This checks for HTTP request errors
        ask_data = ask_response.json()
        ask_price = ask_data['data']['amount']

        bid_response = requests.get(bid_url)
        bid_response.raise_for_status()  # This checks for HTTP request errors
        bid_data = bid_response.json()
        bid_price = bid_data['data']['amount']

        return float(bid_price), float(ask_price)
    except requests.RequestException as e:
        return f"Error: {e}", f"Error: {e}"
