import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = ""
NEWS_API_KEY = ""
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
#2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
#3. - Find the positive difference between 1 and 2
diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (float(diff)/float(yesterday_closing_price))*100
#. - If  percentage is greater than 5 then print news.

if diff_percent > 5:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"] # news articles pertaining to specified company

    ## STEP 2: https://newsapi.org/ 

#7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_arts = articles[:3]


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_news = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_arts]
