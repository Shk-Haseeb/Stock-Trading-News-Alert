import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"  # Replace with any stock symbol you want to track
COMPANY_NAME = "Tesla Inc"  # Replace with the company name you want to search in news

STOCK_API_KEY = "YOUR_STOCK_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH_KEY = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_FROM = "YOUR_TWILIO_PHONE_NUMBER"
TWILIO_TO = "DESTINATION_PHONE_NUMBER"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get("https://www.alphavantage.co/query", params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

data_list = list(stock_data.values())
yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

price_diff = yesterday_close - day_before_close
up_down = "🔺" if price_diff > 0 else "🔻"
percent_change = round((abs(price_diff) / day_before_close) * 100)

# ========== FETCH NEWS AND SEND SMS IF NEEDED ==========
if percent_change > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percent_change}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_KEY)
    for article_text in formatted_articles:
        message = client.messages.create(
            body=article_text,
            from_=TWILIO_FROM,
            to=TWILIO_TO
        )
        print(f"Sent message with status: {message.status}")

