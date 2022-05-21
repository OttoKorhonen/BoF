import json
import requests
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

'''
a. Luo ohjelma joka hakee Suomen pankin verkkosivulta valuuttakurssit. Palauta valuutat ja niiden kurssit.
b. Luo REST-rajapinta josta voi hakea valuuttakurssikoodilla nykyisen kurssin.
c. Muokkaa rajapintaa niin että voit kysyä ja saada vastauksena useita kursseja.
d. Lisää rajapintaa BASIC AUTH autentikaatio.
e. Lisää rajapintaan autentikaatio client-sertifikaatilla.
'''

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


@app.route('/api/all', methods=['GET'])
def all_currencies():
    '''function returns data of all currencies in JSON format'''

    currencies_data = requests.get(
        'https://api.boffsaopendata.fi/referencerates/api/ExchangeRate')

    return jsonify(format_data(currencies_data))


@auth.verify_password
def verify_password(username, password):
    '''security function that asks the user to sign in before use'''
    user = 'testi@gmail.com'
    pwd = '123'

    users = {
        user: generate_password_hash(pwd)
    }

    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/api/currencies/<currency>', methods=['GET', 'POST'])
@auth.login_required
def currencies_by_name(currency):
    '''function returns one or more currencies'''
    currency = currency.upper()

    data = requests.get(
        f'https://api.boffsaopendata.fi/referencerates/api/ExchangeRate?currencies={currency}')

    return jsonify(format_data(data))


if __name__ == '__main__':
    app.run(debug=True)

