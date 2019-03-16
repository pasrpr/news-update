import os
import requests
import sys

try:
    API_TOKEN = os.environ['API_TOKEN']
except KeyError:
    #if it's not an env var, then we might be testing
    API_TOKEN = input("Enter your API Token Key:")

def soupify_event_page(url='https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=API_TOKEN'):
    try:
        r = requests.get(url).json()
    except:
        return

    org_json = requests.get(url).json()
    return org_json

def main():
    soup = soupify_event_page()
    if not soup:
        sys.exit(1)

    news=[]
    for a in soup['articles']:
        news.append(a['title']+' : '+a['url'])
    return news

if __name__ == '__main__':
    events = main()
    print(events)