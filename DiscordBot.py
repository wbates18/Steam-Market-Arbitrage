# Discord bot gets data from all the files from the python scripts
# sends links to discord server
import pyshorteners
import os
import discord
from urllib.parse import quote

os.environ['TOKEN'] = ""
client = discord.Client()  # sets up tokens and client
access = pyshorteners.Shortener(api_key='')


def PrintResults(changeline):  # uses params of the line that is outputed
    changeline[3] = changeline[3].strip("'")
    allUpSkins = changeline[3]
    res = allUpSkins.strip('][').split(', ')
    print(res)
    SkinList = []
    for i in range(0, len(res)):
        if (i % 2) == 0:
            print(res[i])
            SkinList.append(eval((str(res[i]) + ", " + str(res[i + 1]))))  # string formatting, seperating wear, price, and skin
    AllList = []
    print(SkinList)
    Namelist = []
    for x in SkinList:
        Skin = x.split(", ")
        print(Skin)
        FloatRange = []
        Float = Skin[1].split(":")
        FFloat = Float[0]
        SFloat = Float[1]
        if 0 <= float(FFloat) <= 0.07:  # getting floats and ranges
            FFloat = "Factory New"
        elif 0.07 < float(FFloat) <= 0.15:
            FFloat = "Minimal Wear"
        elif 0.15 < float(FFloat) <= 0.37:
            FFloat = "Field-Tested"
        elif 0.37 < float(FFloat) <= 0.44:
             FFloat = "Well-Worn"
        elif 0.44 < float(FFloat) <= 1:
            FFloat = "Battle-Scarred"

        if 0 <= float(SFloat) <= 0.07:
            SFloat = "Factory New"
        elif 0.07 < float(SFloat) <= 0.15:
            SFloat = "Minimal Wear"
        elif 0.15 < float(SFloat) <= 0.37:
            SFloat = "Field-Tested"
        elif 0.37 < float(SFloat) <= 0.44:
            SFloat = "Well-Worn"
        elif 0.44 < float(SFloat) <= 1:
            SFloat = "Battle-Scarred"

        if FFloat == "Factory New" and SFloat == "Battle-Scarred":  # getting all wears in range
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
        for a in FloatRange:  # getting the links used to send to the discord server
            itemname = str(Skin[0]) + " (" + str(a) + ")"
            link = access.bitly.short(quote("https://steamcommunity.com/market/listings/730/{}".format(itemname), safe=":'/")) # encodes everything but : and /
            AllList.append(link)
            Namelist.append(str(Skin[0]) + " (" + str(a) + ")")
    FloatRange = []
    Float = changeline[2].split(":")
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
    for a in FloatRange: # getting base skin links
        link = quote(
            "https://steamcommunity.com/market/listings/730/{}".format(str(changeline[0]) + " (" + str(a) + ")"),
            safe=":'/")
        AllList.insert(0, link)
        Namelist.insert(0, str(changeline[0]) + " (" + str(a) + ")")  # inserting into name file, so it can show up with embeded link
    linkstring = ""
    linkstringbase = ""
    templine = str(changeline[0]).replace(" ", "%20")
    templine = templine.replace("|", "%7C")
    for l in AllList:  # setting all links into discord message
        if templine in l:
            linkstringbase = "[" + Namelist[AllList.index(l)] + "]" + "(" + str(l) + ")" + "\n" + linkstringbase
        else:
            linkstring = "[" + Namelist[AllList.index(l)] + "]" + "(" + str(l) + ")" + "\n" + linkstring
    embed = discord.Embed(title="Trade Up Found")
    embed.add_field(name="Base Skin x10", value=linkstringbase)
    embed.add_field(name="All Possibilities", value=linkstring)
    embed.add_field(name="Ping", value="@Willow#3736")  # returns embeded links with the name of the skin as what is displayed.
    return embed




@client.event
async def on_ready():  # when the bot starts, basically a while loop
    channel = client.get_channel(838897099440783370)  # channel it is set to be in.
    StLength = -1
    ColLength = -1
    RegLength = -1
    while True:
        ST = open("ProfitFileST.txt", 'r')
        Lines = ST.readlines()
        for line in Lines:
            if line != "\n":
                line_count = Lines.index(line)
                if StLength < line_count:  # if new line
                    StLength = line_count
                    print(line.strip("\n"))
                    line = line.strip("\n")
                    changeline = line.split(" - ")
                    embed = PrintResults(changeline)  # send info and get embeded links returned
                    await channel.send(embed=embed) # send embed ----- SAME BELOW, just has to be different because they are all independent.
        Col = open("ProfitFileCL.txt", 'r')
        Lines1 = Col.readlines()
        for line1 in Lines1:
            if line1 != "\n":
                line_count1 = Lines1.index(line1)
                if ColLength < line_count1:
                    ColLength = line_count1
                    print(line1.strip("\n"))
                    line1 = line1.strip("\n")
                    changeline = line1.split(" - ")
                    embed = PrintResults(changeline)
                    await channel.send(embed=embed)
        Reg = open("ProfitFile.txt", 'r')
        Lines2 = Reg.readlines()
        for line2 in Lines2:
            if line2 != "\n":
                line_count2 = Lines2.index(line2)
                if RegLength < line_count2:
                    RegLength = line_count2
                    print(line2.strip("\n"))
                    line2 = line2.strip("\n")
                    changeline = line2.split(" - ")
                    embed = PrintResults(changeline)
                    await channel.send(embed=embed)





client.run(os.getenv('TOKEN'))

