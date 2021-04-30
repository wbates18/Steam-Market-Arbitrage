import requests
from currency_converter import CurrencyConverter
import time
import beepy
import numpy
c = CurrencyConverter()

def cad(usd):
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

CaseListConfirm = []
for a in CaseList: # Case
    print(a)
    PrevPrice = {}
    WorstPrice = {}
    AllPrice = {}
    for i in Cases[a]: # Rarity
        print(i)
        AllPrice[i] = {}
        WorstPrice[i] = {'Factory New': ["", 0], 'Minimal Wear': ["", 0], 'Field-Tested': ["", 0], 'Well-Worn': ["", 0], 'Battle-Scarred': ["", 0]}
        PrevPrice[i] = {'Factory New': ["", 10000], 'Minimal Wear': ["", 10000], 'Field-Tested': ["", 10000], 'Well-Worn': ["", 10000], 'Battle-Scarred': ["", 10000]}
        for n in Cases[a][i]: # Skin
            AllPrice[i][n] = {'Factory New': 0, 'Minimal Wear': 0, 'Field-Tested': 0, 'Well-Worn': 0, 'Battle-Scarred': 0}
            FloatRange = []
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
                                FFloat = "Battle-Scarred"
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
                                SFloat = "Battle-Scarred"
            if FFloat == "Factory New" and SFloat == "Battle-Scarred":
                FloatRange = ["Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred"]
            elif FFloat == "Minimal Wear" and SFloat == "Battle-Scarred":
                FloatRange = ["Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred"]
            elif FFloat == "Field-Tested" and SFloat == "Battle-Scarred":
                FloatRange = ["Field-Tested", "Well-Worn", "Battle-Scarred"]
            elif FFloat == "Well-Worn" and SFloat == "Battle-Scarred":
                FloatRange = ["Well-Worn", "Battle-Scarred"]
            elif FFloat == "Factory New" and SFloat == "Well-Worn":
                FloatRange = ["Factory New", "Minimal Wear", "Field-Tested", "Well-Worn"]
            elif FFloat == "Minimal Wear" and SFloat == "Well-Worn":
                FloatRange = ["Minimal Wear", "Field-Tested", "Well-Worn"]
            elif FFloat == "Field-Tested" and SFloat == "Well-Worn":
                FloatRange = ["Field-Tested", "Well-Worn"]
            elif FFloat == "Factory New" and SFloat == "Field-Tested":
                FloatRange = ["Factory New", "Minimal Wear", "Field-Tested"]
            elif FFloat == "Minimal Wear" and SFloat == "Field-Tested":
                FloatRange = ["Minimal Wear", "Field-Tested", "Well-Worn"]
            elif FFloat == "Factory New" and SFloat == "Minimal Wear":
                FloatRange = ["Factory New", "Minimal Wear"]
            elif FFloat == "Factory New" and SFloat == "Factory New":
                FloatRange = ["Factory New"]
            elif FFloat == "Minimal Wear" and SFloat == "Minimal Wear":
                FloatRange = ["Minimal Wear"]
            elif FFloat == "Field-Tested" and SFloat == "Field-Tested":
                FloatRange = ["Field-Tested"]
            elif FFloat == "Well-Worn" and SFloat == "Well-Worn":
                FloatRange = ["Well-Worn"]
            elif FFloat == "Minimal Wear" and SFloat == "Field-Tested":
                FloatRange = ["Minimal Wear", "Field-Tested"]
            for p in FloatRange:
                itemname = n[0] + " (" + p + ")"
                url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}".format(itemname)
                responce = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                if str(responce) == "<Response [429]>":
                    for x in range(0, 20):
                        beepy.beep(1)
                    time.sleep(60)
                    responce = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                    pass
                if str(responce) == "<Response [502]>":
                    continue
                if str(responce) == "<Response [500]>":
                    continue
                if responce == None:
                    continue
                json = responce.json()
                if json['success'] == False:
                    Price = 10000
                elif 'median_price' not in json:
                    Price = str(json['lowest_price'].replace("$", ""))
                elif 'lowest_price' not in json:
                    Price = str(json['median_price'].replace("$", ""))
                else:
                    Price = str(json['median_price'].replace("$", ""))
                time.sleep(5)
                CurrentPrice = (float(Price), p)
                AllPrice[i][n][p] = float(Price)
                if CurrentPrice[0] < PrevPrice[i][p][1]:
                    PrevPrice[i][p][1] = CurrentPrice[0]
                    PrevPrice[i][p][0] = n
                elif CurrentPrice[0] > WorstPrice[i][p][1]:
                    WorstPrice[i][p][1] = CurrentPrice[0]
                    WorstPrice[i][p][0] = n
    for y in AllPrice: # Rarity
        if y == "Restricted":
            up = "Mil-Spec"
        elif y == "Classified":
            up = "Restricted"
        elif y == "Covert":
            up = "Classified"
        elif y == "Mil-Spec":
            continue
        for x in numpy.arange(0.01, 1.01, 0.01): # 100 times
            if 0 <= x <= 0.07:
                upfloat = "Factory New"
            elif 0.07 < x <= 0.15:
                upfloat = "Minimal Wear"
            elif 0.15 < x <= 0.37:
                upfloat = "Field-Tested"
            elif 0.37 < x <= 0.44:
                upfloat = "Well-Worn"
            elif 0.44 < x <= 1:
                upfloat = "Battle-Scarred"
            s = PrevPrice[up][upfloat]
            skin = s[0]
            Float = skin[1].split(":")
            FFloat = Float[0]
            SFloat = Float[1]
            if float(FFloat) <= x <= float(SFloat):
                LowPrice = s[1]
                i = 0
                for p in AllPrice[y]:
                    OFloat = p[1].split(":")
                    OFFloat = OFloat[0]
                    OSFloat = OFloat[1]
                    outputF = ((float(OSFloat) - float(OFFloat)) * x) + float(OFFloat)
                    if 0 <= outputF <= 0.07:
                        HighPrice = AllPrice[y][p]['Factory New']
                        wear = "Factory New"
                    elif 0.07 < outputF <= 0.15:
                        HighPrice = AllPrice[y][p]['Minimal Wear']
                        wear = "Minimal Wear"
                    elif 0.15 < outputF <= 0.37:
                        HighPrice = AllPrice[y][p]['Field-Tested']
                        wear = "Field-Tested"
                    elif 0.37 < outputF <= 0.44:
                        HighPrice = AllPrice[y][p]['Well-Worn']
                        wear = "Well-Worn"
                    elif 0.44 < outputF <= 1:
                        HighPrice = AllPrice[y][p]['Battle-Scarred']
                        wear = "Battle-Scarred"
                    if LowPrice * 10 < HighPrice * 0.85:
                        continue
                    else:
                        i = 1
                if i == 0:
                    print("Skin" + str(s[0][0]) + " At Price " + str(cad(LowPrice)) + " At Wear " + str(x))
                else:
                    print("NO")




