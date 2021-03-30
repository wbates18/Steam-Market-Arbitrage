import requests

StatrakConst = "StatTrak%E2%84%A2"

gunname = "AK-47"
skin = "Fire Serpent"
quality = "Field-Tested"

Statrak = True

if Statrak == True:
    itemname = StatrakConst + " " + gunname + " | " + skin + " (" + quality + ")"
else:
    itemname = gunname + " | " + skin + " (" + quality + ")"

print(itemname)
url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name={}".format(itemname)
responce = requests.get(url)
json = responce.json()
print(json)