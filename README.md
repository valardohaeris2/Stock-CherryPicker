
# HashiCorp (HCP) Stock/RSU (or any other stock): sell, hold or buy? 
Stock Price and Stock News Python App sends SMS with stock price & the most recent 4 news articles for the company (after an explicit threshold has been met). 

## Pre-reqs:
- Twilio Account
- News API account: https://newsapi.org/
- Stock Market API key: https://www.alphavantage.co/ 


## Useage: 
- To authenticate, provide the following:
  * Stock API Key
  * News API Key
  * Twilio SID and
  * Twilio Auth Token
  * Google Voice number or cellphone number
    
- To get stock data:
  * Enter the stock symbol and/or company name
 
- To set thresholds:
  * Tweek lines 53 - 54
