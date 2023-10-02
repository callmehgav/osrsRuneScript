import time
import threading
import numpy as np
from pynput.mouse import Button as pyB, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller as C
import random
from time import sleep
from tkinter import *
delay = 0.001
everyMinute = 60
buttonLeftClick = pyB.left
buttonRightClick = pyB.right
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='+')

class ClickMouse(threading.Thread):

    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Started Clicking")
        self.running = True

    def stop_clicking(self):
        print("Stopped Clicking")
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
    def run(self):
        while self.program_running:
            while self.running:
            #cooking-------------------------------cooking
            #crafting-------------------------------crafting
            #firemaking-------------------------------firemaking
            #agility-------------------------------agility
            #woodcutting-------------------------------woodcutting
            #fletching-------------------------------fletching
            #mining-------------------------------mining
            #magic-------------------------------magic
            #range-------------------------------range
            #melee-------------------------------melee
            #multiUse-------------------------------multiUse
                quickRandomAutoClicker(self)
                #clickAndDropInv(self)
                #openPacks(self)
                #dropInventory(self)
                #quickAFRandomAutoClicker(self)
                #highAlch(self)
            #fishing-------------------------------fishing
            #thieving-------------------------------thieving
            #smithing-------------------------------smithing
            #construction-------------------------------construction

                time.sleep(self.delay)
            time.sleep(0.1)
################################################################
####################SUPPORT METHODS#############################
################################################################
def click(self):
    cm = ClickMouse()
    if self.running == True:
        cm.stop_clicking()
    else:
        cm.start_clicking()


keyboard = C()
mouse = Controller()
click_thread = ClickMouse(1, buttonLeftClick)
click_thread.start()


def on_press(key):
    print("Key pressed ", key)
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()

################################################################
####################SUPPORT METHODS#############################
################################################################
def tenPercentChanceOfE():
    # 10% chance of storing ore
    randPercent = np.random.randint(1, 101)
    if randPercent > 80:
        #rint('e clicked')
        keyboard.press('e')
        keyboard.release('e')

def returnInt (minInt, maxInt):
    return np.random.randint(minInt, maxInt)

def moveMouse(x,y):
    mouse.position = (x, y)

def randomInSquare(num):
    return returnInt(num, num+10)


def clickEsc(self):
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(random.uniform(.2,.4))
def clickSpace(self):
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(.2,.4))
################################################################
####################BOTS########################################
################################################################
def quickRandomAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(10,15)
    # tenPercentChanceOfE()
    time.sleep(delay)