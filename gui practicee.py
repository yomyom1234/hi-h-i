from tkinter import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def ent_p():
    a = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
    url += a
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div",attrs = {"class","win_result"}).get_text()
    txt = txt.split("\n")
    num_list = txt[7:13]
    bonus = txt[-4]
    print("당첨번호는 {} 보너스는 {}".format(num_list, bonus))

win = Tk() 
win.geometry("500x500")
win.option_add("*Font","고딕 20")
win.configure(bg="#9BE7F9")
ent = Entry(win)
ent.pack()





btn = Button(win)
btn.config(text = "lotto check")
btn.config(command=ent_p )
btn.pack()



win.mainloop()