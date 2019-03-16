import bs4
import requests
import sys

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
    news = []
    for i in range(10):
        news.append(events_divs[i].text.strip() + ':' + events_divs[i]['href'])
    return news

if __name__ == '__main__':
    news = main()