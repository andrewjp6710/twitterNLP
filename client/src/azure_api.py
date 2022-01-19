import re
import requests

from src.api_config import API_ENDPOINT_DOMAIN

def get_keyword_analysis(statuses):
    data = {"documents": [cleanse_twitter_status(s) for s in statuses]}
    response = requests.post(API_ENDPOINT_DOMAIN + "/azure/keyword-analysis", json=data)
    analysis = response.json()
    return analysis

def get_sentiment_analysis(statuses):
    data = {"documents": [cleanse_twitter_status(s) for s in statuses]}
    response = requests.post(API_ENDPOINT_DOMAIN + "/azure/sentiment-analysis", json=data)
    analysis = response.json()
    return analysis

def cleanse_twitter_status(text):
    return re.sub(r'[^\s]*https?://[^\s]+', "", text)
