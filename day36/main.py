# import requests
# from twilio.rest import Client
#
#
# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"
#
# # STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# # NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# #

########copy from readme



#
#
#     ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
# stock_parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "interval": "1min",
#     "apikey" : STOCK_API_KEY
# }
#
# #Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#
# stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
# stock_response.raise_for_status()
# stock_data = stock_response.json()["Time Series (Daily)"]
# data_list = [value for (key, value) in stock_data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)
#
# # Get the day before yesterday's closing stock price
#
# day_before_yesterday_price = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_price["4. close"]
# print(day_before_yesterday_closing_price)
#
# # Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#
# difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# print(difference)
# up_down = None
# if difference > 0:
#     up_down = '📈'
# else:
#     up_down = '📉'
#
# # Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#
# diff_percent = (difference/float(yesterday_closing_price))*100
# print(diff_percent)
#
# #If TODO4 percentage is greater than 5 then print("Get News").
#
# if diff_percent > 2:
#     news_parameters = {
#         "apikey" : NEWS_API_KEY,
#         "qInTitle": COMPANY_NAME,
#     }
#
#     news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
#     articles = news_response.json()["articles"]
#
# #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
#     three_articles = articles[:3]
#     print(three_articles)
#
#     ## STEP 3: Use twilio.com/docs/sms/quickstart/python
#     #to send a separate message with each article's title and description to your phone number.
#
# #Create a new list of the first 3 article's headline and description using list comprehension.
#
# formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#
# #Send each article as a separate message via Twilio.
#
# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#
# for article in formatted_articles:
#     message = client.messages.create(
#         body=article,
#         from_= "+1 717 276 0228",
#         to="+918767883223"
#     )
#
# # Format the message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
#
