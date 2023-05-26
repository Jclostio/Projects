from flask import Flask
from flask import render_template
from flask import request
import requests
app = Flask(__name__)


# Playing around with Flask, makes a simple HTTP GET request that pulls from a random api (cat facts)

@app.route('/', methods=['GET', 'POST'])
def main():
    api_url = "https://cat-fact.herokuapp.com/facts/random"
    response = requests.get(api_url)
    response = response.json()
    if request.method == 'POST':
        if request.form.get('action1') == 'New Cat Fact':
            response = requests.get(api_url)
            response = response.json()
            return render_template('index.html', response=response['text'])
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html', response=response['text'])

    return render_template('index.html', response=response['text'])
