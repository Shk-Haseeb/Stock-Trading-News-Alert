# 📈 Stock Alert Bot 🚀
This is a Python script that keeps an eye on a stock price 📉📈 and sends you breaking news updates via SMS if there's a big movement! 📲

## 🔧 What It Does
- Checks the daily closing prices of TSLA using Alpha Vantage.
- Calculates the % difference between yesterday and the day before.
- If the price moves more than 5% ⬆️ or ⬇️:
- Fetches the top 3 news articles about Tesla from NewsAPI.
- Sends you the headlines and summaries via Twilio SMS!

## 💡 Example SMS
TSLA: 🔻5%
Headline: Tesla Shares Dip After Market Shock
Brief: Tesla stock took a hit today following recent economic data releases and investor concerns.

## 🔑 You'll Need
- 📊 Alpha Vantage API key
- 📰 NewsAPI key
- 📞 Twilio account (for sending SMS)

## 🚀 How to Run
- Replace the placeholders like STOCK_API_KEY, NEWS_API_KEY, TWILIO_SID, TWILIO_AUTH_KEY, etc.
- Run the script: python stock_alert.py

## ✅ Done! If Tesla moves big, you’ll get the news straight to your phone.
