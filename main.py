import requests

path = "https://api.coinmarketcap.com/v1/ticker/"

def get_crypto_prices(crypto):
    data = requests.get(path+crypto)

    json = data.json()

    price = float(json[0]['price_usd'])

    return price
decision = True
while decision:
    price = get_crypto_prices('bitcoin')
    print(price)   