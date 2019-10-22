from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import urllib.request


import json
import pickle as p


"""create and configures an instance of a flask app"""
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


@APP.route('/')
def root():
    request
    message = 'Working render.'
    return render_template('base.html', message=message)

@APP.route('/request')
def request_data():

    return "Requesting data"

@APP.route('/predictor')
def predictor():
    request
    return " predictor is here"

# Here lies the dummy data.
@APP.route('/dummy')
def dummy_data():
    with open('dummy.json', 'r') as f:
        dummy = json.load(f)
    return dummy

@APP.route('/topredict')
def request_info():
    url = "http://127.0.0.1:5000/dummy"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data
# Above lies the dummy data.

if __name__ == '__main__':
    APP.run(debug=True)
