from google_news import news as google_news
from bbc_news import news as bbc_news
from cnn_news import news as cnn_news

def main():
    news = google_news()+bbc_news()+cnn_news()
    return news

if __name__ == '__main__':
    news = main()
    print(news)
