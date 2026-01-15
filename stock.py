
import yfinance as yf
import requests
import os


stocks_env = os.environ.get("STOCKS", "")
symbols = [s.strip().upper() for s in stocks_env.split(",") if s.strip()]

lines = []

### telegram
TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

for stock in symbols:

    ticker = yf.Ticker(stock)
  
    current_price = ticker.fast_info["last_price"]
    previous_close = ticker.fast_info["previous_close"]

    trend = "↑" if current_price > previous_close else "↓"
    
    percent_change = ((current_price - previous_close) / previous_close) * 100

    
    lines.append(f"{stock:<10} : {trend}{current_price:.2f} / {percent_change:.2f}%")
    
message = "\n".join(lines)


### Now send message using telegram

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})


