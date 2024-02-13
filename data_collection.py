import time
import pandas as pd
from datetime import datetime
from BTC.coinbase_btc import get_bitcoin_prices_coinbase
from BTC.kraken_btc import get_bitcoin_prices_kraken
from BTC.gemini_btc import get_bitcoin_prices_gemini
from BTC.analyze import calculate_and_save_deltas
import sys  # Import sys for exiting the script

def collect_data(duration_minutes):
    end_time = time.time() + (duration_minutes * 60)
    data = []

    while time.time() < end_time:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Handles errors hat arise 
        try:
            coinbase_data = get_bitcoin_prices_coinbase()
            if coinbase_data is None or None in coinbase_data:
                raise ValueError("Coinbase API failed to deliver data.")
            kraken_data = get_bitcoin_prices_kraken()
            if kraken_data is None or None in kraken_data:
                raise ValueError("Kraken API failed to deliver data.")
            gemini_data = get_bitcoin_prices_gemini()
            if gemini_data is None or None in gemini_data:
                raise ValueError("Gemini API failed to deliver data.")
        except ValueError as e:
            print(e)
            sys.exit("Script terminated due to API failure.")

        # Append the data with the timestamp
        data.append({
            'Timestamp': timestamp,
            'Coinbase Bid': coinbase_data[0],
            'Coinbase Ask': coinbase_data[1],
            'Kraken Bid': kraken_data[0],
            'Kraken Ask': kraken_data[1],
            'Gemini Bid': gemini_data[0],
            'Gemini Ask': gemini_data[1]
        })

        time.sleep(1)  # Wait for 1 second before the next API call

    return pd.DataFrame(data)

def main(duration_minutes):
    start_time = time.time()
    df = collect_data(duration_minutes)
    
    # Calculate runtime
    runtime = round((time.time() - start_time), 3)
    
    # Add runtime to the DataFrame as a new row
    df = df.append({'Timestamp': 'Runtime (seconds)', 'Coinbase Bid': runtime}, ignore_index=True)
    
    # Save the DataFrame to an Excel file
    filename = 'crypto_data.xlsx'
    df.to_excel(filename, index=False)
    print(f"Data collected and saved to {filename}")

if __name__ == "__main__":
    duration_minutes = 360  # Set the duration for which you want to collect data
    main(duration_minutes)

#calculate_and_save_deltas()