import time
import requests
from BTC.coinbase_btc import get_bitcoin_prices_coinbase
from BTC.kraken_btc import get_bitcoin_prices_kraken
from BTC.gemini_btc import get_bitcoin_prices_gemini
from BTC.huobi_btc import get_bitcoin_prices_huobi
# Assuming the functions for Coinbase, Kraken, Gemini, and a similarly defined function for Huobi are available

# Initial balances
balances = {
    'Coinbase': {'USD': 10000, 'BTC': 1},
    'Kraken': {'USD': 10000, 'BTC': 1},
    'Gemini': {'USD': 10000, 'BTC': 1},
    'Huobi': {'USD': 10000, 'BTC': 1}
}

def simulate_trade(exchange_buy, exchange_sell, buy_price, sell_price, amount_btc=0.01):
    cost = buy_price * amount_btc
    proceeds = sell_price * amount_btc
    profit = proceeds - cost
    
    if profit > 20 and balances[exchange_buy]['USD'] >= cost and balances[exchange_sell]['BTC'] >= amount_btc:
        balances[exchange_buy]['USD'] -= cost
        balances[exchange_buy]['BTC'] += amount_btc
        balances[exchange_sell]['USD'] += proceeds
        balances[exchange_sell]['BTC'] -= amount_btc
        print(f"Trade executed: Bought {amount_btc} BTC on {exchange_buy} at {buy_price} and sold on {exchange_sell} at {sell_price}. Profit: ${profit:.2f}")
        print_balances()
    else:
        if profit <= 20:
            print("Opportunity found but profit below $20 threshold.")
        else:
            print("Insufficient funds to execute trade.")

def print_balances():
    for exchange, balance in balances.items():
        print(f"{exchange}: USD={balance['USD']:.2f}, BTC={balance['BTC']:.4f}")

def print_prices(exchange, bid_price, ask_price):
    print(f"{exchange} - Bid: {bid_price}, Ask: {ask_price}")

def main():
    while True:
        start_time = time.time()

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

        # Example simulation of arbitrage (expanded logic to include $20 profit check)
        exchanges = [('Coinbase', coinbase_bid_price, coinbase_ask_price),
                     ('Kraken', kraken_bid_price, kraken_ask_price),
                     ('Gemini', gemini_bid_price, gemini_ask_price),
                     ('Huobi', huobi_bid_price, huobi_ask_price)]
        
        for i, (exchange_buy, _, ask_price_buy) in enumerate(exchanges):
            for exchange_sell, bid_price_sell, _ in exchanges[i+1:]:
                if bid_price_sell - ask_price_buy > 20:
                    simulate_trade(exchange_buy, exchange_sell, ask_price_buy, bid_price_sell)

        # Sleep for 5 seconds
        time_to_sleep = 5 - (time.time() - start_time)
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)

if __name__ == "__main__":
    main()
