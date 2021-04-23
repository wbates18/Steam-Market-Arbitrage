import requests
from currency_converter import CurrencyConverter
import time
import beepy
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

CaseListConfirm = []
for a in CaseList: # Case
    Pleasegodsavemefromthishellscape = {'FN': 0, 'MW': 0, 'FT': 0, 'WW': 0, "BS": 0}
    PrevPrice = {}
    AllPrice = {}
    for i in Cases[a]: # Rarity
        AllPrice[i] = {}
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
                                print(n[0])
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
                print(responce)
                if str(responce) == "<Response [429]>":
                    for x in range(0, 20):
                        beepy.beep(1)
                    time.sleep(60)
                    responce = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                    pass
                if str(responce) == "<Response [502]>":
                    pass
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
    leni = i
    for y in AllPrice: # Rarity
        if y == 'Restricted':
            up = 'Mil-Spec'
        elif y == 'Classified':
            up = 'Restricted'
        elif y == 'Covert':
            up = 'Classified'
        elif y == 'Mil-Spec':
            continue
        for s in AllPrice[y]:
            Float = s[1].split(":")
            FFloat = Float[0]
            SFloat = Float[1]
            if AllPrice[y][s]['Factory New'] != 0:
                avg = (0.07 - float(FFloat))/(float(SFloat) - float(FFloat))
                if 0 <= avg <= 0.07:
                    if (PrevPrice[up]['Factory New'][1] * 10) < (AllPrice[y][s]['Factory New'] * 0.85):
                        Pleasegodsavemefromthishellscape['FN'] += 1
                        if Pleasegodsavemefromthishellscape['FN'] == leni:
                            print('10x Factory New ' + str(PrevPrice[up]['Factory New'][0][0]) + ' Turns into 1 Factory New Skin From Case: ' + a)
                elif 0.07 < avg <= 0.15:
                    if (PrevPrice[up]['Minimal Wear'][1] * 10) < (AllPrice[y][s]['Factory New'] * 0.85):
                        Pleasegodsavemefromthishellscape['FN'] += 1
                        if Pleasegodsavemefromthishellscape['FN'] == leni:
                            print('10x Minimal Wear ' + str(PrevPrice[up]['Minimal Wear'][0][0]) + ' Turns into 1 Factory New Skin From Case: ' + a)
                elif 0.15 < avg <= 0.37:
                    if (PrevPrice[up]['Field-Tested'][1] * 10) < (AllPrice[y][s]['Factory New'] * 0.85):
                        Pleasegodsavemefromthishellscape['FN'] += 1
                        if Pleasegodsavemefromthishellscape['FN'] == leni:
                            print('10x Field-Tested ' + str(PrevPrice[up]['Field-Tested'][0][0]) + ' Turns into 1 Factory New Skin From Case: ' + a)
                elif 0.37 < avg <= 0.44:
                    if (PrevPrice[up]['Well-Worn'][1] * 10) < (AllPrice[y][s]['Factory New'] * 0.85):
                        Pleasegodsavemefromthishellscape['FN'] += 1
                        if Pleasegodsavemefromthishellscape['FN'] == leni:
                            print('10x Well-Worn ' + str(PrevPrice[up]['Well-Worn'][0][0]) + ' Turns into 1 Factory New Skin From Case: ' + a)
                elif 0.44 < avg <= 1:
                    if (PrevPrice[up]['Battle-Scarred'][1] * 10) < (AllPrice[y][s]['Factory New'] * 0.85):
                        Pleasegodsavemefromthishellscape['FN'] += 1
                        if Pleasegodsavemefromthishellscape['FN'] == len(AllPrice):
                            print('10x Battle-Scarred ' + str(PrevPrice[up]['Battle-Scarred'][0][0]) + ' Turns into 1 Factory New Skin From Case: ' + a)
            if AllPrice[y][s]['Minimal Wear'] != 0:
                avg = (0.15 - float(FFloat))/(float(SFloat) - float(FFloat))
                if 0.07 < avg <= 0.15:
                    if (PrevPrice[up]['Minimal Wear'][1] * 10) < (AllPrice[y][s]['Minimal Wear'] * 0.85):
                        Pleasegodsavemefromthishellscape['MW'] += 1
                        if Pleasegodsavemefromthishellscape['MW'] == leni:
                            print('10x Minimal Wear ' + str(PrevPrice[up]['Minimal Wear'][0][0]) + ' Turns into 1 Minimal Wear Skin From Case: ' + a)
                elif 0.15 < avg <= 0.37:
                    if (PrevPrice[up]['Field-Tested'][1] * 10) < (AllPrice[y][s]['Minimal Wear'] * 0.85):
                        Pleasegodsavemefromthishellscape['MW'] += 1
                        if Pleasegodsavemefromthishellscape['MW'] == leni:
                            print('10x Field-Tested ' + str(PrevPrice[up]['Field-Tested'][0][0]) + ' Turns into 1 Minimal Wear Skin From Case: ' + a)
                elif 0.37 < avg <= 0.44:
                    if (PrevPrice[up]['Well-Worn'][1] * 10) < (AllPrice[y][s]['Minimal Wear'] * 0.85):
                        Pleasegodsavemefromthishellscape['MW'] += 1
                        if Pleasegodsavemefromthishellscape['MW'] == leni:
                            print('10x Well-Worn ' + str(PrevPrice[up]['Well-Worn'][0][0]) + ' Turns into 1 Minimal Wear Skin From Case: ' + a)
                elif 0.44 < avg <= 1:
                    if (PrevPrice[up]['Battle-Scarred'][1] * 10) < (AllPrice[y][s]['Minimal Wear'] * 0.85):
                        Pleasegodsavemefromthishellscape['MW'] += 1
                        if Pleasegodsavemefromthishellscape['MW'] == leni:
                            print('10x Battle-Scarred ' + str(PrevPrice[up]['Battle-Scarred'][0][0]) + ' Turns into 1 Minimal Wear Skin From Case: ' + a)
            if AllPrice[y][s]['Field-Tested'] != 0:
                avg = (0.37 - float(FFloat))/(float(SFloat) - float(FFloat))
                if 0.15 < avg <= 0.37:
                    if (PrevPrice[up]['Field-Tested'][1] * 10) < (AllPrice[y][s]['Field-Tested'] * 0.85):
                        Pleasegodsavemefromthishellscape['FT'] += 1
                        if Pleasegodsavemefromthishellscape['FT'] == leni:
                            print('10x Field-Tested ' + str(PrevPrice[up]['Field-Tested'][0][0]) + ' Turns into 1 Field-Tested Skin From Case: ' + a)
                elif 0.37 < avg <= 0.44:
                    if (PrevPrice[up]['Well-Worn'][1] * 10) < (AllPrice[y][s]['Field-Tested'] * 0.85):
                        Pleasegodsavemefromthishellscape['FT'] += 1
                        if Pleasegodsavemefromthishellscape['FT'] == leni:
                            print('10x Well-Worn ' + str(PrevPrice[up]['Well-Worn'][0][0]) + ' Turns into 1 Field-Tested Skin From Case: ' + a)
                elif 0.44 < avg <= 1:
                    if (PrevPrice[up]['Battle-Scarred'][1] * 10) < (AllPrice[y][s]['Field-Tested'] * 0.85):
                        Pleasegodsavemefromthishellscape['FT'] += 1
                        if Pleasegodsavemefromthishellscape['FT'] == leni:
                            print('10x Battle-Scarred ' + str(PrevPrice[up]['Battle-Scarred'][0][0]) + ' Turns into 1 Field-Tested Skin From Case: ' + a)
            if AllPrice[y][s]['Well-Worn'] != 0:
                avg = (0.44 - float(FFloat))/(float(SFloat) - float(FFloat))
                if 0.37 < avg <= 0.44:
                    if (PrevPrice[up]['Well-Worn'][1] * 10) < (AllPrice[y][s]['Well-Worn'] * 0.85):
                        Pleasegodsavemefromthishellscape['WW'] += 1
                        if Pleasegodsavemefromthishellscape['WW'] == len(AllPrice):
                            print('10x Well-Worn ' + str(PrevPrice[up]['Well-Worn'][0][0]) + ' Turns into 1 Well-Worn Skin From Case: ' + a)
                elif 0.44 < avg <= 1:
                    if (PrevPrice[up]['Battle-Scarred'][1] * 10) < (AllPrice[y][s]['Well-Worn'] * 0.85):
                        Pleasegodsavemefromthishellscape['WW'] += 1
                        if Pleasegodsavemefromthishellscape['WW'] == leni:
                            print('10x Battle-Scarred ' + str(PrevPrice[up]['Battle-Scarred'][0][0]) + ' Turns into 1 Well-Worn Skin From Case: ' + a)
            if AllPrice[y][s]['Battle-Scarred'] != 0:
                avg = (1 - float(FFloat))/(float(SFloat) - float(FFloat))
                if 0.44 < avg <= 1:
                    if (PrevPrice[up]['Battle-Scarred'][1] * 10) < (AllPrice[y][s]['Battle-Scarred'] * 0.85):
                        Pleasegodsavemefromthishellscape['BS'] += 1
                        if Pleasegodsavemefromthishellscape['BS'] == leni:
                            print('10x Battle-Scarred ' + str(PrevPrice[up]['Battle-Scarred'][0][0]) + ' Turns into 1 Battle-Scarred Skin From Case: ' + a)
