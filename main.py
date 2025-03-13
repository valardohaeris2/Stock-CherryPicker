import requests
from twilio.rest import Client

STOCK = "HCP"
COMPANY_NAME = "HashiCorp, Inc"      

 
STOCK_ENDPOINT = "https://www.alphavantage.co/query/"                   
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"   
   
STOCK_API_KEY = ""    
NEWS_API_KEY = ""   
TWILIO_SID = "" 
TWILIO_AUTH_TOKEN = ""    
  

# The price change threshold is set VERY low (0.2%). Modify threshold according to market indicators. 
# When STOCK price increase/decreases by 0.2% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY, 
} 
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print("Yesterday's close was: " + yesterday_closing_price)

# Day before yesterday closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print("Day before close was:  " + day_before_yesterday_closing_price))

# difference between yesterday and day before yesterday's closing price
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Percentage diff in closing price between yesterday and day before yesterday
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# If diff is > 0.2% get the first 4 news pieces for the COMPANY_NAME from  https://newsapi.org
if abs(diff_percent) > 0.2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    four_articles = articles[:4]
    print(four_articles)


# Register with https://www.twilio.com and send a seperate message with the percentage change and each article's date, title and description to your Google Voice phone number. 

formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nDate: {article['publishedAt']} \nBrief: {article['description']}" for article in four_articles]

# Formated SMS message:
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="<twilio_number>",
        to="<cellphone_number>"
)



