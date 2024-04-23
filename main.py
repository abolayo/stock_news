import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily 80edc6608913459e81487aae1055c0b7
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=UFT185NW0HP8DU5T'
# r = requests.get(url)
# data = r.json()
#
# print(data['Time Series (Daily)'])
# closing_price = [value['4. close'] for (key, value) in data['Time Series (Daily)'].items()]
#
# # Get the yesterday's closing stock price
# yesterday_closing_price = float(closing_price[0])
# # Get the day before yesterday's closing stock price
# d_yesterday_closing_price = float(closing_price[1])
#
# # the positive difference between 1 and 2.
# p_diff = round(abs(yesterday_closing_price - d_yesterday_closing_price), 3)
#
# # Work out the percentage difference in price between closing price yesterday and closing price the day before
# # yesterday.
# percentage_diff = round((p_diff / yesterday_closing_price) * 100, 3)
#
# # If percentage is greater than 5 then print("Get News").
# if percentage_diff <= 5:
# https://newsapi.org/
# get the first 3 news pieces for the Tesla Inc.
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-03-23&sortBy=publishedAt&apiKey"
       "=80edc6608913459e81487aae1055c0b7")
r = requests.get(url)
news = r.json()

# A list that contains the first 3 articles.
articles = news["articles"][:3]
# STEP 3: Use twilio.com/docs/sms/quickstart/python ## 2ZU167TREYC7VERJ1761C5DZ
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
articles_headlines = [value['title'] for value in articles]

print(articles_headlines)
#TODO 9. - Send each article as a separate message via Twilio. 


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
