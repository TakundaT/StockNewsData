# Stock Price Alert with News Notifications

## Description
This Python script monitors Tesla Inc.'s stock price using the Alpha Vantage API. If the stock price changes by more than 5% compared to the previous day's closing price, it fetches the latest news articles related to Tesla Inc. from the News API and formats them for notification.

## Features
- Fetches daily stock prices from [Alpha Vantage](https://www.alphavantage.co/documentation/#daily).
- Calculates the percentage change between the last two closing prices.
- Retrieves the latest news articles from [News API](https://newsapi.org/).
- Uses list comprehensions to extract and format relevant stock and news data.
- Sends stock news alerts when the price fluctuation exceeds 5%.

## Requirements
Ensure you have the following Python modules installed:
```sh
pip install requests twilio
```

## Configuration
Before running the script, update the following variables with your API keys:
- `STOCK_API_KEY`: Your Alpha Vantage API key.
- `NEWS_API_KEY`: Your News API key.

Also, specify the stock and company name:
- `STOCK_NAME`: Stock symbol (e.g., `TSLA` for Tesla Inc.).
- `COMPANY_NAME`: Full name of the company (e.g., `Tesla Inc`).

## How It Works
1. Fetches Tesla Inc.'s stock data for the last two days.
2. Extracts the closing prices of yesterday and the day before yesterday.
3. Calculates the absolute percentage difference.
4. If the price movement exceeds 5%, it fetches the latest news articles about Tesla Inc.
5. Formats and prints the top 3 news headlines with descriptions.

## Usage
Run the script using:
```sh
python stock_news_alert.py
```

## Important Notes
- Ensure you have valid API keys for Alpha Vantage and News API.
- Replace `STOCK_API_KEY` and `NEWS_API_KEY` with your actual API credentials.
- This project is still being developed to send messages via twillio whenever there is a significant change in stock price between two days.


## License
This project is open-source and free to use.

## Author
Takunda Christian Takaindisa

