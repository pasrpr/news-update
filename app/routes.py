from app import app
from flask import render_template, request
# from .news import main as updates
from .google_news import news as google_news
from .bbc_news import news as bbc_news
from .cnn_news import news as cnn_news

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/result')
def result():
    # headline = updates.keys()
    # news = {}
    # for k in updates.keys():
    #     news[headline] = updates[k]
    news = google_news().copy()
    news.update(bbc_news())
    news.update(cnn_news())
    return render_template('result.html', title='News', news = news.keys(), urls = news.values())