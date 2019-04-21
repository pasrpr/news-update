import os
import requests
import sys
#   API_TOKEN = 'd092cf0e3c8a40cb8d197d112fcc0aaa'

try:
    API_TOKEN = os.environ['API_TOKEN']
except KeyError:
    #if it's not an env var, then we might be testing
    API_TOKEN = input("Enter your API Token Key:")

def get_content(url='https://newsapi.org/v2/top-headlines?sources=cnn&apiKey='+API_TOKEN):
    try:
        news_json = requests.get(url).json()
    except:
        return
    return news_json

def news():
    news_data = get_content()
    if not news_data:
        sys.exit(1)

    #news = []
    cnn_news = {}
    for article in news_data['articles']:
        cnn_news[article['title']] = article['url']
        #news.append(article['title'] + ' : ' + article['url'])
    return cnn_news
