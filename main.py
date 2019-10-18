import requests
import time

path = "https://api.coinmarketcap.com/v1/ticker/"

def get_crypto_prices(crypto):
    data = requests.get(path+crypto)

    json = data.json()

    price = float(json[0]['price_usd'])

    return price
decision = True
price = get_crypto_prices('bitcoin')
print(price)
while decision:   
    time.sleep(5) #stop for five seconds and then continue
    new_price = get_crypto_prices('bitcoin')
    if price > new_price or price < new_price:
        print(f'new price {new_price}')
        break
    print(price)