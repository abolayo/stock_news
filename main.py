import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily 80edc6608913459e81487aae1055c0b7
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=UFT185NW0HP8DU5T'
r = requests.get(url)
data = r.json()

print(data['Time Series (Daily)'])
closing_price = [value['4. close'] for (key, value) in data['Time Series (Daily)'].items()]

# Get the yesterday's closing stock price
yesterday_closing_price = float(closing_price[0])
# Get the day before yesterday's closing stock price
d_yesterday_closing_price = float(closing_price[1])

# the positive difference between 1 and 2.
p_diff = round(abs(yesterday_closing_price - d_yesterday_closing_price), 0)

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
percentage_diff = round((p_diff / yesterday_closing_price) * 100, 3)

# If percentage is greater than 5 then print("Get News").
if percentage_diff >= 5:
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

    # - Create a new list of the first 3 article's headline and description using list comprehension.
    articles_headlines = [value['title'] for value in articles]
    content = [value['content'] for value in articles]


    # - Send each article as a separate message via Twilio.

    #Optional  Format the message:
    for i in range(len(content)):
        if yesterday_closing_price > d_yesterday_closing_price:

            print(
                f"TSLA: 🔺{int(percentage_diff)}% \n"
                f"Headline: {articles_headlines[i]} \n"
                f"Brief: {content[i]}."
            )
        else:

            print(
                f"TSLA: 🔻{int(percentage_diff)}% \n"
                f"Headline: {articles_headlines[i]} \n"
                f"Brief: {content[i]}"
            )
