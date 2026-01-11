
import yfinance as yf
import requests
import os


#TElegram bot
#8468785766:AAGrfdeQQSU7i3wEX4uUkAe-UAZEtkurfU8

symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
lines = []

### telegram
TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

for stock in symbols:

    ticker = yf.Ticker(stock)

    # Get latest price
    current_price = ticker.info["currentPrice"]
    previous_close = ticker.info["previousClose"]
    trend = "↑" if current_price > previous_close else "↓"
    stock_name = ticker.info["shortName"]
    
    #print(f"{stock:<5} : {trend}{current_price}")
    lines.append(f"{stock_name:<25} : {trend}{current_price}")
    
#message = "📊 Stock Update\n```\n" + "\n".join(lines) + "\n```"
message = "\n".join(lines)

#print("Here is combined result")
#print(message)

### Now send message using telegram

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
    #,"parse_mode": "Markdown"
})


