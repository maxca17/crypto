import pandas as pd

def calculate_and_save_deltas(input_filename, output_filename):
    # Load the Excel file
    df = pd.read_excel(input_filename)
    
    # Remove the runtime row if present to avoid calculation errors
    df = df[df['Timestamp'] != 'Runtime (seconds)']
    
    # Calculate deltas for each exchange and add them as new columns
    df['Coinbase Delta'] = (df['Coinbase Ask'] - df['Coinbase Bid']).abs()
    df['Kraken Delta'] = (df['Kraken Ask'] - df['Kraken Bid']).abs()
    df['Gemini Delta'] = (df['Gemini Ask'] - df['Gemini Bid']).abs()
    
    # Save the updated DataFrame to a new Excel file
    df.to_excel(output_filename, index=False)
    print(f"Data with deltas saved to {output_filename}")

if __name__ == "__main__":
    input_filename = 'crypto_data.xlsx'
    output_filename = 'crypto_data_with_deltas.xlsx'
    calculate_and_save_deltas(input_filename, output_filename)
