# Bank of Finland pre-assignment
This is job pre-assignment made for BoF.

## About
This application is programmed with Python 3 programming language using Flask framework. The purpose of this application is to fetch currency data from BoF api and make the wanted data available. The data is presented in JSON format.

The requirements for this application were:

- Fetch all currencies and their exchange rates
- Create REST interface where user can make a request by exchange rate code
- Create REST interface where user can make multiple requests by exchange rate codes
- Add basic authentication for the REST interface
- Add client certificate authentication for the REST interface (not done)

## Installation
In order to make this application run you need Python 3 programming language installed.

To install all the required modules for this projects run the following command in the project folder:
>pip install -r requirements.txt

## Usage
After installation start the program by running app.py file by running the following command:
>python3 app.py

The program is running on http://127.0.0.1:5000

You can use cURL to make the requests to the endpoints.

cURL example:
> curl -su 'testi@gmail.com' http://127.0.0.1:5000/api/currencies/brl,usd,sek

password: 123

To make a request for all currency data use the following endpoint:
>/api/all


```
[

    {
        "currency": "AUD",
        "value": "1.498"
    },
    {
        "currency": "BGN",
        "value": "1.9558"
    },
    {
        "currency": "BRL",
        "value": "5.1989"
    },
    {
        "currency": "CAD",
        "value": "1.3526"
    },
    {
        "currency": "CHF",
        "value": "1.028"
    }
]

```

To make a request for a specific currency use the following endpoint and currency code i.e jpy:
>/api/currencies/jpy

```
[
    {
        "currency": "JPY",
        "value": "135.34"
    }

]
```

To make a request for multiple currencies use the following endpoint and currency codes i.e brl,usd,sek NOTE: currency codes are separated by comma:
>/api/currencies/brl,usd,sek

```
[

    {
        "currency": "BRL",
        "value": "5.1989"
    },
    {
        "currency": "SEK",
        "value": "10.4915"
    },
    {
        "currency": "USD",
        "value": "1.0577"
    }

]
```