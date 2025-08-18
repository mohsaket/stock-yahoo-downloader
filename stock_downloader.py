import yfinance as yf

def download_stock_data():
    # Get user input for stock symbol and timeframe
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA, BTC-USD): ").strip().upper()
    section = input("Enter Windsor Name  ( APPLE ): ").strip().upper()
    timeframe = input("Enter timeframe (e.g., 1m, 5m, 1h, 1d, 1wk, 1mo): ").strip()

    # Map timeframes to CFD value
    timeframe_map = {
        '1m': '1',   # 1 minute
        '5m': '5',   # 5 minutes
        '15m': '15',  # 15 minutes
        '30m': '30',  # 30 minutes
        '60m': '60',  # 1 hour
        '1h': '60',   # 1 hour
        '1d': '1440', # 1 day
        '1wk': '10080', # 1 week (in minutes)
        '1mo': '43200' # 1 month (in minutes)
    }

    # Set period based on the interval
    period_map = {
        '1m': '7d',
        '5m': '60d',
        '15m': '60d',
        '30m': '60d',
        '60m': '730d',
        '1h': '730d',
        '1d': 'max',
        '1wk': 'max',
        '1mo': 'max'
    }

    period = period_map.get(timeframe, 'max')
    cfd_timeframe = timeframe_map.get(timeframe, '1440')  # Default to 1d (1440)

    try:
        # Download data from Yahoo Finance
        data = yf.download(symbol, period=period, interval=timeframe, auto_adjust=False)
        if data.empty:
            print("⚠️ No data available for this timeframe or it is not supported.")
            return

        # Remove "Adj Close" column if it exists
        if 'Adj Close' in data.columns:
            data.drop('Adj Close', axis=1, inplace=True)

        # Save data to CSV file in the desired format
        filename = f"{section}_CFD{cfd_timeframe}.csv"
        data.reset_index(inplace=True)
        
        # Handle date and time formatting
        if timeframe.endswith('m') or timeframe.endswith('h'):
            data['Date'] = data['Datetime'].dt.strftime('%Y.%m.%d')
            data['Time'] = data['Datetime'].dt.strftime('%H:%M')
        else:
            data['Date'] = data['Date'].dt.strftime('%Y.%m.%d')
            data['Time'] = '0:00'

        # Reorder and rename columns
        data = data[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']]
        
        # Save as tab-separated CSV
        data.to_csv(filename, sep=',', index=False, header=False)
        print(f"✅ Data successfully saved to {filename}.")

    except Exception as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    download_stock_data()
