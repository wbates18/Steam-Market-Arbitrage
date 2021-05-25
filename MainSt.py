import requests
import time
import numpy
import os
import beepy
PriceVar = 0

responce1 = requests.get("https://v6.exchangerate-api.com/v6/a4ddeb3abd17d84802e2007d/latest/USD")
CadConst = responce1.json()
print(CadConst)
CadConst = CadConst['conversion_rates']['CAD']

def cad(usd):
    cad = float(usd) * float(CadConst)
    cad = round(cad, 2)
    return cad



StatrakConst = "StatTrak%E2%84%A2"

with open("AllSkins.txt", "r") as Skins:
    r = Skins.readlines()
    Skins.close()

with open("ProfitFileST.txt", "w") as Profit:
    Profit.write("")
    Profit.close()

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
                time.sleep(3.2)
                itemname = StatrakConst + " " + n[0] + " (" + p + ")"
                url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}".format(itemname)
                responce = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                while str(responce) == "<Response [429]>":
                    for x in range(20):
                        beepy.beep(1)
                    time.sleep(10)
                    print("Disconnecting from vpn")
                    os.system("nordvpn d")
                    time.sleep(2)
                    print("connecting to different vpn")
                    os.system("nordvpn c") # For Linux only. VPN needs to be changed manually on mac and windows
                    time.sleep(10)
                    responce = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                    print(responce)
                    print("vpn change success if above is 200")
                if str(responce) == "<Response [502]>":
                    continue
                if str(responce) == "<Response [500]>":
                    continue
                if responce == None:
                    continue
                try:
                    json = responce.json()
                except:
                    Price = 10000
                    continue
                if str(json) == "{'success': True}":
                    continue
                elif 'median_price' not in str(json):
                    Price = str(json['lowest_price'].replace("$", ""))
                elif 'lowest_price' not in str(json):
                    Price = str(json['median_price'].replace("$", ""))
                else:
                    lowest = str(json['lowest_price'].replace("$", ""))
                    median = str(json['median_price'].replace("$", ""))
                    if ',' in str(median):
                        median = median.replace(",", "")
                    if "," in str(lowest):
                        lowest = lowest.replace(",", "")
                    if float(lowest) >= float(median):
                        Price = float(lowest)
                    else:
                        Price = float(median) 
                if "," in str(Price):
                    Price = cad(Price.replace(",", ""))
                else:
                    Price = cad(Price)
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
        o = 0
        for x in numpy.arange(0.01, 1.01, 0.01): # 100 times
            x = round(x, 2)
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
            if PrevPrice[up][upfloat][1] != 10000 and PrevPrice[up][upfloat][1] != 0:
                s = PrevPrice[up][upfloat]
            else:
                continue
            skin = s[0]
            Float = skin[1].split(":")
            FFloat = Float[0]
            SFloat = Float[1]
            if float(FFloat) <= x <= float(SFloat):
                i = 0
                CurrentLowest = [100000, ""]
                if o == 0:
                    currentskin = [str(s[0][0]), 0, 0]
                    LowPrice = s[1]
                    o = 1
                AllSkinList = []
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
                    if ((LowPrice * 10) + PriceVar) < (HighPrice * 0.85):
                        if HighPrice * 0.85 < CurrentLowest[0]:
                            CurrentLowest[0] = HighPrice * 0.85
                            CurrentLowest[1] = p
                        AllSkinList.append(p)
                        continue
                    else:
                        i = 1
                if i == 0:
                    if currentskin[0] == str(s[0][0]) or currentskin[0] == "":
                        continue
                    else:
                        print(AllSkinList)
                        currentskin[2] = (x - 0.01)
                        ProfitA = open("ProfitFileST.txt", "a")
                        ProfitA.write(str(currentskin[0]) + " - " + str(LowPrice) + " - " + str(currentskin[1]) + ":" + str(currentskin[2]) + " - " + str(AllSkinList) + "\n")
                        ProfitA.close()
                        print(str(currentskin[0]) + " At Price " + str(LowPrice) + " At Wears " + str(currentskin[1]) + "-" + str(currentskin[2]))
                        currentskin[1] = x
                        LowPrice = s[1]
                        currentskin[0] = str(s[0][0])
