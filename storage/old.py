import time
from BTC.coinbase_btc import get_bitcoin_prices_coinbase
from BTC.kraken_btc import get_bitcoin_prices_kraken
from BTC.gemini_btc import get_bitcoin_prices_gemini

start_time = time.time()

def main():
    # Fetch the bid and ask prices for each exchange
    coinbase_bid_price, coinbase_ask_price = get_bitcoin_prices_coinbase()
    kraken_bid_price, kraken_ask_price = get_bitcoin_prices_kraken()
    gemini_bid_price, gemini_ask_price = get_bitcoin_prices_gemini()

    # Print the fetched prices
    print_prices('Coinbase', coinbase_bid_price, coinbase_ask_price)
    print_prices('Kraken', kraken_bid_price, kraken_ask_price)
    print_prices('Gemini', gemini_bid_price, gemini_ask_price)

    # Identify and print arbitrage opportunities
    print_arbitrage_opportunities('Coinbase', 'Kraken', coinbase_bid_price, coinbase_ask_price, kraken_bid_price, kraken_ask_price)
    print_arbitrage_opportunities('Coinbase', 'Gemini', coinbase_bid_price, coinbase_ask_price, gemini_bid_price, gemini_ask_price)
    print_arbitrage_opportunities('Kraken', 'Gemini', kraken_bid_price, kraken_ask_price, gemini_bid_price, gemini_ask_price)

    # Print deltas between exchanges
    print("\nPrice Deltas Between Exchanges:")
    print_deltas('Coinbase', 'Kraken', coinbase_bid_price, kraken_ask_price)
    print_deltas('Coinbase', 'Gemini', coinbase_bid_price, gemini_ask_price)
    print_deltas('Kraken', 'Gemini', kraken_bid_price, gemini_ask_price)

def print_prices(exchange, bid_price, ask_price):
    print(f"The current bid price of Bitcoin on {exchange} is {bid_price} USD")
    print(f"The current ask price of Bitcoin on {exchange} is {ask_price} USD")

def print_arbitrage_opportunities(exchange1, exchange2, bid1, ask1, bid2, ask2):
    if bid1 > ask2:
        print(f"Arbitrage opportunity: Buy on {exchange2} at {ask2} USD and sell on {exchange1} at {bid1} USD.")
    if bid2 > ask1:
        print(f"Arbitrage opportunity: Buy on {exchange1} at {ask1} USD and sell on {exchange2} at {bid2} USD.")

def print_deltas(exchange1, exchange2, bid_price, ask_price):
    # Calculate and print the delta between the bid price of one exchange and the ask price of another
    delta = round(abs(bid_price - ask_price), 2)
    print(f"Delta between {exchange1} bid and {exchange2} ask: {delta} USD")

if __name__ == "__main__":
    main()

# Record end time
end_time = time.time()
# Calculate total runtime
runtime = round((end_time - start_time), 2)
print(f"Script runtime: {runtime} seconds")
