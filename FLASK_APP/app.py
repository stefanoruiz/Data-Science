from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import json
import pickle as p


"""create and configures an instance of a flask app"""
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


@APP.route('/')
def root():
    request
    return "Welcome, Register here"

@APP.route('/request')
def request_data():
    request
    return "Requesting data"

@APP.route('/predictor')
def predictor():
    request
    return " predictor is here"


if __name__ == '__main__':
    APP.run(debug=True)
