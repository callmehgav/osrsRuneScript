import os
import time
import threading
import numpy as np
from pynput.mouse import Button as pyB, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller as C
import random
import sys
from time import sleep
from tkinter import *
#import pyautogui
everyMinute = 60
buttonLeftClick = pyB.left
buttonRightClick = pyB.right
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='+')
kill_key = KeyCode(char='-')

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

    def kill_clicking(self):
        print("kill Clicking")
        os._exit(1)
    def exit(self):
        self.stop_clicking()
        self.program_running = False
    def run(self):
        counter = 0
        while self.program_running:
            counter = 0
            while self.running:
                #if (counter < 215):
                    #counter = counter +1
                    #print(counter)
                #@@@@@@@@@@@@@@@@@@@@@
            #agility-------------------------------agility
                #canifisAgilCourse(self)
                #seersCourse(self)
                #rellekkaCourse(self)
                #colorTest(self)
                prifAgil(self)
                #prifAgilWithHA(self)
                #ardyCourse(self)
                #pixelRangeTest(self)

            #Herb-------------------------------herb
                #cleanHerbs(self)
                #makePots(self)
                #birdNest(self)
            #cooking-------------------------------cooking
                #catchNBankKarambwans(self)
                #hosidiousCookingBot(self)
            #construction-------------------------------construction
                #runPlanks(self)
                #toggleRun(self)
                #plankMake(self)
                #mythCapesWButler(self)
                #plankMakeSpell(self)
            #crafting-------------------------------crafting
                #cookSeaweedAtFT(self)
                #edgevilleFurnace(self)
                #edgevilleFurnace2Item(self)
                #craftOrFletch(self)
                #spinFlax(self)
                #lunarSpinFlax(self)
                #superGlassmake(self)
                #pickUpFromGround(self)
            #firemaking-------------------------------firemaking
                #burnInv(self)

            # Hunter-------------------------------Hunter
                #maniMonkeys(self)
                #mmDropInventory(self)
            #fletching-------------------------------fletching
                #broads(self)
                #teakCutNFletch(self)
                #craftOrFletch(self)
                #stringBows(self)
                #enchantBolts(self)
            #mining-------------------------------mining
                #quick60to120RandomAutoClicker(self)
                #threeTickMiningGranite(self)
                #mlmTopFloor(self)
                #mineSalts2(self)
                #mineIronOreAndBank(self)
                #mineSandstone(self)
                #iron(self)
                #mineSulfur(self)
                #miningCraftingBot(self)
                #shiloVillageSurfaceMine(self)
            #magic-------------------------------magic
                #(self, "saphire")

                #mageTrainingArenaGraveyard(self)
                #mageTrainingArenaEnchant(self)
            #range-------------------------------range
            #prayer-------------------------------prayer
                #wildyAlter(self)
            #melee-------------------------------melee
                #amaniteCrabs2(self)
                #amaniteCrabs3(self)

            #fishing-------------------------------fishing
                #counter = minnows(self,counter)
                #fishAndDropInv(self)
                #threeTickFish(self)
            #farming-------------------------------farming
                #titheFarm(self)
                #plantSapplings4kStreched(self)
                #plantSapplings(self)
            #thieving-------------------------------thieving
                #ardyKnights(self)
                #fruitStalls(self)
                #masterFarmerHouseLure(self)
                #masterFarmerGuild(self)
            #smithing-------------------------------smithing
                #walkingSteelBlastFurnace(self)
                #goldBlastFurnace(self)
                #BlastFurnaceForMithBars(self)
                #BlastFurnaceForAddyBars(self)
                #BlastFurnaceForSteelBars(self)
                #runCannonBalls(self)
                #varrockSmithing(self)
                #edgevilleFurnace(self)
                #buyBlastFurnaceOres(self)
                #drinkStam(self)
            #woodcutting-------3------------------------woodcutting
                #clickAndFletchIntoShafts(self)
                #clickAndFletchIntoBows(self)
                #cutFossilIslandTreesAndBank(self)
                #cutFossilIslandTest(self)
                #yewsAndBank(self)
            #multiUse-------------------------------multiUse
                #quick10through15RandomAutoClicker(self)
                #cannonAutoClicker(self)
                #cannonAutoClicker(self)
                #emptyInventoryInBank(self)
                #clickAndDropInv(self)
                #leftClickDropInventory(self)
                #openPacks(self)
                #makeTablets(self)
                #checkRange(self)
                #dropInventory(self)
                #quickAFRandomAutoClicker(self)
                #highAlch(self)
                #sellItemsToShop(self)
                time.sleep(0.05)
            time.sleep(0.01)
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
def quick10through15RandomAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(10,15)
    # tenPercentChanceOfE()
    time.sleep(delay)
def quick60to120RandomAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(60,120)
    # tenPercentChanceOfE()
    time.sleep(delay)
#bank set to all standing infront of bank with empty inv
#zoomed out camera. WEAR GRACEFUL. have tab on 1 to grab stams
def buyBlastFurnaceOres(self):
    for ii in range (2):
        for i in range (4):
            #move mouse to ore guy
            moveMouse(returnInt(415, 424), returnInt(258, 267))
            waitClickWait(self,5,6)
            #move mouse to ore
            moveMouse(returnInt(437, 451), returnInt(236, 252))
            waitClick(self)
            #move mouse to bank
            moveMouse(returnInt(832, 842), returnInt(567, 576))
            waitClickWait(self,5,6)
            clickFirstInvSlot(self)
            clickEsc(self)
        switchWorlds(self)
        time.sleep(random.uniform(7,8))
        keyboard.press('e')
        keyboard.release('e')

    # move mouse to bank
    moveMouse(returnInt(624, 635), returnInt(434, 443))
    drinkStam(self,"1")
    clickEsc(self)


def drinkStam(self,invSlot):
    moveMouse(returnInt(624, 635), returnInt(434, 443))
    waitClickWait(self, .5,.8)
    #grab stam
    moveMouse(returnInt(672, 691), returnInt(505, 521))

    keyboard.press(Key.shift)
    waitClickWait(self, .5,.8)
    #drink stam
    if invSlot=='1':
        clickFirstInvSlot(self)
    else :
        clickSecondInvSlot(self)
    keyboard.release(Key.shift)
    #bank stam
    if invSlot=='1':
        clickFirstInvSlot(self)
    else :
        clickSecondInvSlot(self)
def switchWorlds(self):
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.right)
    time.sleep(random.uniform(.2,.4))
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release(Key.right)

#assumed zoomed in north facing camera lecturn in bottom left
def makeTablets(self):
    moveMouse(returnInt(612, 682), returnInt(305, 343))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(2,3))
    moveMouse(returnInt(635, 677), returnInt(232, 276))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(30,35))

    #click butler 2x
    moveMouse(returnInt(471,503), returnInt(415,462))
    time.sleep(random.uniform(.3, .6))
    mouse.click(self.button)
    time.sleep(random.uniform(1,2))
    mouse.click(self.button)

    #retrieve more planks
    time.sleep(random.uniform(1,2))
    keyboard.press('1')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('1')
    time.sleep(random.uniform(.3, .6))
    #run north
    moveMouse(returnInt(448,515), returnInt(78,148))
    time.sleep(random.uniform(1,2))
    mouse.click(self.button)
    #wait 8 sec
    time.sleep(random.uniform(5,6))
    #run south
    moveMouse(returnInt(728,798), returnInt(683,744))
    time.sleep(random.uniform(.3, .6))
    mouse.click(self.button)
    time.sleep(random.uniform(3,4))

#start ontop of spot one
def ardyCourse(self):
    #run roof 1 jump to roof two
    moveMouse(returnInt(611,624), returnInt(190,233))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    #run roof 2 walk plank to roof 3
    moveMouse(returnInt(551,562), returnInt(415,418))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    #roll a small chance you will pick up marks of grace
    if returnInt(0,25)==0:
        moveMouse(returnInt(640, 647), returnInt(414, 419))
        time.sleep(random.uniform(.2, .25))
        mouse.click(self.button)
        time.sleep(random.uniform(6,7))

    #run roof 3 jump to roof 4
    moveMouse(returnInt(561,580), returnInt(406,438))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    #run roof 4 jump gap
    moveMouse(returnInt(620,631), returnInt(500,535))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    #run roof 4 walk across steep roof
    moveMouse(returnInt(672,684), returnInt(574,584))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    #jump down
    moveMouse(returnInt(633,647), returnInt(420,456))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(11,12))
    #climb starting point to reset
    moveMouse(returnInt(713,731), returnInt(401,407))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))

###########################################################################TEMPLATE
def movementTemplate(self):
    moveMouse(returnInt(713,731), returnInt(401,407))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(1,2))
###########################################################################TEMPLATE

#assums on 4k monitor stretched mode on
def plantSapplings4kStreched(self):
    moveMouse(returnInt(-679,-628), returnInt(1885,1925))
    time.sleep(random.uniform(.2,.25))
    mouse.click(self.button)
    time.sleep(random.uniform(.1,.2))
    moveMouse(returnInt(-547,-504), returnInt(1883,1917))
    time.sleep(random.uniform(.2,.25))
    mouse.click(self.button)

def plantSapplings(self):
    moveMouse(returnInt(1166,1182), returnInt(742,754))
    time.sleep(random.uniform(.2,.25))
    mouse.click(self.button)
    time.sleep(random.uniform(.1,.2))
    moveMouse(returnInt(1208,1224), returnInt(740,760))
    time.sleep(random.uniform(.2,.25))
    mouse.click(self.button)
#bolder to the left, zoomed in with left click set to empty
#have inv full of bannana baskets 3 in spots just banana
def maniMonkeys(self):
    if (returnInt(0,10)>6):
        mmDropInventory(self)
    moveMouse(returnInt(456,493), returnInt(353,406))
    time.sleep(random.uniform(.2,.4))
    mouse.click(self.button)
    time.sleep(returnInt(5,6))
    mouse.click(self.button)
    delay = np.random.randint(15,20)
    # tenPercentChanceOfE()
    time.sleep(delay)
def cannonballAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(45,60)
    # tenPercentChanceOfE()
    time.sleep(delay)
def pixelRangeTest(self):
    moveMouse(returnInt(551,562), returnInt(415,418))
def colorTest(self):
    #check for portal 1:
    moveMouse(returnInt(757,770), returnInt(452,459))
    time.sleep(random.uniform(0.16, .2))
    print(checkForPrifPortal(self))
def mousePointerColorTest(self):
    #check for portal 1:
    moveMouse(returnInt(688,701), returnInt(557,571))
    time.sleep(random.uniform(0.16, .2))
    print(checkForPrifPortal(self))
def checkForPrifPortal(self):
    x, y = pyautogui.position()
    r1,g1,b1 = pyautogui.pixel(x, y)
    time.sleep(random.uniform(0.16, .2))
    r2,g2,b2 = pyautogui.pixel(x, y)
    #time.sleep(random.uniform(0.16, .2))
    #r3,g3,b3 = pyautogui.pixel(x, y)
    if r1!=r2 and g1!=g2 and b1 != b2:# and r1!=r3 and g1!=g3 and b1 != b3:
        return True
    else :
        return False
def prifAgil(self):
    #check for portal 1:
    moveMouse(returnInt(826,836), returnInt(473,483))
    time.sleep(random.uniform(0.16, .2))
    #portal is there on roof 1. Jump roof 2
    if checkForPrifPortal(self):
        print("taking portal from roof 1 to roof 2")
        mouse.click(self.button)
        time.sleep(random.uniform(4,5))
        moveMouse(returnInt(731,744), returnInt(469,481))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(5,6))
    #portal is not there walk rope 1 and jump roof 2
    else:
        #walk first roap (cfp)
        print("portal is not there walk rope 1 and jump roof 2")
        moveMouse(returnInt(825,840), returnInt(610,624))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(14,15))
        #jump roofs
        moveMouse(returnInt(807,818), returnInt(476,483))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(5,6))
    #jump down off the roof
    print("jumping off roof")
    moveMouse(returnInt(778,785), returnInt(425,433))
    time.sleep(random.uniform(0.16, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    # check for portal 2 before going into hole
    moveMouse(returnInt(806, 816), returnInt(539, 549))
    time.sleep(random.uniform(0.16, .2))
    #portal is there take it and walk across bridge
    if checkForPrifPortal(self):
        print("portal found at hole")
        mouse.click(self.button)
        time.sleep(random.uniform(3,4))
        moveMouse(returnInt(690,699), returnInt(494,507))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        #input('Press ENTER to exit')
        time.sleep(random.uniform(9,10))
    #portal is not there enter hole climb ladder and cross bridge
    else:
        print("no portal found at hole")
        #enter hole
        moveMouse(returnInt(786,790), returnInt(498,500))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(5,6))
        #climb ladder
        moveMouse(returnInt(804,818), returnInt(419,436))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(5,6))
        #cross bridge 1 (cfp)
        moveMouse(returnInt(663,676), returnInt(580,593))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(10,11))
        print("bridge 1")
    #on platform2 check for portal
    moveMouse(returnInt(797, 810), returnInt(611, 628))
    time.sleep(random.uniform(0.16, .2))
    shortcutTaken = False
    #portal is there take it then cross rope 2
    if checkForPrifPortal(self):
        print("platform 2 has portal. taking it to p3 and crossing rope to p4")
        mouse.click(self.button)
        time.sleep(random.uniform(4, 5))
        #cross rope 2
        moveMouse(returnInt(822,836), returnInt(402,416))
        #moveMouse(returnInt(720,735), returnInt(449,462))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)

        time.sleep(random.uniform(9,10))
        #cross rope 3
        #moveMouse(returnInt(697,717), returnInt(426,439))
        moveMouse(returnInt(720, 735), returnInt(449, 462))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        print("crossed p4 to p5")
        time.sleep(random.uniform(9,10))
    #cross invisa bridge then cross rope 2
    else:
        print("platform 2 does not have a portal. Walking the rope to platform 3")
        moveMouse(returnInt(697,708), returnInt(520,530))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(8,9))

        #cross rope 2 (cfp)
        #check for portal

        moveMouse(returnInt(688,701), returnInt(557,571))
        time.sleep(random.uniform(0.16, .2))
        #check for portal on platform 3
        if checkForPrifPortal(self):
            #portal found
            mouse.click(self.button)

            print("took platform 3 portal to platform 4")
            time.sleep(random.uniform(4,5))
            #cross rope to p5
            #moveMouse(returnInt(720,732), returnInt(452,464))
            moveMouse(returnInt(697,717), returnInt(426,439))
            time.sleep(random.uniform(0.16, .2))
            mouse.click(self.button)
            time.sleep(random.uniform(9,10))


        #no portal found on platform 3
        else:
            print("took platform 3 invsabridge to platform 4")
            moveMouse(returnInt(755,769), returnInt(469,479))
            time.sleep(random.uniform(0.16, .2))
            mouse.click(self.button)
            time.sleep(random.uniform(8,9))

            #print("took p4 rope to p5")
            #check for portal

            moveMouse(returnInt(821, 834), returnInt(537, 547))
            time.sleep(random.uniform(0.16, .2))
            if checkForPrifPortal(self):
                mouse.click(self.button)

                print("took portal from platform 4 to 5")
                time.sleep(random.uniform(4, 5))
                #rope4

                moveMouse(returnInt(791,800), returnInt(452,460))
                time.sleep(random.uniform(0.16, .2))
                mouse.click(self.button)
                shortcutTaken = True

                print("walkin rope to land")
                time.sleep(random.uniform(8,9))
            else:
                #cross rope 3 to land
                moveMouse(returnInt(726,733), returnInt(454,458))
                time.sleep(random.uniform(0.16, .2))
                mouse.click(self.button)

                print("took rope from platform 4 to 5")
                time.sleep(random.uniform(8,9))

    #check for portal before rope 4
    #moveMouse(returnInt(757,770), returnInt(452,459))
    #time.sleep(random.uniform(0.16, .2))
    #if checkForPrifPortal(self):
    #    mouse.click(self.button)

   #     print("p 10")
    #    time.sleep(random.uniform(4,5))
        #enter hole
   #     moveMouse(returnInt(686, 697), returnInt(380, 391))
    #    time.sleep(random.uniform(0.16, .2))
    #    mouse.click(self.button)
    #    time.sleep(random.uniform(8, 9))
    #else:
    #cross rope 3
    if  not shortcutTaken:
        moveMouse(returnInt(859,868), returnInt(477,483))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        print("crossed p5 rope to land")
        time.sleep(random.uniform(8,9))
    #enter hole
    moveMouse(returnInt(736,744), returnInt(368,377))
    time.sleep(random.uniform(0.16, .2))
    print("clicked enter hole")
    mouse.click(self.button)
    time.sleep(random.uniform(7,8))
    #run to restart=
    moveMouse(returnInt(1088,1092), returnInt(520,525))
    time.sleep(random.uniform(0.16, .2))
    mouse.click(self.button)
    print("running to reset")
    time.sleep(random.uniform(7,8))


def prifAgilWithHA(self):
    highAlchForPriff(self)
    #check for portal 1:
    moveMouse(returnInt(826,836), returnInt(473,483))
    time.sleep(random.uniform(0.16, .2))
    #portal is there on roof 1. Jump roof 2
    if checkForPrifPortal(self):
        print("taking portal from roof 1 to roof 2")
        mouse.click(self.button)
        time.sleep(random.uniform(4,5))
        moveMouse(returnInt(731,744), returnInt(469,481))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(6,7))
    #portal is not there walk rope 1 and jump roof 2
    else:
        #walk first roap (cfp)
        print("portal is not there walk rope 1 and jump roof 2")
        moveMouse(returnInt(825,840), returnInt(610,624))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(14,15))
        #jump roofs
        moveMouse(returnInt(807,818), returnInt(476,483))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(6,7))
    #jump down off the roof
    print("jumping off roof")
    moveMouse(returnInt(778,785), returnInt(425,433))
    time.sleep(random.uniform(0.16, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    highAlchForPriff(self)
    # check for portal 2 before going into hole
    moveMouse(returnInt(806, 816), returnInt(539, 549))
    time.sleep(random.uniform(0.16, .2))
    #portal is there take it and walk across bridge
    if checkForPrifPortal(self):
        print("portal found at hole")
        mouse.click(self.button)
        time.sleep(random.uniform(3,4))
        moveMouse(returnInt(690,699), returnInt(494,507))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        #input('Press ENTER to exit')
        time.sleep(random.uniform(9,10))
    #portal is not there enter hole climb ladder and cross bridge
    else:
        print("no portal found at hole")
        #enter hole
        moveMouse(returnInt(786,790), returnInt(498,500))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(5,6))
        #climb ladder
        moveMouse(returnInt(804,818), returnInt(419,436))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(5,6))
        #cross bridge 1 (cfp)
        moveMouse(returnInt(663,676), returnInt(580,593))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(10,11))
        print("bridge 1")
    #on platform2 check for portal
    highAlchForPriff(self)
    time.sleep(random.uniform(0.16, .2))
    moveMouse(returnInt(797, 810), returnInt(611, 628))
    time.sleep(random.uniform(0.16, .2))
    shortcutTaken = False
    #portal is there take it then cross rope 2
    if checkForPrifPortal(self):
        print("platform 2 has portal. taking it to p3 and crossing rope to p4")
        mouse.click(self.button)
        time.sleep(random.uniform(4, 5))
        #cross rope 2
        moveMouse(returnInt(822,836), returnInt(402,416))
        #moveMouse(returnInt(720,735), returnInt(449,462))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)

        time.sleep(random.uniform(9,10))
        #cross rope 3
        #moveMouse(returnInt(697,717), returnInt(426,439))
        moveMouse(returnInt(720, 735), returnInt(449, 462))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        print("crossed p4 to p5")
        time.sleep(random.uniform(9,10))
    #cross invisa bridge then cross rope 2
    else:
        print("platform 2 does not have a portal. Walking the rope to platform 3")
        moveMouse(returnInt(697,708), returnInt(520,530))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(8,9))

        #cross rope 2 (cfp)
        #check for portal

        highAlchForPriff(self)
        time.sleep(random.uniform(0.36, .6))
        moveMouse(returnInt(688,701), returnInt(557,571))
        time.sleep(random.uniform(0.16, .2))
        #check for portal on platform 3
        if checkForPrifPortal(self):
            #portal found
            mouse.click(self.button)

            print("took platform 3 portal to platform 4")
            time.sleep(random.uniform(4,5))
            #cross rope to p5
            #moveMouse(returnInt(720,732), returnInt(452,464))
            moveMouse(returnInt(697,717), returnInt(426,439))
            time.sleep(random.uniform(0.16, .2))
            mouse.click(self.button)
            time.sleep(random.uniform(9,10))

        #no portal found on platform 3
        else:
            print("took platform 3 invsabridge to platform 4")
            moveMouse(returnInt(755,769), returnInt(469,479))
            time.sleep(random.uniform(0.16, .2))
            mouse.click(self.button)
            time.sleep(random.uniform(8,9))

            #print("took p4 rope to p5")
            #check for portal

            moveMouse(returnInt(821, 834), returnInt(537, 547))
            time.sleep(random.uniform(0.16, .2))
            if checkForPrifPortal(self):
                mouse.click(self.button)

                print("took portal from platform 4 to 5")
                time.sleep(random.uniform(4, 5))
                #rope4

                moveMouse(returnInt(791,800), returnInt(452,460))
                time.sleep(random.uniform(0.16, .2))
                mouse.click(self.button)
                shortcutTaken = True

                print("walkin rope to land")
                time.sleep(random.uniform(8,9))
            else:
                #cross rope 3 to land
                moveMouse(returnInt(726,733), returnInt(454,458))
                time.sleep(random.uniform(0.16, .2))
                mouse.click(self.button)

                print("took rope from platform 4 to 5")
                time.sleep(random.uniform(8,9))

    #check for portal before rope 4
    #moveMouse(returnInt(757,770), returnInt(452,459))
    #time.sleep(random.uniform(0.16, .2))
    #if checkForPrifPortal(self):
    #    mouse.click(self.button)

   #     print("p 10")
    #    time.sleep(random.uniform(4,5))
        #enter hole
   #     moveMouse(returnInt(686, 697), returnInt(380, 391))
    #    time.sleep(random.uniform(0.16, .2))
    #    mouse.click(self.button)
    #    time.sleep(random.uniform(8, 9))
    #else:
    #cross rope 3
    if  not shortcutTaken:
        moveMouse(returnInt(859,868), returnInt(477,483))
        time.sleep(random.uniform(0.16, .2))
        mouse.click(self.button)
        print("crossed p5 rope to land")
        time.sleep(random.uniform(8,9))
    highAlchForPriff(self)
    #enter hole
    moveMouse(returnInt(736,744), returnInt(368,377))
    time.sleep(random.uniform(0.16, .2))
    print("clicked enter hole")
    mouse.click(self.button)
    time.sleep(random.uniform(7,8))
    highAlchForPriff(self)
    #run to restart=
    moveMouse(returnInt(1088,1092), returnInt(520,525))
    time.sleep(random.uniform(0.16, .2))
    mouse.click(self.button)
    print("running to reset")
    time.sleep(random.uniform(7,8))



def cannonAutoClicker(self):
    keyboard.press(Key.shift)
    time.sleep(random.uniform(.2,.3))
    mouse.click(self.button)
    time.sleep(random.uniform(.2,.3))
    keyboard.release(Key.shift)
    delay = np.random.randint(60,90)
    # tenPercentChanceOfE()
    time.sleep(delay)
def quickAFRandomAutoClicker(self):
    mouse.click(self.button)
    # tenPercentChanceOfE()
    time.sleep(random.uniform(.2,.3))

#x set to 14
def birdNest(self):
    clickCraftingGuildBank(self)
    emptyInventoryInBank(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    leftClickHalfInventory(self)
#assumes facing south camera down
def wildyAlter(self):

    moveMouse(returnInt(columnNums[6], columnNums[7]), returnInt(rowNums[12], rowNums[13]))
    time.sleep(random.uniform(0.1, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(.1,.2))
    moveMouse(returnInt(827,970),returnInt(384,636))
    time.sleep(random.uniform(.1,.2))
    mouse.click(self.button)
def sellItemsToShop(self):
    #right click first

    xVal = returnInt(1080, 1100)
    yVal = returnInt(524,543)
    moveMouse(xVal, yVal )
    rightClickForthOption(self,xVal,yVal)
def clickOpFarmSpot(self,doubleClick):
    moveMouse(returnInt(606,630),returnInt(365,386))
    time.sleep(random.uniform(.2,.32))
    mouse.click(self.button)
    if(doubleClick):
        time.sleep(random.uniform(.1, .2))
        mouse.click(self.button)
    time.sleep(random.uniform(2,2.5))
def water(self):

    # click spot
    moveMouse(returnInt(592, 636), returnInt(432, 475))
    time.sleep(random.uniform(.1, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(.1, .2))
    mouse.click(self.button)
    #above plants
    time.sleep(random.uniform(2.3,2.5))
    for x in range(3):

        #method call to opposite spot
        #click again to water
        clickOpFarmSpot(self,True)
        #click diagonally readjust and click again to water
        moveMouse(returnInt(555, 582), returnInt(452, 488))
        time.sleep(random.uniform(.1, .2))
        mouse.click(self.button)
        time.sleep(random.uniform(.1, .2))
        mouse.click(self.button)
        #above plants
        time.sleep(random.uniform(3.5,4))

    clickOpFarmSpot(self,True)
def plant8(self):

    # click first inv spot
    clickFirstInvSlot(self)
    #click the patch
    moveMouse(returnInt(592, 636), returnInt(432, 475))
    time.sleep(random.uniform(.1, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(1.8,2))
    #water same plant
    mouse.click(self.button)
    time.sleep(random.uniform(.6,1))
    for x in range(3):
        #method call to opposite spot
        clickFirstInvSlot(self)
        clickOpFarmSpot(self,False)
        #click again to water
        mouse.click(self.button)
        time.sleep(random.uniform(.8,1))

        clickFirstInvSlot(self)
        #click diagonally
        moveMouse(returnInt(554, 576), returnInt(449, 470))
        time.sleep(random.uniform(.1, .2))
        #click and move
        mouse.click(self.button)
        time.sleep(random.uniform(3,3.5))
        #readjust
        moveMouse(returnInt(592, 636), returnInt(432, 475))
        time.sleep(random.uniform(.1,.2))
        mouse.click(self.button)
        time.sleep(random.uniform(1,2))
    #plant lasts spot
    clickFirstInvSlot(self)
    clickOpFarmSpot(self,False)
    #click again to water
    mouse.click(self.button)
    time.sleep(random.uniform(2,2.5))
    time.sleep(random.uniform(1, 1.2))
#assumes facing east
def walkway(self):
    moveMouse(returnInt(514, 526), returnInt(428, 436))
    time.sleep(random.uniform(.1, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(3.5,4))
def startSpotForTithe(self):
    moveMouse(returnInt(1047, 1058), returnInt(428, 440))
    time.sleep(random.uniform(.1, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
def titheFarm(self):
    #click first spot
    #moveMouse(returnInt(838,844),returnInt(363,372))
    #time.sleep(random.uniform(.1,.2))
    #mouse.click(self.button)
    #time.sleep(random.uniform(5,6))
    #plant/water ######################################################1
    plant8(self)
    #click across walkway#
    walkway(self)
    plant8(self)

    ###################################################
    #click to reset location
    startSpotForTithe(self)
    #water ######################################################2
    water(self)
    #click across walkway
    walkway(self)
    water(self)
    #click to reset
    startSpotForTithe(self)

    #water ######################################################3
    water(self)
    #click across walkway
    walkway(self)
    water(self)
    time.sleep(random.uniform(.8,1))



    #click to reset
    startSpotForTithe(self)
    #pick ######################################################4
    water(self)
    #click across walkway
    walkway(self)
    water(self)

    time.sleep(random.uniform(2,3))
    #click_thread.stop_clicking()
    #refill and reset
    clickSecondInvSlot(self)
    moveMouse(returnInt(833, 845), returnInt(505, 514))
    time.sleep(random.uniform(.1, .2))
    mouse.click(self.button)
    time.sleep(random.uniform(25,30))
    moveMouse(returnInt(838, 848), returnInt(363, 372))
    time.sleep(random.uniform(.1, .2))
    mouse.click(self.button)
    #water fillup time
    time.sleep(random.uniform(9,11))
#takes in param to enchant a certain type. Assumes zoooomed in and x set to all. cosmic runes in last in
#inv spot
def enchant(self, type):
    clickFirstInvSlot(self)

    clickFirstBankSpot(self)
    clickEsc(self)
    if (type == "saphire"):
        moveMouse(returnInt(1204, 1212), returnInt(519, 529))
        waitClickWait(self, .3,.6)
    clickFirstInvSlot(self)
    sleep(returnInt(40,50))
    clickCraftingGuildBank(self)

def enchantBolts(self):
    mouse.click(self.button)
    time.sleep(random.uniform(.82,.94))
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(8,10))
def cleanHerbs(self):
    clickCraftingGuildBank(self)
    clickFirstInvSlot(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    leftClickDropInventory(self)
    time.sleep(random.uniform(3,4))
#set x to 14
def  makePots(self):
    #empty inv
    clickSecondOrThirdInvSlot(self)
    #grab herb and water
    clickFirstBankSpot(self)
    clickSecondBankSpot(self)
    clickEsc(self)
    #mix
    clickMiddleInvSlots(self)
    time.sleep(random.uniform(.82,.94))
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(11,12))
    #bank
    clickCraftingGuildBank(self)
    clickThirdBankSpot(self)
    clickEsc(self)
    #mix
    clickMiddleInvSlots(self)
    time.sleep(random.uniform(.82,.94))
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(18,19))
    #bank
    clickCraftingGuildBank(self)
def broads(self):
    # click inv spot one
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.07, .08))  # random.uniform(0.3, .5)
    mouse.click(self.button)
    # click inv spot 5
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[2], rowNums[3]))
    time.sleep(random.uniform(0.03, .05))  # random.uniform(0.3, .5)
    mouse.click(self.button)  # start herb animation
def plankMake(self):
    time.sleep(random.uniform(.2, .4))
    clickSecondOrThirdInvSlot(self)
    clickFirstBankSpot(self)
    time.sleep(random.uniform(.2, .4))
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(random.uniform(.2, .4))

    #click plank make spell

    moveMouse(returnInt(1188, 1192), returnInt(677, 684))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
    #click again
    mouse.click(self.button)
    time.sleep(random.uniform(45,60))

    # clickLilIslandBank(self)
    clickFishingGuildBank(self)
#assumes set on all with glass in bank spot 1 and pipe in inv slot 1
#do first inv before starting to set space bar
def craftOrFletch(self):
    time.sleep(random.uniform(.2,.4))
    clickSecondOrThirdInvSlot(self)
    clickFirstBankSpot(self)
    time.sleep(random.uniform(.2,.4))
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(random.uniform(.2,.4))
    clickFirstInvSlot(self)
    clickSecondInvSlot(self)
    time.sleep(random.uniform(.8,.9))
    #keyboard.press('2')
    #keyboard.release('2')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(random.uniform(45,55))
    #clickLilIslandBank(self)
    clickCraftingGuildBank(self)

def spinFlax(self):
    depositAll(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    #click stairs
    moveMouse(returnInt(568,584),returnInt(621,634))
    waitClickWait(self,5,6)
    #click wheel
    moveMouse(returnInt(676,684),returnInt(343,352))
    waitClickWait(self,5,6)
    #click 3
    keyboard.press('3')
    keyboard.release('3')
    time.sleep(random.uniform(40,54))
    #click stairs
    moveMouse(returnInt(541,555),returnInt(524,533))
    waitClickWait(self,5,6)
    #click bank
    moveMouse(returnInt(674,684),returnInt(193,208))
    waitClickWait(self,5,6)


def stringBows(self):
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    clickSecondBankSpot(self)
    time.sleep(random.uniform(.2,.4))
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(random.uniform(.2,.4))
    clickFirstInvSlot(self)
    clickLastInvSlot(self)
    time.sleep(random.uniform(.2,.4))
    #keyboard.press('2')
    #keyboard.release('2')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(random.uniform(18,20))
    #clickLilIslandBank(self)
    clickCraftingGuildBank(self)
def spec(self):
    moveMouse(returnInt(1112,1125),returnInt(168,183))
    waitClickWait(self,.2,.4)
def toggleRun(self):
    moveMouse(returnInt(1089,1101),returnInt(142,160))
    waitClickWait(self,.2,.4)

#assumes zoomed in and starting with farmer pinned to south
def masterFarmerGuild(self):
    moveMouse(returnInt(621,676),returnInt(588,628))
    for x in range(returnInt(163,174)):
        waitClickWait(self,.2,.4)

    moveMouse(returnInt(556,648),returnInt(229,316))
    time.sleep(random.uniform(0.8, 1))
    waitClickWait(self,5,10)
    leftClickDropInventory(self)
    pause(self)
#assumes zoomed in and starting with farmer pinned between guard and dog. camera south
#need spear to lure guard (not the bow one) and knife to lure dog
def masterFarmerHouseLure(self):
    moveMouse(returnInt(624,667),returnInt(257,286))
    for x in range(returnInt(70,83)):
        waitClickWait(self,.2,.4)

    waitClickWait(self,.2,.4)
    leftClickDropInventory(self)
def shiloVillageSurfaceMine(self):
    moveMouse(returnInt(638,649),returnInt(432,444))
    waitClickWait(self,9,10)
    moveMouse(returnInt(625,634),returnInt(396,404))
    waitClickWait(self,9,10)
    moveMouse(returnInt(660,669),returnInt(416,424))
    waitClickWait(self,6,7)
    moveMouse(returnInt(644,652),returnInt(364,373))
    waitClickWait(self,7,8)
    moveMouse(returnInt(661,666),returnInt(411,420))
    waitClickWait(self,8,9)
    moveMouse(returnInt(643,650),returnInt(376,384))
    waitClickWait(self,9,12)
    sleep(10)
    moveMouse(returnInt(533,542),returnInt(483,489))
    waitClickWait(self,9,12)
def ardyKnights(self):
    moveMouse(returnInt(1027,1081),returnInt(359,400))
    moveMouse(returnInt(1027,1081),returnInt(359,400))
    for x in range(returnInt(30,49)):
        if not self.running:
            pause(self)
        waitClickWait(self,.2,.4)
    time.sleep(random.uniform(0.8, 1))
    clickFirstInvSlot(self)

def yewsAndBank(self):
    #empty inv
    emptyInventoryInBank(self)
    clickEsc(self)

    if(returnInt(0, 10)<5):
        spec(self)
    #Click first yew tree
    moveMouse(returnInt(454,475),returnInt(236,244))
    waitClickWait(self,45,55)
    #Click second yew tree
    moveMouse(returnInt(640,652),returnInt(470,485))
    waitClickWait(self,45,55)
    for i in range (2):
        #Click first yew tree
        moveMouse(returnInt(595,608),returnInt(352,368))
        waitClickWait(self,45,55)
        #Click second yew tree
        moveMouse(returnInt(640,652),returnInt(470,485))
        waitClickWait(self,45,55)
    #click bank
    moveMouse(returnInt(752,760),returnInt(547,556))
    waitClickWait(self,6,7)
#start in bank with deposit all on
#gpu plugin on and atleast 30
#inventory closed
def cutFossilIslandTreesAndBank(self):
    #empty inv
    emptyInventoryInBank(self)
    #click on cave
    moveMouse(returnInt(155,185), returnInt(196,220))
    waitClickWait(self,9,11)

    if(returnInt(0, 10)<5):
        spec(self)
    #click on first tree
    moveMouse(returnInt(644,671), returnInt(315,341))
    waitClickWait(self,39,55)
    #aitClickWait(self,2,3)
    #click on second tree
    moveMouse(returnInt(505,536), returnInt(402,424))
    waitClickWait(self,37,57)
    #waitClickWait(self,2,3)
    #click on third tree
    moveMouse(returnInt(459,491), returnInt(328,352))
    waitClickWait(self,34,56)
    #waitClickWait(self,3,4)
    #click on second tree
    moveMouse(returnInt(685,703), returnInt(462,476))
    waitClickWait(self,34,56)
    #waitClickWait(self,2,3)
    #click on cave from second tree
    moveMouse(returnInt(753,781), returnInt(520,536))
    waitClickWait(self,5,6)
    #click on cave from 3rd tree
    #moveMouse(returnInt(783,811), returnInt(544,563))
    #waitClickWait(self,5,6)
    #click on bank
    moveMouse(returnInt(1112,1127), returnInt(594,609))
    waitClickWait(self,9,10)
def varrockSmithing(self):
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    #click anvil
    moveMouse(returnInt(679,689), returnInt(672,681))
    waitClickWait(self,6,7)
    #click space
    clickSpace(self)
    time.sleep(random.uniform(12,14))
    #click bank
    moveMouse(returnInt(588,600), returnInt(151,172))
    waitClickWait(self,6,7)
def cutFossilIslandTest(self):
    #click on first tree
    moveMouse(randomInSquare(719),randomInSquare(415))
    #waitClickWait(self,39,55)
    waitClickWait(self,2,3)
    #click on second tree
    moveMouse(randomInSquare(541),randomInSquare(520))
    #waitClickWait(self,37,57)
    waitClickWait(self,2,3)
    #click on third tree
    moveMouse(randomInSquare(486),randomInSquare(431))
    #waitClickWait(self,34,56)
    waitClickWait(self,3,4)
    #click on second tree
    moveMouse(randomInSquare(768),randomInSquare(595))
    #waitClickWait(self,34,56)
    waitClickWait(self,2,3)
    #click on cave
    moveMouse(randomInSquare(855),randomInSquare(665))
    waitClickWait(self,5,6)

    click_thread.stop_clicking()
#assumes at fishing guild bank camera zoomed in and north
#assumes bank fillers are on with runes in inv
#x set to 18
def superGlassmake(self):
    for x in range(4):
        emptyInventoryInBank(self)
        keyboard.press(Key.shift)
        #click first bank spot with no long wait
        moveMouse(returnInt(340,357), returnInt(104,123))
        waitClickWait(self,0.1,.12)
        #click y more seaweeds
        for y in range(2):
            mouse.click(self.button)
            time.sleep(random.uniform(0.1,.12))
        keyboard.release(Key.shift)
        clickSecondBankSpot(self)
        clickEsc(self)
        #click glass make spell
        moveMouse(returnInt(1069, 1080), returnInt(624, 634))
        waitClickWait(self,3,4)
        clickFishingGuildBank(self)
    #pick up dropped glass
    emptyInventoryInBank(self)
    clickEsc(self)
    pickUpFromGround(self)
    clickFishingGuildBank(self)
#assumes at fishing guild bank camera zoomed in and north
#assumes money in last inv slot x set to all
#spell book zoomed
def plankMakeSpell(self):
    clickSecondOrThirdInvSlot(self)
    #click first bank spot with no long wait
    moveMouse(returnInt(340,357), returnInt(104,123))
    waitClickWait(self,0.1,.12)

    clickEsc(self)
    #click plank make spell
    moveMouse(returnInt(1183, 1188), returnInt(674, 684))
    waitClickWait(self,.5,.6)
    waitClickWait(self,75,80)
    clickCraftingGuildBank(self)
def pickUpFromGround(self):
    moveMouse(returnInt(577, 616), returnInt(414, 458))
    for x in range(returnInt(27,33)):
        time.sleep(random.uniform(0.42,.6))
        mouse.click(self.button)
#this bot dope as hell have camera zoomed in till the east box is 1 pan from out of frame
#have tab set to spells with no filter
def mageTrainingArenaGraveyard(self):
    moveMouse(returnInt(533,560),returnInt(415,438))
    for i in range(15):
        time.sleep(random.uniform(0.42,.6))
        mouse.click(self.button)

    moveMouse(returnInt(1202,1212),returnInt(635,648))
    time.sleep(random.uniform(0.42,.6))
    mouse.click(self.button)

    keyboard.press('e')
    time.sleep(random.uniform(0.42,.6))
    keyboard.release('e')

    eat8fruit(self)

    keyboard.press('f')
    time.sleep(random.uniform(0.42,.6))
    keyboard.release('f')

    moveMouse(returnInt(1131,1157),returnInt(238,276))
    time.sleep(random.uniform(0.42,.6))
    mouse.click(self.button)
    time.sleep(random.uniform(3.5,4))

    moveMouse(returnInt(113,144),returnInt(522,553))
    time.sleep(random.uniform(0.42,.6))
    mouse.click(self.button)
    time.sleep(random.uniform(3.5,4))
#start on start rock camera north
#have inv set on spell book

def mageTrainingArenaEnchant(self):
    moveMouse(returnInt(603,613),returnInt(415,420))
    for i in range(26):
        time.sleep(random.uniform(0.42,.6))
        mouse.click(self.button)

    moveMouse(returnInt(1124,1142),returnInt(683,695))
    for i in range(24):
        time.sleep(random.uniform(.8,1.2))
        mouse.click(self.button)

    time.sleep(random.uniform(20,25))
    #click on well

    moveMouse(returnInt(890,897),returnInt(642,648))
    time.sleep(random.uniform(.4,.8))
    mouse.click(self.button)
    time.sleep(random.uniform(7,8))

    #back on crate
    moveMouse(returnInt(390,400),returnInt(216,224))
    time.sleep(random.uniform(.4,.8))
    mouse.click(self.button)
    time.sleep(random.uniform(7,8))
def eat8fruit(self):
    for i in range(4):
        for ii in range(2):
            #rowLow=i*2f
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(.6,.8))
            mouse.click(self.button)
def threeTickMiningGranite(self):
    #click rock 2
    moveMouse(randomInSquare(832),randomInSquare(715))
    waitClickWait(self,1,1.2)
    #click 3t
    tickManipulate(self)
    drop3tItems(self)
    #click 3rd rock
    moveMouse(randomInSquare(835),randomInSquare(715))
    waitClickWait(self,1,1.2)
    #click 3t
    tickManipulate(self)
    drop3tItems(self)
    #click 4th
    moveMouse(randomInSquare(464),randomInSquare(694))
    waitClickWait(self,1,1.2)
    #click 3t
    tickManipulate(self)
    drop3tItems(self)
    #click 1st
    moveMouse(randomInSquare(1031),randomInSquare(118))
    waitClickWait(self,1.6,1.8)
    #click 3tick
    tickManipulate(self)
    drop3tItems(self)


def cookSeaweedAtFT(self):
    #click empty inv
    emptyInventoryInBank(self)
    time.sleep(random.uniform(.2,.4))
    #click bank spot 1
    clickFirstBankSpot(self)
    time.sleep(random.uniform(.2,.4))
    #click esc
    clickEsc(self)
    time.sleep(random.uniform(.9,1.4))
    #click fire
    moveMouse(randomInSquare(714), randomInSquare(695))
    time.sleep(random.uniform(.2,.4))
    mouse.click(self.button)
    #wait while running
    time.sleep(random.uniform(4,5))
    #space
    clickSpace(self)
    #click bank after waiting few sec

    time.sleep(random.uniform(7,9 ))
    moveMouse(randomInSquare(671), randomInSquare(391))
    time.sleep(random.uniform(.2,.4))
    mouse.click(self.button)
    time.sleep(random.uniform(3,4))
#assumes on spell tab
def highAlch(self):
    moveMouse(returnInt(1227, 1235), returnInt(608, 623))
    time.sleep(random.uniform(1, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(1, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(1, 1.2))
#assumes on spell tab use0s pyhsical
def highAlchForPriff(self):
    moveMouse(returnInt(1533, 1543), returnInt(767, 778))
    time.sleep(random.uniform(0.9, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(0.9, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(1,2))
#assums starting top of seers bank
#zoomed out and north
def seersCourse(self):

    highAlch(self)
    #jump to next roof
    moveMouse(returnInt(483, 506), returnInt(424, 539))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    highAlch(self)
    #cross rope
    moveMouse(returnInt(626, 641), returnInt(656, 668))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    highAlch(self)
    #jump to next roof
    moveMouse(returnInt(686, 809), returnInt(634, 657))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    highAlch(self)
    #jump to next roof
    moveMouse(returnInt(451, 507), returnInt(614, 627))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    highAlch(self)
    #jump down
    moveMouse(returnInt(715, 736), returnInt(543, 664))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    highAlch(self)

    if(returnInt(0,10)>5):
        #click mid square
        moveMouse(returnInt(1201, 1213), returnInt(261, 274))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(0.3, .5))
        highAlch(self)
        time.sleep(random.uniform(7,8))
        highAlch(self)
        #climb up bank
        moveMouse(returnInt(742, 752), returnInt(259, 281))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(9, 10))
    else:
        #click left square
        moveMouse(returnInt(1174, 1192), returnInt(261, 274))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(0.3, .5))
        highAlch(self)
        time.sleep(random.uniform(7,8))
        highAlch(self)
        #climb up bank
        moveMouse(returnInt(763, 779), returnInt(259, 278))
        time.sleep(random.uniform(0.3, .5))
        mouse.click(self.button)
        time.sleep(random.uniform(9, 10))
#Zoomed out starting ontop of first roof
def rellekkaCourse(self):
    #click first jump gap
    moveMouse(returnInt(542, 592), returnInt(504, 561))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    highAlch(self)
    #Click tight rope
    moveMouse(returnInt(636, 652), returnInt(590, 612))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(8,9))
    highAlch(self)

    # Click second gap / tight rope
    moveMouse(returnInt(659, 724), returnInt(360, 392))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(12,13))
    highAlch(self)

    # Click third gap
    moveMouse(returnInt(691, 724), returnInt(380, 411))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    highAlch(self)

    #Click second tight rope
    moveMouse(returnInt(696, 709), returnInt(308, 316))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    highAlch(self)

    #jump down
    moveMouse(returnInt(587, 631), returnInt(284, 336))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    highAlch(self)
    time.sleep(random.uniform(0.3, .5))

    #run across market and click jump up
    moveMouse(returnInt(143, 159), returnInt(402, 406))
    time.sleep(random.uniform(0.3, .5))
    mouse.click(self.button)
    time.sleep(random.uniform(11,12))
    highAlch(self)

def lunarSpinFlax(self):
    clickSecondOrThirdInvSlot(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    #Click spell 5x
    moveMouse(returnInt(1228, 1240), returnInt(596, 608))
    for x in range(5):
        waitClickWait(self,1.6,1.8)

    time.sleep(random.uniform(2,3))
    clickFishingGuildBank(self)
def checkRange(self):
    moveMouse(returnInt(420, 504), returnInt(387, 475))
#assumes zoomed in camera is east
def clickFishingGuildBank(self):
    moveMouse(returnInt(420, 504), returnInt(387, 475))
    waitClickWait(self,.2,.4)
    time.sleep(random.uniform(.8,1))
#assumes zoomed in camera is north
def clickCraftingGuildBank(self):
    moveMouse(returnInt(753, 820), returnInt(395, 476 ))
    waitClickWait(self,.2,.4)
    time.sleep(random.uniform(.8,1))
#assumes zoomed in
def clickLilIslandBank(self):
    moveMouse(randomInSquare(412), randomInSquare(465))
    waitClickWait(self,.2,.4)
    time.sleep(random.uniform(.2,.4))
#assumes mould is in inv spot 1 and x set to all camera zoomed out
def edgevilleFurnace(self):
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    #click furnace
    moveMouse(returnInt(880,887), returnInt(328,339))
    waitClickWait(self,6,8)
    #click space
    clickSpace(self)
    time.sleep(random.uniform(40,50))
    #click bank
    moveMouse(returnInt(387,394), returnInt(519,528))
    waitClickWait(self,6,8)
#assumes mould is in inv spot 1 and x set to 13 zoomed out
def edgevilleFurnace2Item(self):
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    clickSecondBankSpot(self)
    #click furnace
    moveMouse(returnInt(880,887), returnInt(328,339))
    waitClickWait(self,6,8)
    #click space
    clickSpace(self)
    time.sleep(random.uniform(23,25))
    #click bank
    moveMouse(returnInt(387,394), returnInt(519,528))
    waitClickWait(self,6,8)

#zoom to square under wiki banner
def runCannonBalls(self):
    #deposit all cannonballs
    clickSecondInvSlot(self)
    #grab more bars
    clickFirstBankSpot(self)

    #click furnace
    moveMouse(returnInt(874, 882), returnInt(331, 338))
    waitClickWait(self,6,8)
    #click space
    clickSpace(self)
    time.sleep(random.uniform(70,80))
    #click bank
    moveMouse(returnInt(394, 405), returnInt(517, 532))
    waitClickWait(self,6,8)

def amaniteCrabs3(self):
    for x in range(10):
        #click
        #wait 15.6 seconds
        mouse.click(self.button)
        time.sleep(random.uniform(62,67))
        print(x)
    # regain agro
    moveMouse(returnInt(760, 777), returnInt(1037, 1046))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    moveMouse(returnInt(628, 644), returnInt(51, 66))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    moveMouse(returnInt(628, 644), returnInt(95, 106))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    mouseUnderPerson(self)
def amaniteCrabs2(self):
    for x in range(9):
        #click
        #wait 15.6 seconds
        mouse.click(self.button)
        time.sleep(random.uniform(45,55))
        print(x)
    #regain agro
    moveMouse(returnInt(77, 98), returnInt(418, 437))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    moveMouse(returnInt(603, 619), returnInt(545, 558))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(3,5))
    moveMouse(returnInt(1201, 1215), returnInt(647, 660))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    moveMouse(returnInt(806, 819), returnInt(546, 559))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(3,5))
    mouseUnderPerson(self)
def mouseUnderPerson(self):
    #move mouse to under person
    moveMouse(returnInt(698, 709), returnInt(546, 556))
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
def temp(self):
    for x in range (16):
        moveMouse(randomInSquare(675),randomInSquare(545))
        time.sleep(random.uniform(1.2,1.4))
        mouse.click(self.button)
        time.sleep(random.uniform(1.8,2))
        moveMouse(randomInSquare(699),randomInSquare(569))
        time.sleep(random.uniform(1.2,1.4))
        mouse.click(self.button)
        time.sleep(random.uniform(3,4.2))
def depositAll(self):
    #deposit all
    moveMouse(returnInt(688,710), returnInt(612,632))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.8, 1.2))

def mineIronOreAndBank(self):
    temp(self)
    #click connector square
    moveMouse(randomInSquare(1207), randomInSquare(392))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(16,18))
    #bank box
    moveMouse(randomInSquare(1032), randomInSquare(523))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    #deposit all
    moveMouse(randomInSquare(655), randomInSquare(567))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.8, 1.2))
    #connector
    moveMouse(randomInSquare(314), randomInSquare(584))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    #first ore
    moveMouse(randomInSquare(214), randomInSquare(729))
    time.sleep(random.uniform(.8, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(16,18))


# alkarhid power mining
def iron(self):
    for ii in range(8):
        moveMouse(returnInt(696, 709), returnInt(566, 574))
        waitClickWait(self, 2, 2.5)
        moveMouse(returnInt(670, 685), returnInt(541, 555))
        waitClickWait(self, 2, 2.5)
        moveMouse(returnInt(696, 709), returnInt(518, 532))
        waitClickWait(self, 2, 2.5)
    dropInventory(self)


columnNums = [1079,1099,1119,1143,1165,1187,1210,1226]
rowNums = [523,542,563,582,601,614,635,651,672,689,710,724,740,758]
lastColSlot=[columnNums[6],columnNums[7]]
lastRowSlot=[rowNums[12],rowNums[13]]
global firstTime
def minnows(self,counter ):
    for x in range(4):
        #click
        #wait 15.6 seconds
        mouse.click(self.button)
        if counter != 0 and x==0:
            time.sleep(random.uniform(13.5,13.55))
            print('timer1')
            #time.sleep(13.53)
        else:
            time.sleep(random.uniform(14.27,14.3))
            print('timer2')
            #time.sleep(14.27)
        #move left
        if x !=3:
            moveMouse(returnInt(454, 560), returnInt(300,310))
            time.sleep(random.uniform(0.8, 1))
        #repeat x4
    moveMouse(returnInt(1214, 1315), returnInt(300,310))
    time.sleep(random.uniform(1,1.4))
    mouse.click(self.button)
    return counter +1

def catchNBankKarambwans(self):
    #move mouse to fairy ring
    xVal = returnInt(714, 729)
    yVal = returnInt(714,726)
    moveMouse(xVal, yVal )
    time.sleep(random.uniform(.6, 1.2))
    #right click on fairy ring and configure
    rightClickThridOption(self, xVal, yVal)
    #run to the fairy ring
    time.sleep(random.uniform(3, 4))
    #select locaton in quick select
    moveMouse(returnInt(1236, 1348), returnInt(828,853))
    waitClickWait(self,.6,1.2)
    #select submit center screen
    moveMouse(returnInt(522, 657), returnInt(553,595))
    waitClickWait(self,3,4)
    #click to get bank in frame
    #moveMouse(returnInt(1325, 1336), returnInt(708,715))
    #waitClickWait(self,11,12)
    #click bank
    #moveMouse(returnInt(698, 710), returnInt(657,670))
    #waitClickWait(self,2,4)
    #click bank and wait 11,12
    keyboard.press('e')
    time.sleep(random.uniform(.3, .5))
    keyboard.release('e')
    moveMouse(returnInt(1264, 1276), returnInt(810,821))
    time.sleep(random.uniform(.6,1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.6,1.2))
    keyboard.press('e')
    time.sleep(random.uniform(.1, .3))
    keyboard.release('e')
    time.sleep(random.uniform(11, 12))
    #click item with all selected to bank all karams
    moveMouse(returnInt(columnNums[6], columnNums[7]), returnInt(rowNums[6], rowNums[7]))
    waitClickWait(self,2,4)
    #click to get ring in frame
    #moveMouse(returnInt(30, 49), returnInt(331,345))
    #waitClickWait(self,11,12)
    #move mouse to fairy ring
    xVal = returnInt(0, 14)
    yVal = returnInt(242,258)
    moveMouse(xVal, yVal )
    time.sleep(random.uniform(.6,1.2))
    #right click on fairy ring and configure
    rightClickThridOption(self, xVal, yVal)
    time.sleep(random.uniform(11,12))
    #select locaton in quick select
    moveMouse(returnInt(1236, 1345), returnInt(792,811))
    waitClickWait(self,.6,1.2)
    #select submit center screen
    moveMouse(returnInt(522, 657), returnInt(553,595))
    waitClickWait(self,3,4)
    #move mouse to fishing spot
    moveMouse(returnInt(674, 687), returnInt(382,393))

    time.sleep(random.uniform(0.8, 1))
    #click and fish for 2 minutes
    waitClickWait(self,115,120)
#zoomed all the way in then scroll 5 ticks out. Stand on start spot and
#camera should barely be fully on the screen
def fruitStalls(self):
    for i in range(np.random.randint(7,8)):
        #run to second stall
        moveMouse(returnInt(1148,1229), returnInt(364,440))
        time.sleep(random.uniform(0.1, .2)) #random.uniform(0.3, .5)
        mouse.click(self.button)
        #run back to start
        time.sleep(random.uniform(3,3.2))
        moveMouse(returnInt(32,106), returnInt(361,437))
        time.sleep(random.uniform(0.1, .2)) #random.uniform(0.3, .5)
        mouse.click(self.button)
        time.sleep(random.uniform(3,3.23))
    leftClickDropInventory(self)
    time.sleep(random.uniform(0.4, .45)) #random.uniform(0.3, .5)

    #assums x = 14 and bank on steel smithing tab. wearing ice gaunts
def walkingSteelBlastFurnace(self):
    #click last inv spot
    clickSecondInvSlot(self)

    clickFirstBankSpot(self)
    clickSecondBankSpot(self)

    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    #walk to deposit
    moveMouse(randomInSquare(567), randomInSquare(294))
    waitClickWait(self,13,14)

    #walk to collect
    moveMouse(randomInSquare(657), randomInSquare(629))
    waitClickWait(self,6,7)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(0.8, 1))

    # switch to gold gaunts
    clickFirstInvSlot(self)

    time.sleep(random.uniform(0.8, 1))
    #click bank
    moveMouse(randomInSquare(879), randomInSquare(723))
    waitClickWait(self,7,8)

#coal bag in first inv slot and empty
def BlastFurnaceForSteelBars(self):
    for x in range (4):
        #deposit bars
        clickSecondInvSlot(self)
        clickFirstBankSpot(self)
        #grab coal
        clickFirstInvSlot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        #run to deposit
        moveMouse(randomInSquare(522), randomInSquare(208))
        waitClickWait(self,12,13)
        #place coalfrom bag
        keyboard.press(Key.shift)
        clickFirstInvSlot(self)
        keyboard.release(Key.shift)
        moveMouse(randomInSquare(641), randomInSquare(410))
        waitClickWait(self,1,1.3)
        #run to collect
        moveMouse(randomInSquare(592), randomInSquare(477))
        waitClickWait(self,4,5)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(random.uniform(0.8, 1))

        #click bank
        moveMouse(randomInSquare(766), randomInSquare(556))
        waitClickWait(self,5,6)
    clickSecondOrThirdInvSlot(self)
    drinkStam(self,"2")
#assumes ore in spot 2 in bank coal in spot 1. Bag is in inv spot 1 and quantity set to all
def BlastFurnaceForMithBars(self):
    for x in range (3):
        for y in range (3):
            #deposit bars
            clickSecondInvSlot(self)
            #grab addy
            if(y==0):
                #grab coal
                clickSecondBankSpot(self)
            if(y==1 or y==2):
                #grab coal and addy
                clickFirstBankSpot(self)
            if y==2:
                print("2")
            #grab coal
            clickFirstInvSlot(self)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            #run to deposit
            moveMouse(randomInSquare(522), randomInSquare(208))
            waitClickWait(self,8,10)
            #place coalfrom bag
            keyboard.press(Key.shift)
            clickFirstInvSlot(self)
            keyboard.release(Key.shift)
            moveMouse(returnInt(643,654), returnInt(412,421))
            waitClickWait(self,.4,.8)
            #if y==0 run to bank
            if y==0:
                moveMouse(returnInt(724,732), returnInt(591,599 ))
                waitClickWait(self, 7,8)

            #if y!=0
            #run to collect
            else:
                time.sleep(returnInt(2,3))
                moveMouse(randomInSquare(592), randomInSquare(477))
                waitClickWait(self,4,5)
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                time.sleep(random.uniform(0.8, 1))

                # click bank
                moveMouse(randomInSquare(766), randomInSquare(556))
                waitClickWait(self,5,6)
        if returnInt(0,10)>=5:
            clickLastInvSlot(self )
            drinkStam(self,"2")
#assumes starting with full run and coffer filled and goldsmith gaunts on with ice in inv1
def goldBlastFurnace(self):
    for x in range (10):
        #click last inv spot
        clickLastInvSlot(self)

        clickFirstBankSpot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        #run to deposit
        moveMouse(randomInSquare(522), randomInSquare(208))
        waitClickWait(self,12,13)

        #switch to ice gaunts
        clickFirstInvSlot(self)
        time.sleep(random.uniform(0.8, 1))

        #run to collect
        moveMouse(randomInSquare(592), randomInSquare(477))
        waitClickWait(self,4,5)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(random.uniform(0.8, 1))

        # switch to gold gaunts
        clickFirstInvSlot(self)

        time.sleep(random.uniform(0.8, 1))
        #click bank
        moveMouse(randomInSquare(766), randomInSquare(556))
        waitClickWait(self,5,6)
    clickLastInvSlot(self )
    drinkStam(self,"2")
#assumes ore in spot 2 in bank coal in spot 1. Bag is in inv spot 1 and quantity set to all
def BlastFurnaceForAddyBars(self):
    for x in range (5):
        for y in range (2):
            #deposit bars
            clickSecondInvSlot(self)
            #grab addy
            if(y==0):
                #grab coal
                clickSecondBankSpot(self)
            if(y==1 or y==2):
                #grab coal and addy
                clickFirstBankSpot(self)
            if y==2:
                print("2")
            #grab coal
            clickFirstInvSlot(self)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
            #run to deposit
            moveMouse(randomInSquare(522), randomInSquare(208))
            waitClickWait(self,8,10)
            #place coalfrom bag
            keyboard.press(Key.shift)
            clickFirstInvSlot(self)
            keyboard.release(Key.shift)
            moveMouse(returnInt(643,654), returnInt(412,421))
            waitClickWait(self,.4,.8)
            #if y==0 run to bank
            if y==0:
                moveMouse(returnInt(724,732), returnInt(591,599 ))
                waitClickWait(self, 7,8)

            #if y!=0
            #run to collect
            else:
                time.sleep(returnInt(2,3))
                moveMouse(randomInSquare(592), randomInSquare(477))
                waitClickWait(self,4,5)
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                time.sleep(random.uniform(0.8, 1))

                # click bank
                moveMouse(randomInSquare(766), randomInSquare(556))
                waitClickWait(self,5,6)
        if returnInt(0,10)>=6:
            clickLastInvSlot(self )
            drinkStam(self,"2")
def BlastFurnaceForSteelBarsWalking(self):
    for x in range(5):
        # deposit bars
        clickSecondInvSlot(self)
        # grab iron ore
        clickFirstBankSpot(self)
        # grab coal
        clickFirstInvSlot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        # grab coal
        clickFirstInvSlot(self)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        # walk to deposit
        moveMouse(randomInSquare(567), randomInSquare(294))
        waitClickWait(self, 15, 16)

        #place coalfrom bag
        keyboard.press(Key.shift)
        clickFirstInvSlot(self)
        keyboard.release(Key.shift)
        moveMouse(randomInSquare(720), randomInSquare(546))
        waitClickWait(self,.4,.8)
        # walk to collect
        moveMouse(randomInSquare(657), randomInSquare(629))
        waitClickWait(self, 6, 7)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(random.uniform(0.8, 1))

        # click bank
        moveMouse(randomInSquare(879), randomInSquare(723))
        waitClickWait(self, 9, 10 )

def clickFirstBankSpot(self):
    moveMouse(returnInt(340,351), returnInt(112,124))
    waitClickWait(self,1.3, 1.6)
def clickSecondBankSpot(self):
    moveMouse(returnInt(389,404), returnInt(109,124))
    waitClickWait(self,1.3, 1.6)
def clickThirdBankSpot(self):
    moveMouse(returnInt(432,452), returnInt(109,124))
    waitClickWait(self,1.3, 1.6)
def emptyInventoryInBank(self):
    moveMouse(returnInt(692,713),returnInt(614,631) )
    waitClickWait(self,1,2)
def mineSalts1(self):

    moveMouse(returnInt(571,644), returnInt(209,279))
    waitClickWait(self,9,13)
    moveMouse(returnInt(572,638), returnInt(526,584))
    waitClickWait(self,9,14)
def mineSalts2(self):

    moveMouse(returnInt(901,955), returnInt(559,618))
    waitClickWait(self,9,15)
    moveMouse(returnInt(302,358), returnInt(572,617))
    waitClickWait(self,10,17)
def mlmTopFloor(self):
    #empty inventory
    emptyInventoryInBank(self)
    #press esc
    keyboard.press(Key.esc)
    time.sleep(random.uniform(.1,.2))
    keyboard.release(Key.esc)
    #click ladder
    moveMouse(returnInt(527,537), returnInt(272,277))
    waitClickWait(self,6,7)
    #click first ore spot
    moveMouse(returnInt(463,469), returnInt(248,264))
    waitClickWait(self,50,60)
    #waitClickWait(self,10,12)
    #2nd
    moveMouse(returnInt(620,632), returnInt(429,440))
    waitClickWait(self,36,39)
    #click first ore spot
    moveMouse(returnInt(601,610), returnInt(415,423))
    waitClickWait(self,36,39)
    #2nd,
    moveMouse(returnInt(620,632), returnInt(429,440))
    waitClickWait(self,37,39)
    #click first ore spot
    moveMouse(returnInt(601,610), returnInt(415,423))
    waitClickWait(self,36,39)
    #2nd,
    moveMouse(returnInt(620,632), returnInt(429,440))
    waitClickWait(self,37,39)
    
    #waitClickWait(self,3,4)
    #third
    #moveMouse(returnInt(640,649), returnInt(431,438))
    #waitClickWait(self,32,35)
    #waitClickWait(self,3,4)

    #waitClickWait(self,1,2)
    #4th
    #moveMouse(returnInt(644,652), returnInt(431,437))
    #waitClickWait(self,33,35)
    #waitClickWait(self,3,4)

    #click ladder
    moveMouse(returnInt(742,749), returnInt(568,573))
    waitClickWait(self,10,11)
    #click hopper
    moveMouse(returnInt(493,506), (returnInt(416,424)))
    waitClickWait(self,7,10)
    #click sack
    moveMouse(returnInt(605,612), (returnInt(646,652)))
    time.sleep(random.uniform(.4,.55))
    mouse.click(self.button)
    waitClickWait(self,7,9)
    #click bank1
    moveMouse(returnInt(840,848), (returnInt(285,292)))
    waitClickWait(self,7,9)
    #click sack
    if(returnInt(1,10)>9):
        depositAll(self)
        clickEsc(self)
        moveMouse(returnInt(416,425), (returnInt(537,545)))
        waitClickWait(self,5,6)
        #click bank1
        moveMouse(returnInt(840,848), (returnInt(285,292)))
        waitClickWait(self,7,9)
def doubleClick(self):
    time.sleep(random.uniform(.08, .1))
    mouse.click(self.button)

#assumes zoomed in and walking from north to position camera
#butler called and on the square behind144
def mythCapesWButler(self):
    # build 7 racks remove each one
    for i in range(8):
        xval = returnInt(613, 681)
        yval = returnInt(498, 512)
        moveMouse(xval, yval)
        time.sleep(random.uniform(.3, .6))
        rightClickThridOption(self, xval, yval)

        time.sleep(random.uniform(.6, 1))
        # press 4
        keyboard.press('4')
        time.sleep(random.uniform(.3, .6))
        keyboard.release('4')

        time.sleep(random.uniform(.6, 1))
        xval = returnInt(621, 672)
        yval = returnInt(490, 511)
        moveMouse(xval, yval)
        time.sleep(random.uniform(.6, 1))
        rightClickForthOption(self, xval, yval)

        time.sleep(random.uniform(.6, 1))
        keyboard.press('1')
        time.sleep(random.uniform(.3, .6))
        keyboard.release('1')
        time.sleep(random.uniform(.3, .6))

    #click butler 2x
    moveMouse(returnInt(622,666), returnInt(263,288))
    time.sleep(random.uniform(.3, .6))
    mouse.click(self.button)
    time.sleep(random.uniform(1,2))
    mouse.click(self.button)

    #retrieve more planks
    time.sleep(random.uniform(1,2))
    keyboard.press('1')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('1')
    time.sleep(random.uniform(.3, .6))
    #wait 8 sec

    moveMouse(returnInt(448,515), returnInt(78,148))
    time.sleep(random.uniform(1,2))
    mouse.click(self.button)
    moveMouse(returnInt(728,798), returnInt(683,744))
    time.sleep(random.uniform(5,6))

    #pay if needed1
    clickSpace(self)
    keyboard.press('1')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('1')
    time.sleep(random.uniform(1,2))
    clickSpace(self)
    time.sleep(random.uniform(1,2))

    mouse.click(self.button)
    time.sleep(random.uniform(2,3))

    #exit()

def mythCapes(self):
    #run to spot
    moveMouse(returnInt(588,602), returnInt(362,372))
    waitClickWait(self,3,4)
    #build 7 racks remove each one
    for i in range(7):
        #move mouse to wall
        xval = returnInt(623,632)
        yval = returnInt(419,422)
        moveMouse(xval, yval)
        time.sleep(random.uniform(.3,.6))
        rightClickThridOption(self,xval,yval)

        time.sleep(random.uniform(.6,1))
        #press 4
        keyboard.press('4')
        time.sleep(random.uniform(.3,.6))
        keyboard.release('4')

        time.sleep(random.uniform(.6,1))
        xval = returnInt(623,631)
        yval = returnInt(421,422)
        moveMouse(xval, yval)
        time.sleep(random.uniform(.6,1))
        rightClickForthOption(self,xval,yval)

        time.sleep(random.uniform(.6,1))
        keyboard.press('1')
        time.sleep(random.uniform(.3,.6))
        keyboard.release('1')
        time.sleep(random.uniform(.3,.6))
    #click portal then exit
    time.sleep(random.uniform(.3,.6))
    moveMouse(returnInt(670,679), returnInt(487,510))
    waitClickWait(self,4,5)

    clickFirstInvSlot(self)
    moveMouse(randomInSquare(607), randomInSquare(557))
    exit()

#assumes north faceing zoomed out camera
#set quantity to all, wear full gracefull dumbass
def runPlanks(self):
    for i in range(2):
        # click first bank spot
        clickFirstBankSpot(self)
        # click square
        # wait while running
        moveMouse(randomInSquare(860), randomInSquare(77))
        waitClickWait(self, 12, 13)
        # click sawmill dude
        moveMouse(returnInt(891, 906), returnInt(396, 400))
        waitClickWait(self, 8, 9)
        # click space
        clickSpace(self)
        # click square
        # wait while running
        moveMouse(returnInt(63, 78), returnInt(527, 540))
        waitClickWait(self, 10, 12)
        # click bank
        moveMouse(returnInt(495, 504), returnInt(778, 783))
        waitClickWait(self, 8, 10)
        # click second inv spot
        clickSecondInvSlot(self)

    drinkStam(self,'2')
    # moveMouse(returnInt(626, 633), returnInt(434, 442))
    # waitClickWait(self, .2,.4)
    # for i in range(2):
    #     #click second inv spot
    #     clickSecondInvSlot(self)
    #     #click first bank spot
    #     clickFirstBankSpot(self)
    #     #click square
    #     #wait while running
    #     moveMouse(randomInSquare(860), randomInSquare(77))
    #     waitClickWait(self,24,25)
    #     #click sawmill dude
    #     moveMouse(returnInt(891,906), returnInt(396,400))
    #     waitClickWait(self,14,15)
    #     #click space
    #     clickSpace(self)
    #     #click square
    #     #wait while running
    #     moveMouse(returnInt(63,78), returnInt(527,540))
    #     waitClickWait(self,20,21)
    #     #click bank
    #     moveMouse(returnInt(495,504), returnInt(778,783))
    #     waitClickWait(self,17,18)
    #
    # toggleRun(self)
    # moveMouse(returnInt(626, 633), returnInt(434, 442))
    # waitClickWait(self, .2,.4)
def hosidiousCookingBot(self):
    #empty inventory
    emptyInventoryInBank(self)
    #click karams
    moveMouse(returnInt(413,430), returnInt(151,167))
    waitClickWait(self,1.3, 2.5)
    #press esc
    keyboard.press(Key.esc)
    time.sleep(random.uniform(.3,.6))
    keyboard.release(Key.esc)
    #click range and run there

    moveMouse(returnInt(738,748), returnInt(408,420))
    waitClickWait(self,3.7,3.9)
    #click option 2
    #keyboard.press("2")
    keyboard.press(Key.space)
    time.sleep(random.uniform(.3,.6))
    #keyboard.release("2")
    keyboard.release(Key.space)
    #cook and wait
    time.sleep(random.uniform(64,67))
    #move mouse to bank
    moveMouse(returnInt(656,664), returnInt(679,688))
    waitClickWait(self,3.4,3.6)

#stand west of tree and camera points north. zoom in all the way
def teakCutNFletch(self):
    #click 5 times
    for i in range(7):
        waitClickWait(self,15,20);
    #click last inv spot
    clickLastInvSlot(self)
    #click first inv spot
    clickFirstInvSlot(self)
    #click space
    keyboard.press(Key.space)
    time.sleep(random.uniform(40, 45))
    #drop inv
    dropInventory(self)

    #click tree
    moveMouse(returnInt(832,949), returnInt(515,641))

def rightClickThridOption(self,xVal,yVal):
    mouse.click(self.button.right)
    time.sleep(random.uniform(.6, 1.2))
    # move mouse down to configure X pixels down from the saved location
    newxVal = xVal + random.uniform(-38, 30)
    if (newxVal < 5):newxVal=5
    moveMouse(newxVal, yVal + random.uniform(53, 60))
    time.sleep(random.uniform(.6, 1.2))
    mouse.click(self.button)
    time.sleep(random.uniform(.6, 1.2))
def rightClickForthOption(self,xVal,yVal):
    mouse.click(self.button.right)
    time.sleep(random.uniform(.6, 1.2))
    # move mouse down to configure X pixels down from the saved location
    newxVal = xVal + random.uniform(-12, 47)
    if (newxVal < 5):newxVal=5
    moveMouse(newxVal, yVal + random.uniform(68, 73))
    time.sleep(random.uniform(.6, .9))
    mouse.click(self.button)
    time.sleep(random.uniform(.3, .6))
def tickManipulate(self):
    # click inv spot one
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.48, .62))  # random.uniform(0.3, .5)
    mouse.click(self.button)
    # click inv spot 5
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[2], rowNums[3]))
    time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
    mouse.click(self.button)  # start herb animation
def drop3tItems(self):
    # click inv spot 9
    if (random.uniform(0, 10) > 2):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
        mouse.click(self.button)
    # 10% chance to click inv spot 10
    if (random.uniform(0, 10) > 100):
        moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
        mouse.click(self.button)
    # 50% chance to click inv spot 13
    if (random.uniform(0, 10) > 100):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[6], rowNums[7]))
        time.sleep(random.uniform(0.2, .25))  # random.uniform(0.3, .5)
        mouse.click(self.button)
def threeTickFish(self):
    tickManipulate(self)
    drop3tItems(self)
    #click inv spot 9
    if(random.uniform(0,10)>2):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
        mouse.click(self.button)
    #10% chance to click inv spot 10
    if(random.uniform(0,10)>9):
        moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[4], rowNums[5]))
        time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
        mouse.click(self.button)
    #50% chance to click inv spot 13
    if(random.uniform(0,10)>9):
        moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[6], rowNums[7]))
        time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
        mouse.click(self.button)
    #click fishing spot
    moveMouse(returnInt(1040,1132), returnInt(856,928))
    time.sleep(random.uniform(0.2, .25)) #random.uniform(0.3, .5)
    mouse.click(self.button)
    time.sleep(random.uniform(0.2 ,.3))
def fishAndDropInv(self):
    dropInventory(self)

    time.sleep(random.uniform(.4,.6))
    moveMouse(returnInt(722, 731), returnInt(547,556))

    time.sleep(random.uniform(.6,1.2))
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(5,6):
        mouse.click(self.button)
        # tenPercentChanceOfE()
        time.sleep(random.uniform(15, 20))
        counter += 1

def clickAndDropInv(self):
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(13, 14):
        mouse.click(self.button)
        delay = np.random.randint(15, 18)
        # tenPercentChanceOfE()
        time.sleep(random.uniform(.3, 1))
        counter += 1
    dropInventory(self)

    moveMouse(returnInt(722, 731), returnInt(547,556))
    delay = np.random.randint(2, 3)
def clickAndFletchIntoShafts(self):
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(17,20):
        mouse.click(self.button)
        delay = np.random.randint(5,8)
        # tenPercentChanceOfE()
        time.sleep(delay)
        counter += 1
    #dropInventory(self)
    clickLastSlot(self)
    clickFirstInvSlot(self)
    keyboard.press(Key.space)
    time.sleep(random.uniform(.3, 1))
    keyboard.release(Key.space)
    time.sleep(random.uniform(25, 35))
    #dropInventory(self)
    moveMouse(returnInt(729, 738), returnInt(538, 548))
    time.sleep(random.uniform(.3, 1))
    moveMouse(returnInt(702, 709), returnInt(581, 591))
    time.sleep(random.uniform(.3, 1))


def clickAndFletchIntoBows(self):
    counter = 0
    # click randomly for a few minutes
    while counter < returnInt(17,20):
        mouse.click(self.button)
        delay = np.random.randint(5,8)
        # tenPercentChanceOfE()
        time.sleep(delay)
        counter += 1
    #dropInventory(self)
    clickLastSlot(self)
    clickFirstInvSlot(self)
    keyboard.press(Key.space)
    time.sleep(random.uniform(.3, 1))
    keyboard.release(Key.space)
    time.sleep(random.uniform(30, 40))
    dropInventory(self)
    moveMouse(returnInt(747, 761), returnInt(547, 556))
    time.sleep(random.uniform(.3, 1))

def waitClick(self):
    time.sleep(random.uniform(0.8, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(0.8, 1))
def waitClickWait(self,min,max):
    time.sleep(random.uniform(0.6, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(min, max))

def clickFirstInvSlot(self):
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickMiddleInvSlots(self):
    moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[6], rowNums[7]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    moveMouse(returnInt(columnNums[4], columnNums[5]), returnInt(rowNums[6], rowNums[7]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickSecondInvSlot(self):
    moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickThirdInvSlot(self):
    moveMouse(returnInt(columnNums[4], columnNums[5]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickSecondOrThirdInvSlot(self):
    if(random.uniform(0,10)>2  ):
        clickThirdInvSlot(self)
    else:
        clickSecondInvSlot(self)
def clickLastInvSlot(self):
    moveMouse(returnInt(columnNums[6], columnNums[7]), returnInt(rowNums[12], rowNums[13]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
def clickLastSlot(self):
    moveMouse(returnInt(lastColSlot[0], lastColSlot[1]), returnInt(lastRowSlot[0], lastRowSlot[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(1.3, 1.8))

def clickInventory(self):
    #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            waitClickWait(self)
def leftClickDropInventory(self):
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.27, .32))
            mouse.click(self.button)
    time.sleep(random.uniform(.4,.6))
def mmDropInventory(self):
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.27, .32))
            if (i == 3 and ii == 5):
                keyboard.press(Key.shift)
                time.sleep(random.uniform(.3,.4))
                mouse.click(self.button)
                time.sleep(random.uniform(.3,.4))
                mouse.click(self.button)
                time.sleep(random.uniform(.3,.4))

                keyboard.release(Key.shift)
            else:
                mouse.click(self.button)
    time.sleep(random.uniform(.4,.6))
def leftClickHalfInventory(self):
    for i in range(4):
        for ii in range(3):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.27, .32))
            mouse.click(self.button)
    time.sleep(random.uniform(.4,.6))
def dropInventory(self):
    #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    keyboard.press(Key.shift)
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.2, .3))
            mouse.click(self.button)
    keyboard.release(Key.shift)
    time.sleep(random.uniform(.4,.6))
def openPacks(self):   #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.2, .3))
            mouse.click(self.button)
    time.sleep(random.uniform(.4,.6))
    click_thread.stop_clicking()
    #assumes 10 waterskins and runs for cast
def mineSandstone(self):
    #mine 4 rocks 3 times
    #moveMouse(randomInSquare(696), randomInSquare(564))
    #waitClickWait(self, .6,1)
    for i in range(6):
        moveMouse(returnInt(607,615), returnInt(433,442))
        waitClickWait(self, 2.7,3.5)
        moveMouse(returnInt(584,593), returnInt(414,421))
        waitClickWait(self, 2.7,3.9)
        moveMouse(returnInt(603,608), returnInt(395,400))
        waitClickWait(self, 2.7,3.6)
        #click first one
        moveMouse(returnInt(656,664), returnInt(447,453))
        waitClickWait(self, 4.2,4.4)
    #deposit into grinder

    moveMouse(returnInt(272,297), returnInt(515,528))
    waitClickWait(self, 7,9)
    #click first rock
    moveMouse(returnInt(870,876), returnInt(368,373))
    waitClickWait(self, 10,12)
def turnOffBot(self):
    keyboard.press('=')
    time.sleep(random.uniform(.2,.5))
    keyboard.release('=')
def dropInventory2(self):
    #moveMouse(returnInt(columnNums[2], columnNums[3]), returnInt(rowNums[0], rowNums[1]))
    #keyboard.press(Key.shift)
    for i in range(4):
        for ii in range(7):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            #clickLastSlot(self)
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]),returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.2, .3))
            mouse.click(self.button)
            time.sleep(random.uniform(0.1,.15))
            mouse.click(self.button)
    #keyboard.release(Key.shift)
    time.sleep(random.uniform(.4,.6))
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
def pause(self):
    click_thread.stop_clicking()
def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
    elif key == kill_key:
        click_thread.kill_clicking()
        listener.stop()

def exit():
    click_thread.exit()
    listener.stop()
with Listener(on_press=on_press) as listener:
    listener.join()
