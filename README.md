# 📈 Stock Alert Bot

This is the **second project** I built for the *Advanced Programming* course at the University of Helsinki. It’s a Python script that **watches any stock you choose** and sends you a **news update via SMS** if the price jumps or drops more than 5%.

---

## ⚙️ How It Works

- Gets daily stock data from **Alpha Vantage**
- Compares closing prices for the last two days
- If the change > 5%:
  - Fetches 3 relevant news stories via **NewsAPI**
  - Sends them to your phone with **Twilio SMS**
 
## 🚀 Setup

1. Open `main.py` and update:
   - Stock symbol and company name
   - Your API keys (Alpha Vantage, NewsAPI)
   - Twilio SID, auth token, and phone numbers
2. Run the script:
   - python main.py
