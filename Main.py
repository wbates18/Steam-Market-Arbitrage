import requests
from currency_converter import CurrencyConverter
import re
c = CurrencyConverter()

def cad(usd):
    usd = str(usd).replace("$", "")
    usd = str(usd).replace(",", "")
    usd = float(usd)
    cad = c.convert(usd, 'USD', 'CAD')
    cad = round(cad, 2)
    return cad






StatrakConst = "StatTrak%E2%84%A2"

with open("AllSkins.txt", "r") as Skins:
    r = Skins.readlines()
    Skins.close()

Co = {}
C = {}
R = {}
M = {}
CaseList = []
for x in r:
    if "?Cases" in x:
        Cases = {}
        y = 0

    if "?Collections" in x:
        break

    if '!' in x:
        Case = x.replace("\n", "")
        Case = Case.replace("!", "")
        Cases[Case] = {}
        TempCase = Case
        CaseList.append(Case)
        Co[TempCase] = 0
        C[TempCase] = 0
        R[TempCase] = 0
        M[TempCase] = 0
        y = 1

    elif y == 1:
        if "Mil-Spec" in x:
            Rarity = "Mil-Spec"
            if M[TempCase] != 1:
                Cases[TempCase][Rarity] = []
                M[TempCase] = 1
        elif "Restricted" in x:
            Rarity = "Restricted"
            if R[TempCase] != 1:
                Cases[TempCase][Rarity] = []
                R[TempCase] = 1
        elif "Classified" in x:
            Rarity = "Classified"
            if C[TempCase] != 1:
                Cases[TempCase][Rarity] = []
                C[TempCase] = 1
        elif "Covert" in x:
            Rarity = "Covert"
            if Co[TempCase] != 1:
                Cases[TempCase][Rarity] = []
                Co[TempCase] = 1
        Float1 = x.split(' - ')
        Float = Float1[2].replace("\n", "")
        Skin = Float1[0]
        SkinF = (Skin, Float)
        Cases[TempCase][Rarity].append(SkinF)


for a in CaseList: # Case
    for i in Cases[a]: # Rarity
        for n in Cases[a][i]: # Skin
            Float = n[1].split(":")
            FFloat = Float[0]
            SFloat = Float[1]
            if 0 <= float(FFloat) <= 0.07:
                FFloat = "Factory New"
            else:
                if 0.07 < float(FFloat) <= 0.15:
                    FFloat = "Minimal Wear"
                else:
                    if 0.15 < float(FFloat) <= 0.37:
                        FFloat = "Field-Tested"
                    else:
                        if 0.37 < float(FFloat) <= 0.44:
                            FFloat = "Well-Worn"
                        else:
                            if 0.44 < float(FFloat) <= 1:
                                FFloat = "Battle-Scared"
            if 0 <= float(SFloat) <= 0.07:
                SFloat = "Factory New"
            else:
                if 0.07 < float(SFloat) <= 0.15:
                    SFloat = "Minimal Wear"
                else:
                    if 0.15 < float(SFloat) <= 0.37:
                        SFloat = "Field-Tested"
                    else:
                        if 0.37 < float(SFloat) <= 0.44:
                            SFloat = "Well-Worn"
                        else:
                            if 0.44 < float(SFloat) <= 1:
                                SFloat = "Battle-Scared"
            print(FFloat, SFloat)
            if FFloat == "Factory New" and SFloat == "Battle-Scared":
                FloatRange = ["Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scared"]
            elif FFloat == "Minimal Wear" and SFloat == "Battle-Scared":
                FloatRange = ["Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scared"]






# Cases['Spectrum 2'][3][1]['float']








url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}".format(itemname)
responce = requests.get(url)
json = responce.json()
