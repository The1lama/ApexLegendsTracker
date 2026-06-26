
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

class apex_news_class:
    def __init__(self) -> None:
        self.title = None
        self.short_desc = None
        self.link = None
        self.img_link = None

def PlayerStatistics(uid, platform):
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

    cpc = apex_player_statistics_class()

    cpc.PlayerName = PlayerName
    cpc.Platform = Platform
    cpc.Level = Level
    cpc.Current_rank_br = Current_rank_br
    cpc.Current_rank_arena = Current_rank_arena
    cpc.Prestige = Prestige
    cpc.TotKills = TotBrKills
    cpc.TotDamage = TotBrDamage
    return cpc

def apexNews(intnews=3): # done
    url = f'https://api.mozambiquehe.re/news?auth={YOUR_API_KEY}'
    r = requests.get(url).json()
    listOfNews = []
    if intnews <= len(r):   # if intnews is equals or less than number of items in the list 
        print()
    else:
        intnews = 1

    for numNews in range(intnews):  # adds every news class to list and returns
        news = apex_news_class()
        listOfNews.append(news)

        news.title = r[numNews]['title']
        news.short_desc = r[numNews]['short_desc']
        news.link = r[numNews]['link']
        news.img_link = r[numNews]['img']
    return listOfNews

def name2uuid(gt, platform): # gets player UID
    url = f'https://api.mozambiquehe.re/nametouid?auth={YOUR_API_KEY}&player={gt}&platform={platform}'
    r = requests.get(url).json()
    return r['uid']
