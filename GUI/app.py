
from tkinter import *
from PIL import Image, ImageTk
import ApexLegends as Al    # import functions from ApexLegends.py file to get info
import webbrowser
import tkinter as tk


class HomePage: # home page for the program
    def __init__(self, master):
        self.master = master

        master.title("Apex Legends")    # sets windows title
        master.geometry("350x350")  # size 
        master.resizable(False, False)  # if resizable

        self.frame = tk.Frame(self.master)

        image = Image.open(f"img/apexLegends.png")  # opens image for a logo
        image = image.resize((300,175))
        logo= ImageTk.PhotoImage(image, Image.ANTIALIAS)

        self.logoimg = Label(self.frame, 
                image=logo)
        self.logoimg.image = logo
        self.logoimg.pack() # packs image to show in window

        self.apex_News = tk.Button(self.frame, text='Apex News', width=25, command=self.apexNews).pack()    # creates a button for apexNews and if pressed opens new windows with the latest news

        self.apex_PlayerStats = tk.Button(self.frame, text='Player Statistics', width=25, command=self.playerStats).pack()  # creates a button for player statistics and if pressed opens player statisctics window

        self.exitButton = tk.Button(self.frame, text = 'Good Bye', width = 25, command=quit).pack() # create a button to close the program

        self.frame.pack()   # packs every thing to to windows to show up

    def playerStats(self):
        self.newWindow = tk.Toplevel(self.master)   # create a new window and places it on top
        self.app = PlayerStats(self.newWindow)  # runs PlayerStats class for the new window

    def apexNews(self):
        self.newWindow = tk.Toplevel(self.master)   # create a new window and places it on top
        self.app = News(self.newWindow) # runs PlayerStats class for the new window

class News:
    def __init__(self, master):
        self.master = master
        
        self.frame = tk.Frame(self.master)

        master.title("Apex News")   # sets windows title
        master.geometry("500x500")  # size
        master.resizable(False, False)  # if resizable

        self.T = Text(master=master, height=7, width=120)   # creats a box with 7 rows high and 120 characters width
        self.l1 = Label(master=master, text='Apex News', font=("Courier", 12)).pack()   # Creates a head line to window

        self.News = apex_news(1)    # runs apex_news function with one news story to get

        self.New1 = f'{self.News[0].title}\n\n{self.News[0].short_desc}\n\n{self.News[0].link}' # formats the text how it should look like

        self.openLinkButton = tk.Button(self.frame, text='Open Link', width=25, command=self.open_link).pack()  # when pressed button opens the news page in webbrowser 

        self.T.insert(tk.END, self.New1)    # insters the formated text to the box 
        self.T.pack()   # packs it

        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).pack() # to kill the window

        self.frame.pack()   # packs it

    def open_link(self):    # opens link
        webbrowser.open_new_tab(self.News[0].link)

    def close_windows(self):    # kills window
        self.master.destroy()

class PlayerStats:
    def __init__(self, master):
        self.master = master

        master.title("Player Statistic")    # sets windows title
        master.geometry("325x350")  # size
        master.resizable(False, False)  # if resizable


        # =============== Creates input for game tag and platform =====================

        self.gTagLable = Label(self.master,
                text="Gamer Tag").grid(row=0, column=0)
        self.platformLable = tk.Label(self.master,
                text="Platform").grid(row=1, column=0)
        self.platformChoises = tk.Label(self.master, 
                text="PC, XBOX, PLAYSTATION").grid(row=1, column=2)

        self.gt = tk.Entry(self.master)
        self.gt.grid(row=0, column=1)
        
        self.platform = tk.Entry(self.master)
        self.platform.grid(row=1, column=1)

        tk.Button(master, 
          text='Next', command=self.show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)  # when pressed it checks if the input fields is correct formated

        self.quitButton = tk.Button(self.master, text = 'Quit', width =4, command = self.close_windows).grid(row=3, column=1)   # kills window

    def close_windows(self):    # kills window
        self.master.destroy()

# https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
# https://www.geeksforgeeks.org/python-tkinter-text-widget/
    def show_entry_fields(self):    # checks if it is correctly formated input fields
        platformList = ['PC', 'XBOX', 'PLAYSTATION']
        platform = self.platform.get().upper()
        gtag = self.gt.get().replace(' ', '')

        if platform in platformList and gtag != '':
            self.clear_screen() # clears screen
            self.with_stats(gt=gtag, pform=platform) # Creats new wigets with player stats

    def with_stats(self, gt, pform):
        col = 2 # for easy movement ?
        row = 1 # for easy movement ?
        self.pstats = apex_player(gt=gt, platform=pform)    # gets playerStats

        image = Image.open("img/yourTheChampion.png")   # opens image for img in window
        image = image.resize((300,175))
        champion= ImageTk.PhotoImage(image, Image.ANTIALIAS)

        self.chaimpionImg = Label(self.master, 
                image=champion)
        self.chaimpionImg.image = champion
        self.chaimpionImg.grid(column=col, row=row-1)   # places image highest

        self.playerName = Label(self.master, 
                text=f"Player Name: {self.pstats.PlayerName}").grid(column=col, row=row)    # shows playerName in window

        self.Platforme = Label(self.master, 
                text=f"Platform: {self.pstats.Platform}").grid(column=col, row=row+1)    # shows platform in window

        self.PrestegeLevel = Label(self.master, 
                text=f"Prestige: {self.pstats.Prestige} Level: {self.pstats.Level}").grid(column=col, row=row+2)    # shows prestige and level in window

        self.rank = Label(self.master, 
                text=f"BR Rank: {self.pstats.Current_rank_br}").grid(column=col, row=row+3)    # shows current BR rank in window

        self.Totkill = Label(self.master, 
                text=f"Recorded Kills: {self.pstats.TotKills}").grid(column=col, row=row+4)    # shows total recorded kills in window

        self.TotDamage = Label(self.master, 
                text=f"Recorded Damage: {self.pstats.TotDamage}").grid(column=col, row=row+5)    # shows total recordead damage done in window

        self.quitButton = tk.Button(self.master, text = 'Quit', width = 25, command = self.close_windows)   # kills window
        self.quitButton.grid(column=col, row=row+6) # paces button in window

    def clear_screen(self): # clears windows from everything
        for child in self.master.winfo_children():
            child.destroy()

def apex_news(num: int):    # function to get the lates apex news
    return Al.apexNews(num)

def apex_player(gt, platform):  # function to get apex_player stats from another file
    uid = Al.name2uuid(gt=gt, platform=platform)
    playerStat = Al.PlayerStatistics(uid=uid, platform=platform)
    return playerStat   # returns a class

if __name__ == '__main__':  # starts program and runs HomePage Class for start screen
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
