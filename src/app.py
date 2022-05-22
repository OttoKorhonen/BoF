import json
import requests
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.secret_key = 'sheize0heemifoaHech9Uz9oepa4ah'


@app.route('/', methods=['GET'])
def index():
    '''returns hello message'''
    return 'Hello BoF currency application!'


def format_data(data):
    '''
    function picks currency data and exhange rate data from given parametre
    makes new dict that is added on a list and the list is returned
    '''
    currencies = []
    data = json.loads(data.text)

    for d in data:
        currencies.append(
            {'currency': d['Currency'], 'value': d['ExchangeRates'][0]['Value']})

    return currencies


def fetch_data(*currencies):
    '''function fetches data from bof api and returns it'''
    url = 'https://api.boffsaopendata.fi/referencerates/api/ExchangeRate'
    params = {
        'currencies': currencies
    }
    currencies_data = requests.get(url, params=params)

    return currencies_data


@app.route('/api/all', methods=['GET'])
@auth.login_required
def all_currencies():
    '''function returns data of all currencies in JSON format'''
    data = fetch_data()

    return jsonify(format_data(data))


@auth.verify_password
def verify_password(username, password):
    '''
    security function that asks the user to sign in before use.
    this is not a proper way to make an authentication. user info
    should never be available like this.
    '''
    user = 'testi@gmail.com'
    pwd = '123'

    users = {
        user: generate_password_hash(pwd)
    }

    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/api/currencies/<currency>', methods=['GET'])
@auth.login_required
def currencies_by_name(currency):
    '''function returns one or more currencies'''
    currency = currency.upper()
    data = fetch_data(currency)

    return jsonify(format_data(data))


if __name__ == '__main__':
    app.run(debug=True)
