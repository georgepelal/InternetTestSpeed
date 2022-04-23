
import ITS_Functions
from termcolor  import cprint


ITS_Functions.clear()

cprint("                                                         WELCOME ",'green',attrs=['bold'])

ITS_Functions.internetspeed()


#after the program finishes for first time it asks if the user wants to re-run it
next2=(input("Press (Enter) to leave or (R) to re-run the test")).lower()
while next2=="r":
  ITS_Functions.clear()
  ITS_Functions.internetspeed()
  next2=(input("Press (Enter) to leave or (R) to re-run the test")).lower()





                # CODE FOR THE .bat  FILE(converted to exe)
  #@echo off
  #pip install termcolor
  #pip install speedtest-cli
  #pip install pyinstaller
  #start ITS_Main.py
  #exit