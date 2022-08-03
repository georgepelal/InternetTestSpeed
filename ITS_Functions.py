#create a function to clear the output screen
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')



from datetime import datetime
import speedtest
import socket
from termcolor import cprint
from random import randint



def internetspeed():

#prints the IP adress
    cprint(f"                                                 Yor IP is : {socket.gethostbyname(socket.gethostname())}","cyan")
    print("                                             Measuring your internet speed...")


    wifi  = speedtest.Speedtest()

    #print the download speed
    downspeed=round((wifi.download() /1000000),2)
    cprint(f"                                        Your internet Download Speed is: {downspeed} Mb/s",'green')

    #print the upload speed
    upspeed=round((wifi.upload() / 1000000),2)
    cprint(f"                                         Your internet Upload Speed is: {upspeed} Mb/s","magenta")



#writes the results on a text file that is being used like a data base in order to remember history
    Speed_History=open('Speed_History.txt',"a") 

    Speed_History.write(f"\n  {datetime.now()} : Download Speed={downspeed} Mb/s , Upload Speed={upspeed} Mb/s")

    Speed_History.close()


    #prints the text file containing the history log
    next=(input("Do you want to display your history?(Y/N)")).lower()
    while next!="y" and next!="n":
        next=(input("Please select 'Y' for yes or 'N' for no .Do you want to display your history?(Y/N)")).lower()
        
    if next =="y":

        Speed_History=open('Speed_History.txt',"r") 
        #creates a list that each component is a line of the text file
        hist_lines=Speed_History.readlines()
        hist_lines.pop(0)#removes words that are not needed


        #prints each list component
        for i in range(len(hist_lines)):
            randomnum=randint(0,5)
            if randomnum==0:
                color="magenta"
            elif randomnum==1:
                color="red"
            elif randomnum==2:
                color="blue"
            elif randomnum==3:
                color="green"
            elif randomnum==4:
                color="yellow"
            elif randomnum==5:
                color="cyan"
                
            cprint(f"{hist_lines[i]}",color)

        Speed_History.close()   
