import requests
itemname = "UMP-45 | Grand Prix (Factory New)"

url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}".format(itemname)
responce = requests.get(url)
json = responce.json()
print(json)