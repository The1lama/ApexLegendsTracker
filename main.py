
from time import sleep
import requests
from Secrets_ import YOUR_API_KEY

class apex_player_statistics_class:
    def __init__(self) -> None:
        self.PlayerName = None
        self.Platform = None
        self.Level = None
        self.Current_rank_br = None
        self.Current_rank_arena = None
        self.Prestige = None

        self.TotKills = None
        self.TotDamage = None
        self.TotKills = None

class apex_character_Class:
    def __init__(self) -> None:
        self.legend = None   # wich legend
        self.tracker = []   # list trackers and its value
        self.badges = []    # lists legends equiped badges

    def witch_legend(self):
        print(f'\t{self.legend}')

    def list_trackers(self):
        print('\tTrackers')
        for i in self.tracker:
            print(i)

    def list_badges(self):
        print('\tBadges')
        for i in self.badges:
            print(i)

class apex_news_class:
    def __init__(self) -> None:
        self.title = None
        self.short_desc = None
        self.link = None
        self.img_link = None

class apex_map_class:
    def __init__(self) -> None:
        self.mode = None
        self.cmap = None   # Current Map name
        self.etime = None  # End time
        self.nmap = None   # Next Map name
        self.stime = None  # Start time

class apex_crafting_class:
    def __init__(self) -> None:
        self.bundle = None
        self.cost = None   # Current Map name
        self.name = None  # End time
        self.rarity = None   # Next Map name
        self.asset = None  # Start time

def Charater_bage_trackers(r, legendsList):
    cclist = []

    for legend in legendsList:
        cc = apex_character_Class()   # cc == character Class
        cclist.append(cc)

        legendInfo = r['legends']['all'][legend]

        cc.legend = legend

        try:
            for data in legendInfo['data']:
                name = data['name']
                value = data['value']
                combo = f'{name}: {value}'
                cc.tracker.append(combo)
        except:
            cc.tracker.append('Could not retrive trackers.')  # if it does not find any trackes it uses this string

        try:
            for data in legendInfo['gameInfo']['badges']:
                name = data['name']
                cc.badges.append(name)
        except:
            cc.badges.append('Could not retrive badges.')   # if it does not find any badges it uses this string 

    return cclist

def PlayerStatistics(uid, platform):
    legendsList = []
    playerlist = []

    url = f'https://api.mozambiquehe.re/bridge?auth={YOUR_API_KEY}&uid={uid}&platform={platform}'
    parmas = {
        'merge': 'true',
        'removeMerged': 'true'
    }
    r = requests.get(url, params=parmas).json()

    PlayerName = str(r['global']['name'])   # gets players gamer tag
    Platform = str(r['global']['platform']) # gets players platform of choice
    Level = str(r['global']['level'])       # gets account level
    Current_rank_br = f"{str(r['global']['rank']['rankName'])} {str(r['global']['rank']['rankDiv'])}"   # gets BR rank and devition
    Current_rank_arena = f"{str(r['global']['arena']['rankName'])} {str(r['global']['arena']['rankDiv'])}"    # gets Arena rank and devition
    Prestige = str(r['global']['levelPrestige'])    # gets prestige level


    TotBrKills = str(r['total']['kills']['value'])    # gets total Br Kills that is recorded
    TotBrDamage = str(r['total']['damage']['value'])  # gets total Br Damage that is recoreded

    for key, value in r['legends']['all'].items():
        if key != 'Global':
            legendsList.append(key)

    cpc = apex_player_statistics_class()

    cpc.PlayerName = PlayerName
    cpc.Platform = Platform
    cpc.Level = Level
    cpc.Current_rank_br = Current_rank_br
    cpc.Current_rank_arena = Current_rank_arena
    cpc.Prestige = Prestige

    cpc.TotKills = TotBrKills
    cpc.TotDamage = TotBrDamage

    cclist = Charater_bage_trackers(r, legendsList)

    playerStatisticsPrint(cpc, cclist)

def playerStatisticsPrint(cpc, cclist):
    legendsList = []
    while True:
        for i in cclist:
            print(f'*{i.legend}')
            legendsList.append(i.legend)
        print('*All\n*Player\n*Exit')
        infoQ = input('What stastistic do you want to get?\n>> ')

        if infoQ in legendsList or infoQ == 'All' or infoQ =='Player':
            print('====================================\n')
            if infoQ in legendsList:
                for x in cclist:
                    if infoQ == x.legend:
                        x.witch_legend()
                        x.list_trackers()
                        x.list_badges()
                break

            elif infoQ =='Player':
                print(f'Game Tag: {cpc.PlayerName}')
                print(f'Platform: {cpc.Platform}')
                print(f'Level: {cpc.Level}')
                print(f'Current BR rank: {cpc.Current_rank_br}')
                print(f'Current Arena rank: {cpc.Current_rank_arena}')
                print(f'Prestige Level: {cpc.Prestige}')
                print(f'Total BR Kills: {cpc.TotKills}')
                print(f'Total BR Damage: {cpc.TotDamage}')
                print()
                break

            elif infoQ == 'All':
                print(f'Game Tag: {cpc.PlayerName}')
                print(f'Platform: {cpc.Platform}')
                print(f'Level: {cpc.Level}')
                print(f'Current BR rank: {cpc.Current_rank_br}')
                print(f'Current Arena rank: {cpc.Current_rank_arena}')
                print(f'Prestige Level: {cpc.Prestige}')
                print(f'Total BR Kills: {cpc.TotKills}')
                print(f'Total BR Damage: {cpc.TotDamage}')
                print()

                for x in cclist:
                    x.witch_legend()
                    x.list_trackers()
                    x.list_badges()
                    print()
                break

        elif infoQ == 'Exit':
            break

        else:
            print('\nType out how it looks on the screen without the star!!\n')
            sleep(2)

def apexNews(): # done
    url = f'https://api.mozambiquehe.re/news?auth={YOUR_API_KEY}'
    r = requests.get(url).json()
    listOfNews = []
    while True: # chooses the number of news articles to see and if more than max repeat
        intnews = int(input(f'How many news articels do you want to watch? Max {len(r)}\n>> '))
        if intnews <= len(r):
            print()
            break

    for numNews in range(intnews):
        news = apex_news_class()
        listOfNews.append(news)

        news.title = r[numNews]['title']
        news.short_desc = r[numNews]['short_desc']
        news.link = r[numNews]['link']
        news.img_link = r[numNews]['img']

    for x in listOfNews:
        print(f'''  **{x.title}**
{x.short_desc}
{x.link}
''')

def apexMapRotation(): # done
    url = f'https://api.mozambiquehe.re/maprotation?auth={YOUR_API_KEY}'
    parmas = {
        'version': 2
    }
    r = requests.get(url, params=parmas).json()

    MapModeList = []

    for key, value in r.items():    # loops throue every mode and gets current and the next map rotation
        modeInfo = apex_map_class()
        MapModeList.append(modeInfo)    # adds 2 list
        modeInfo.mode = key # gives the current mode

        # current map
        modeInfo.cmap = r[key]['current']['map']    # map name
        modeInfo.etime = r[key]['current']['readableDate_end']  # end time

        # next map 
        modeInfo.nmap = r[key]['next']['map']   # map name
        modeInfo.stime = r[key]['next']['readableDate_start']   # start time

    for x in MapModeList:   # prints info
        print(f'''  *{x.mode}*
Current map =>\t{x.cmap}\tEnds at {x.etime} UTC
  Next  map =>\t{x.nmap}\tStarts at {x.stime} UTC
''')

def apexCrafting(): # done
    url = f'https://api.mozambiquehe.re/crafting?auth={YOUR_API_KEY}'
    r = requests.get(url).json()

    craftingList = []   

    for item in r:
        for itemname in item['bundleContent']:  # what items in bundel
            cc = apex_crafting_class()  # cc == crafting class
            craftingList.append(cc)

            cc.bundle = item['bundleType']  # gets the bundelType, daily, weekly, permanent, weapon

            cc.cost = itemname['cost']  # the cost of the item
            cc.name = itemname['itemType']['name']  # the name of the item
            cc.rarity = itemname['itemType']['rarity']  # the rarity of the item
            cc.asset = itemname['itemType']['asset']    # the img link of the item


    printed_list = []
    for x in craftingList:
        if not x.name in printed_list: 
            printed_list.append(x.name)
            print(f'''  Bundel: {x.bundle}
Item: {x.rarity} {x.name}
Cost: {x.cost}
''')

def main():
    while True:
        print('====================================')
        which_info = input('''What information do you want
    [1] Player Info
    [2] Apex News
    [3] Map Rotation
    [4] Crafting Rotation
    [0] End Program
    >> ''')
        print('====================================')
        if which_info == '1':
            gt = input('Give the Gamer tag\n>> ')
            while True:
                platform_question = input('Give the Platform you play on: PC, Xbox, Playstation, *BLANK*(PC)\n>> ').upper().replace(' ','')
                print('====================================')
                if platform_question == 'PC' or platform_question == '':
                    uid = name2uuid(gt, 'PC')
                    PlayerStatistics(uid, 'PC')
                    break

                if platform_question == 'XBOX':
                    uid = name2uuid(gt, 'X1')
                    PlayerStatistics(uid, 'X1')
                    break

                if platform_question == 'PLAYSTATION':
                    uid = name2uuid(gt, 'PS4')
                    PlayerStatistics(uid, 'PS4')
                    break

        elif which_info == '2':
            apexNews()

        elif which_info == '3':
            apexMapRotation()

        elif which_info == '4':
            apexCrafting()

        elif which_info == '0':
            break

def name2uuid(gt, platform): # gets player UID
    url = f'https://api.mozambiquehe.re/nametouid?auth={YOUR_API_KEY}&player={gt}&platform={platform}'
    r = requests.get(url).json()
    return r['uid']

def apexStore(): # Currently have no access
    url = f'https://api.mozambiquehe.re/store?auth={YOUR_API_KEY}'
    r = requests.get(url).json()
    print(r)

if __name__ == '__main__':
    main()
