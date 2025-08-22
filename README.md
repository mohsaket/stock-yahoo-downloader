
# Stock Data Downloader 📊

A simple Python script to download stock, crypto, and index data from **Yahoo Finance** and export it into CSV format.  
Useful for traders, analysts, and algorithm developers (compatible with MetaTrader / MQL).

## ✨ Features
- Download historical data for **stocks, crypto, forex, and indices**.
- Supports multiple timeframes: `1m, 5m, 15m, 30m, 1h, 1d, 1wk, 1mo`.
- Exports clean CSV files: **Date, Time, Open, High, Low, Close, Volume**.
- Easy to integrate with **MQL5 / backtesting tools**.

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/stock-data-downloader.git
cd stock-data-downloader
pip install -r requirements.txt
```

## 🚀 Usage
Run the script:

```bash
python stock_downloader.py
```

Example run:
```
Enter stock symbol (e.g., AAPL, TSLA, BTC-USD): AAPL
Enter Windsor Name  ( APPLE ): APPLE
Enter timeframe (e.g., 1m, 5m, 1h, 1d, 1wk, 1mo): 1h
```

Output:
```
✅ Data successfully saved to APPLE_CFD60.csv
```

## 📂 Example CSV Output
```
2025.08.18, 10:30, 180.50, 182.00, 179.80, 181.20, 234567
2025.08.18, 11:30, 181.20, 183.10, 180.90, 182.40, 198765
```

## 🖼 Screenshot

```markdown
![Demo Screenshot](stock-yahoo-downloader/assets/demo.png)
```

## 📌 Requirements
- Python 3.8+
- yfinance
- pandas

## 👨‍💻 Author
Developed by [@MSaket](https://t.me/MSaket)  
MQL & Python Developer | Trader | Algorithmic Trading Enthusiast
