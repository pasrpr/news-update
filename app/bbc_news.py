import os
import requests
import sys

try:
    API_TOKEN = os.environ['API_TOKEN']
except KeyError:
    #if it's not an env var, then we might be testing
    API_TOKEN = input("Enter your API Token Key:")

def get_content(url='https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey='+API_TOKEN):
    try:
        news_json = requests.get(url).json()
    except:
        return
    return news_json

def news():
    news_data = get_content()
    if not news_data:
        sys.exit(1)

    bbc_news = {}
    for article in news_data['articles']:
        bbc_news[article['title']] = article['url']
    return bbc_news