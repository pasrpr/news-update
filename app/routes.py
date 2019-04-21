from app import app
from flask import render_template, request
from .news import main as updates

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


    return render_template('result.html', title='News', news = updates)