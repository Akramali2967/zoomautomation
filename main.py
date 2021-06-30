import pyautogui as pt
from time import sleep
import pyperclip
import webbrowser
import tkinter as tk
import os



def getmessage():
    position = pt.locateOnScreen("newsmile.PNG", confidence=.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, )
    pt.moveTo(x + 48, y - 41)
    pt.tripleClick()
    pt.hotkey("ctrl", "c")
    message = pyperclip.paste()
    print(message)
    return message

def replydone():
    position = pt.locateOnScreen("newsmile.png", confidence=.5)
    x=position[0]
    y=position[1]
    pt.moveTo(x, y)
    pt.moveTo(x + 120, y + 30 )
    pt.click()
    pt.typewrite("Done", interval=.01)
    pt.typewrite("\n", interval=.01)

def connectaudio():
    position = pt.locateOnScreen("connect.png", confidence=.8)
    x=position[0]
    y=position[1]
    pt.moveTo(x +10, y +20)
    pt.click()
    sleep(3)
    pt.moveRel(12,20)
    checkmic = pt.locateOnScreen("mic.png", confidence=.9)
    if checkmic:
        pt.hotkey("alt", "a")
    else:
        return


def gocontact():
    position = pt.locateOnScreen("Your Friend Whatsapp Png", confidence=.6) //Update This before Running
    x = position[0]
    y = position[1]
    pt.moveTo(x + 10, y + 20)
    pt.click()


def checknew():
    while True:

        try:
            position = pt.locateOnScreen("Your Friend Whatsapp Png when he send you any new message", confidence=.7) //Update This Before Running
            if position is not None:
                os.startfile('c:\win')
                sleep(4)
                gocontact()
                sleep(3)
                message = getmessage()
                replydone()
                webbrowser.open(message)
                sleep(10)
                position3 = pt.locateOnScreen("leavejoin.PNG", confidence=.6)
                if position3 is not None:
                    x = position3[0]
                    y = position3[1]
                    pt.moveTo(x + 10, y + 20)
                    pt.click()
                sleep(20)
                connectaudio()
                sleep(.5)
        except(Exception):
            print("No New Message")

        sleep(2)


os.startfile('Located Your Whatapp File') //This is the location where i have installed WhatsApp Ex- C:\whatsapp
sleep(15)
webbrowser.open("www.google.com")
checknew()




