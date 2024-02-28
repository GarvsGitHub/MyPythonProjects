import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "ESJRTFLI28907"  # Generate yours on site
NEWS_API_KEY = "2b660e2be5e84b2291b82e8cb4dad"  # Generate yours on site

TWILIO_SID = "Login and Get Yor SID"
TWILIO_AUTH_TOKEN = "Login and Get your Token"

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # Here we fetched dictionary data
yesterdays_data = data_list[0]  # we fetched data using index value because it's dictionary data
yesterdays_closing = yesterdays_data["4. close"]  # Here we fetched value using key as its dictionary
# print(yesterdays_closing)

# Get the day before yesterday's closing stock price
day_before_yesterdays_data = data_list[1]
day_before_yesterdays_closing = day_before_yesterdays_data["4. close"]
# print(day_before_yesterdays_closing)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = abs(float(yesterdays_closing) - float(day_before_yesterdays_closing))
# print(difference)

# Find the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterdays_closing)) * 100)
# print(diff_percent)

# If TODO4 percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_params = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API_KEY,
}
if diff_percent > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
# Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[1:4]

    # to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 articles headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}"
                          for article in three_articles]

# Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+15138134901", # Expired Twilio Number
            to="Your Phone Number"
        )

# (Optional) Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
"""
