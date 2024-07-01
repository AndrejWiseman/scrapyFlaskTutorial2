from __future__ import unicode_literals
from flask import Flask, request, Response, render_template, session, redirect, url_for
import json
import requests
import pandas as pd
import os

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/scrap')
def scrape():
    params = {
        'spider_name': 'books',
        'start_requests': True,
    }

    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    df = pd.DataFrame(data=data['items'], columns=['Title', 'Price'])
    return render_template('simple.html', tables=[df.to_html(classes='data', index=False)], titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug=True, port=1234)
