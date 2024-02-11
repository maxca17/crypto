import time
import requests
from coinbase_btc import get_bitcoin_prices_coinbase
from kraken_btc import get_bitcoin_prices_kraken
from gemini_btc import get_bitcoin_prices_gemini

start_time = time.time()

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

def main():
    # Fetch the bid and ask prices for each exchange
    coinbase_bid_price, coinbase_ask_price = get_bitcoin_prices_coinbase()
    kraken_bid_price, kraken_ask_price = get_bitcoin_prices_kraken()
    gemini_bid_price, gemini_ask_price = get_bitcoin_prices_gemini()
    huobi_bid_price, huobi_ask_price = get_bitcoin_prices_huobi()

    # Print the fetched prices
    print_prices('Coinbase', coinbase_bid_price, coinbase_ask_price)
    print_prices('Kraken', kraken_bid_price, kraken_ask_price)
    print_prices('Gemini', gemini_bid_price, gemini_ask_price)
    print_prices('Huobi', huobi_bid_price, huobi_ask_price)

    # Identify and print arbitrage opportunities
    exchanges = [
        ('Coinbase', coinbase_bid_price, coinbase_ask_price),
        ('Kraken', kraken_bid_price, kraken_ask_price),
        ('Gemini', gemini_bid_price, gemini_ask_price),
        ('Huobi', huobi_bid_price, huobi_ask_price)
    ]
    for i, (exchange1, bid1, ask1) in enumerate(exchanges):
        for exchange2, bid2, ask2 in exchanges[i+1:]:
            print_arbitrage_opportunities(exchange1, exchange2, bid1, ask1, bid2, ask2)

    # Print deltas between exchanges
    print("\nPrice Deltas Between Exchanges:")
    for i, (exchange1, bid1, _) in enumerate(exchanges):
        for exchange2, _, ask2 in exchanges[i+1:]:
            print_deltas(exchange1, exchange2, bid1, ask2)

def print_prices(exchange, bid_price, ask_price):
    print(f"The current bid price of Bitcoin on {exchange} is {bid_price} USD")
    print(f"The current ask price of Bitcoin on {exchange} is {ask_price} USD")

def print_arbitrage_opportunities(exchange1, exchange2, bid1, ask1, bid2, ask2):
    if bid1 > ask2:
        print(f"Arbitrage opportunity: Buy on {exchange2} at {ask2} USD and sell on {exchange1} at {bid1} USD.")
    if bid2 > ask1:
        print(f"Arbitrage opportunity: Buy on {exchange1} at {ask1} USD and sell on {exchange2} at {bid2} USD.")

def print_deltas(exchange1, exchange2, bid_price, ask_price):
    delta = round(abs(bid_price - ask_price), 2)
    print(f"Delta between {exchange1} bid and {exchange2} ask: {delta} USD")

if __name__ == "__main__":
    main()

# Record end time
end_time = time.time()
# Calculate total runtime
runtime = round((end_time - start_time), 2)
print(f"Script runtime: {runtime} seconds")
