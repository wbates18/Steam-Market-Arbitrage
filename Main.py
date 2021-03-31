import requests
from currency_converter import CurrencyConverter
c = CurrencyConverter()

def cad(usd):
    usd = str(usd).replace("$", "")
    usd = str(usd).replace(",", "")
    usd = float(usd)
    cad = c.convert(usd, 'USD', 'CAD')
    cad = round(cad, 2)
    return cad


StatrakConst = "StatTrak%E2%84%A2"

gunname = "AK-47"
skin = "Fire Serpent"
quality = "Well-Worn"

Statrak = True

if Statrak:
    itemname = StatrakConst + " " + gunname + " | " + skin + " (" + quality + ")"
else:
    itemname = gunname + " | " + skin + " (" + quality + ")"

print(itemname)
url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}".format(itemname)
print(url)
responce = requests.get(url)
json = responce.json()
print(cad(json['lowest_price']))