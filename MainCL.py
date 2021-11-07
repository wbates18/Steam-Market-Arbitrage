#Comments for all python files in MainSt.py
import requests
import time
import numpy
import os
PriceVar = 0

responce = requests.get("https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey=1b936271ddaf83ca1429")
CadConst = responce.json()
CadConst = CadConst['USD_CAD']

def cad(usd):
    cad = float(usd) * float(CadConst)
    cad = round(cad, 2)
    return cad



StatrakConst = "StatTrak%E2%84%A2"

with open("AllSkins.txt", "r") as Skins:
    r = Skins.readlines()
    Skins.close()

with open("ProfitFileCL.txt", "w") as Profit:
    Profit.write("")
    Profit.close()

Co = {}
C = {}
R = {}
M = {}
Co = {}
In = {}
CaseList = []
i = 0
y = 0
for x in r:
    if "?Cases" in x:
        continue

    if "?Collections" in x:
        i = 1
        Cases = {}
        y = 0

    if '!' in x:
        if i == 1:
            Case = x.replace("\n", "")
            Case = Case.replace("!", "")
            Cases[Case] = {"Consumer": [], "Industrial": [], "Mil-Spec": [], "Restricted": [], "Classified": [], "Covert": []}
            TempCase = Case
            CaseList.append(Case)
            Co[TempCase] = 0
            C[TempCase] = 0
            R[TempCase] = 0
            M[TempCase] = 0
            In[TempCase] = 0
            Co[TempCase] = 0
            y = 1
            continue

    if y == 1:
        if "Consumer" in x:
            Rarity = "Consumer"
            if Co[TempCase] != 1:
                Cases[TempCase][Rarity] = []
                Co[TempCase] = 1
        if "Industrial" in x:
            Rarity = "Industrial"
            if In[TempCase] != 1:
                Cases[TempCase][Rarity] = []
                In[TempCase] = 1
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
                itemname = n[0] + " (" + p + ")"
                url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}".format(itemname)
                responce = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                while str(responce) == "<Response [429]>":
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
                # if 'volume' in str(json):
                #     if "," in str(json['volume']):
                #         volume = str(json['volume'].replace(",", ""))
                #     else:
                #         volume = json['volume']
                #     print(itemname)
                #     print(json)          COMMENTED OUT BECAUSE OF NON MATCHING DATA TO MARKET
                #     print(volume)
                #     if int(volume) <= 7:
                #         continue
                #     else:
                #         pass
                # else:
                #     continue
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
        o = 0
        if y == "Restricted":
            up = "Mil-Spec"
        elif y == "Classified":
            up = "Restricted"
        elif y == "Covert":
            if str(AllPrice[y]) == '{}':
                continue
            else:
                up = "Classified"
        elif y == "Mil-Spec":
            up = "Industrial"
        elif y == "Industrial":
            up = "Consumer"
        elif y == "Consumer":
            continue
        for x in numpy.arange(0.01, 1.01, 0.01):  # 100 times  # Wears go from 0-1, 0.01 accuracy.
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
                s = PrevPrice[up][upfloat]  # skin of cheapest price per rarity per wear
            else:
                continue
            skin = s[0]
            Float = skin[1].split(":")
            FFloat = Float[0]
            SFloat = Float[1]
            if float(FFloat) <= x <= float(SFloat):  # getting float and if it is in the range.
                i = 0
                CurrentLowest = [100000, ""]
                if o == 0:
                    currentskin = [str(s[0][0]), 0, 0]  # current skin gets set for easy output
                    LowPrice = s[1]
                    o = 1
                AllSkinList = []
                for p in AllPrice[
                    y]:  # for skin in output rarity. They all have to be more expensive than input skins or else it isn't 100% profit.
                    OFloat = p[1].split(":")
                    OFFloat = OFloat[0]
                    OSFloat = OFloat[1]
                    outputF = ((float(OSFloat) - float(OFFloat)) * x) + float(
                        OFFloat)  # Trade Up Algorithm. Output float = highest output float range - lowest output float range * float + lowest.
                    if 0 <= outputF <= 0.07:  # getting wears and prices
                        HighPrice = AllPrice[y][p]['Factory New']
                        wear = "Factory New"
                        skin1 = (p[0] + "," + " 0:0.07")
                    elif 0.07 < outputF <= 0.15:
                        HighPrice = AllPrice[y][p]['Minimal Wear']
                        wear = "Minimal Wear"
                        skin1 = (p[0] + "," + " 0.08:0.15")
                    elif 0.15 < outputF <= 0.37:
                        HighPrice = AllPrice[y][p]['Field-Tested']
                        wear = "Field-Tested"
                        skin1 = (p[0] + "," + " 0.16:0.38")
                    elif 0.37 < outputF <= 0.44:
                        HighPrice = AllPrice[y][p]['Well-Worn']
                        wear = "Well-Worn"
                        skin1 = (p[0] + "," + " 0.39:0.45")
                    elif 0.44 < outputF <= 1:
                        HighPrice = AllPrice[y][p]['Battle-Scarred']
                        wear = "Battle-Scarred"
                        skin1 = (p[0] + "," + " 0.46:1")
                    if ((LowPrice * 10) + PriceVar) < (HighPrice * 0.85):  # if the skin works
                        if HighPrice * 0.85 < CurrentLowest[0]:
                            CurrentLowest[0] = HighPrice * 0.85
                            CurrentLowest[1] = p
                        AllSkinList.append(skin1)
                        continue
                    else:  # it doesn't work, so the whole rarity is not profit.
                        i = 1
                if i == 0:  # if that rarity works
                    if currentskin[0] == str(s[0][0]) or currentskin[0] == "":  # if the rarity isn't done
                        continue
                    else:  # Append to text file and send to discord bot
                        currentskin[2] = (x - 0.01)
                        ProfitA = open("ProfitFileST.txt", "a")
                        ProfitA.write(
                            str(currentskin[0]) + " - " + str(LowPrice) + " - " + str(currentskin[1]) + ":" + str(
                                currentskin[2]) + " - " + str(AllSkinList) + "\n")
                        ProfitA.close()
                        print(str(currentskin[0]) + " At Price " + str(LowPrice) + " At Wears " + str(
                            currentskin[1]) + "-" + str(currentskin[2]))
                        currentskin[1] = x
                        LowPrice = s[1]
                        currentskin[0] = str(s[0][0])

