# MainST and Main are basically the same, just executed after one another.
# MainST will have the comments
# most of MainCL is the same, but I will comment the differences in there.




# In these files there are 3 steps: Formatting the text file for use, fetching the current prices,
# and analyising the prices and sending the data to the discord bot.
import requests
import time
import numpy  # Importing all packages
import os
PriceVar = 0

# getting currency converter data
responce1 = requests.get("https://v6.exchangerate-api.com/v6/a4ddeb3abd17d84802e2007d/latest/USD")
CadConst = responce1.json()
print(CadConst)
CadConst = CadConst['conversion_rates']['CAD']

def cad(usd): # Function for using data from above ^
    cad = float(usd) * float(CadConst)
    cad = round(cad, 2)
    return cad



StatrakConst = "StatTrak%E2%84%A2"  # String to append to fetch request. This is the difference between MainST and Main

with open("AllSkins.txt", "r") as Skins:
    r = Skins.readlines()
    Skins.close()  # Reading all the skins

with open("ProfitFileST.txt", "w") as Profit:
    Profit.write("")  # Reseting text file
    Profit.close()

Co = {}
C = {}
R = {}
M = {}
CaseList = []
# This block formats the text file for use
# r is all the lines in the file, and the start of a dataset starts with a ?. We are only looking at cases
# in this file, so after cases, it breaks.
# Then for every case it appends it to a list and creates a dictionary to hold all of the rarities.
for x in r:
    if "?Cases" in x:
        Cases = {}
        y = 0

    if "?Collections" in x:
        break

    if '!' in x:
        Case = x.replace("\n", "")
        Case = Case.replace("!", "")
        Cases[Case] = {}  # dictionary being created.
        TempCase = Case
        CaseList.append(Case)  # Creating list
        Co[TempCase] = 0
        C[TempCase] = 0
        R[TempCase] = 0
        M[TempCase] = 0
        y = 1

    elif y == 1:  # All the rarities and skins being sorted into the dictionary.
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
        Float = Float1[2].replace("\n", "")  # seperating the floats from the skin and appending them into a tuple next to the skin.
        Skin = Float1[0]
        SkinF = (Skin, Float)
        Cases[TempCase][Rarity].append(SkinF)

CaseListConfirm = []  # This next part is fetching the prices. We have already formatted all of the data at this point.
for a in CaseList: # Case
    print(a)
    PrevPrice = {}
    WorstPrice = {}
    AllPrice = {}
    for i in Cases[a]: # Rarity
        AllPrice[i] = {}
        WorstPrice[i] = {'Factory New': ["", 0], 'Minimal Wear': ["", 0], 'Field-Tested': ["", 0], 'Well-Worn': ["", 0], 'Battle-Scarred': ["", 0]}  # Setting default prices in dicts.
        PrevPrice[i] = {'Factory New': ["", 10000], 'Minimal Wear': ["", 10000], 'Field-Tested': ["", 10000], 'Well-Worn': ["", 10000], 'Battle-Scarred': ["", 10000]}
        for n in Cases[a][i]: # For every skin
            AllPrice[i][n] = {'Factory New': 0, 'Minimal Wear': 0, 'Field-Tested': 0, 'Well-Worn': 0, 'Battle-Scarred': 0}
            FloatRange = []
            Float = n[1].split(":")  # Getting float range
            FFloat = Float[0]
            SFloat = Float[1]
            if 0 <= float(FFloat) <= 0.07:  # Getting start and end wears
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
            if FFloat == "Factory New" and SFloat == "Battle-Scarred":  # Getting range and putting it into list
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
            for p in FloatRange:  # Fetching each wear in skin
                time.sleep(3.2)
                itemname = StatrakConst + " " + n[0] + " (" + p + ")"  # This has StatrakConst in only MainSt.
                url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={}".format(itemname)
                responce = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})  # Getting request from market
                while str(responce) == "<Response [429]>":  # If it 429 errors (Too many requests), change the vpn to get around it.
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
                if str(responce) == "<Response [502]>":  # Other errors, sometimes happens if none in stock, just continue
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
                elif 'median_price' not in str(json):  # Get median price if possible, else get lowest
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
                    if float(lowest) >= float(median):  # string formatting.
                        Price = float(lowest)
                    else:
                        Price = float(median) 
                if "," in str(Price):
                    Price = cad(Price.replace(",", ""))
                else:
                    Price = cad(Price)
                CurrentPrice = (float(Price), p)  # Getting lowest price for each wear of each rarity.
                AllPrice[i][n][p] = float(Price)
                if CurrentPrice[0] < PrevPrice[i][p][1]:
                    PrevPrice[i][p][1] = CurrentPrice[0]
                    PrevPrice[i][p][0] = n
                elif CurrentPrice[0] > WorstPrice[i][p][1]:
                    WorstPrice[i][p][1] = CurrentPrice[0]
                    WorstPrice[i][p][0] = n


    for y in AllPrice: # Last Step, analysing prices
        if y == "Restricted":  # Getting rarity and one below it.
            up = "Mil-Spec"
        elif y == "Classified":
            up = "Restricted"
        elif y == "Covert":
            up = "Classified"
        elif y == "Mil-Spec":
            continue
        o = 0
        for x in numpy.arange(0.01, 1.01, 0.01): # 100 times  # Wears go from 0-1, 0.01 accuracy.
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
                for p in AllPrice[y]:  # for skin in output rarity. They all have to be more expensive than input skins or else it isn't 100% profit.
                    OFloat = p[1].split(":")
                    OFFloat = OFloat[0]
                    OSFloat = OFloat[1]
                    outputF = ((float(OSFloat) - float(OFFloat)) * x) + float(OFFloat)  # Trade Up Algorithm. Output float = highest output float range - lowest output float range * float + lowest.
                    if 0 <= outputF <= 0.07:  # getting wears and prices
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
                    if ((LowPrice * 10) + PriceVar) < (HighPrice * 0.85):  # if the skin works
                        if HighPrice * 0.85 < CurrentLowest[0]:
                            CurrentLowest[0] = HighPrice * 0.85
                            CurrentLowest[1] = p
                        AllSkinList.append(p)
                        continue
                    else: # it doesn't work, so the whole rarity is not profit.
                        i = 1
                if i == 0: # if that rarity works
                    if currentskin[0] == str(s[0][0]) or currentskin[0] == "": # if the rarity isn't done
                        continue
                    else: # Append to text file and send to discord bot
                        print(AllSkinList)
                        currentskin[2] = (x - 0.01)
                        ProfitA = open("ProfitFileST.txt", "a")
                        ProfitA.write(str(currentskin[0]) + " - " + str(LowPrice) + " - " + str(currentskin[1]) + ":" + str(currentskin[2]) + " - " + str(AllSkinList) + "\n")
                        ProfitA.close()
                        print(str(currentskin[0]) + " At Price " + str(LowPrice) + " At Wears " + str(currentskin[1]) + "-" + str(currentskin[2]))
                        currentskin[1] = x
                        LowPrice = s[1]
                        currentskin[0] = str(s[0][0])
