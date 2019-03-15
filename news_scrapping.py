import bs4
import html
import json
import re
import requests
import sys
import unicodedata
import pprint


def soupify_event_page(url='https://news.google.com/?hl=en-US&gl=US&ceid=US:en'):
    try:
        r = requests.get(url)
    except:
        return
    content = r.content
    soup = bs4.BeautifulSoup(content, 'html.parser')

    return soup

def main():
    soup = soupify_event_page()
    if not soup:
        sys.exit(1)

    events_divs = soup.findAll('a',{'class':'DY5T1d'})
    #event_divs.find('a').get('href')
    news = {}
    for i in range(5):
        news[events_divs[i].text.strip()] = events_divs[i]['href']
        #print(events_divs[i]['href'])
    print(news)
    return news

if __name__ == '__main__':
    events = main()
    print(events)