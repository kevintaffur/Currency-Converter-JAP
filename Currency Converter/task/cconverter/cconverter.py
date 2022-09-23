import json

import requests as requests

currency = input()
currency = currency.lower()

path = f"http://www.floatrates.com/daily/{currency}.json"
r = requests.get(path)
dictionary = json.loads(r.text)

if currency == "usd":
    exchanges = {"eur": dictionary["eur"]["rate"]}
elif currency == "eur":
    exchanges = {"usd": dictionary["usd"]["rate"]}
else:
    exchanges = {"usd": dictionary["usd"]["rate"], "eur": dictionary["eur"]["rate"]}


while True:
    exchange = input()
    if exchange == "":
        break
    exchange = exchange.lower()

    amount = float(input())

    print("Checking the cache...")
    if exchange in exchanges:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        exchanges[exchange] = dictionary[exchange]["rate"]

    result = float(exchanges[exchange]) * amount
    result = round(result, 2)
    print(f"You received {result} {exchange.upper()}.")
