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
#import pyautogui#not for avg bot

everyMinute = 60
buttonLeftClick = pyB.left
buttonRightClick = pyB.right
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='+')
kill_key = KeyCode(char='-')

counter = 0
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
            while self.running  :

                #if (counter < 215):
                counter = counter +1
                    #print(counter)
                #@@@@@@@@@@@@@@@@@@@@@
            #agility-------------------------------agility
                #canifisAgilCourse(self)
                #seersCourse(self)
                #rellekkaCourse(self)
                #colorTest(self)
                #prifAgil(self)
                #prifAgilWithHA(self)
                #ardyCourse(self)
                #ardyCourseHA(self)

            #cooking-------------------------------cooking
                #catchNBankKarambwans(self)
                #hosidiousCookingBot(self)
                #mythCooking(self)
                #makeWines(self)
                #humidifyJugs(self)
            # combat -------------------------------combat
                #prayerFlickAutoClick(0,self)
                #nmz(self)
                #cannonAutoClicker(self,30,35)
            #construction-------------------------------construction
                #runPlanks(self)
                #makeTablets(self)
                #toggleRun(self)
                #plankMake(self)
                #mythCapesWButler(self)
                #mahogTables(self)
                #plankMakeSpell(self)
            #crafting-------------------------------crafting
                #cookSeaweedAtFT(self)
                #edgevilleFurnace(self)
                #edgevilleFurnace2Item(self)
                #craftOrFletchWKnife(self)
                #fourteenFourteenCraft(self)
                #spinFlax(self)
                #lunarSpinFlax(self)
                #superGlassmake(self)
                #pickUpFromGround(self)
            #fishing-------------------------------fishing
                #counter = minnows(self,counter)
                #fishAndDropInv(self)
                #threeTickFish(self)
                #zulrahScales(self)
            #farming-------------------------------farming
                #titheFarm(self)
                #plantSapplings4kStreched(self)
                #plantSapplings(self)
            #firemaking-------------------------------firemaking
                #fireLines(self)
                #lightFire(self)
            #firemaking-------------------------------firemaking
                #burnInv(self)

            #fletching-------------------------------fletching
                #broads(self)
                #bolts(self)
                #teakCutNFletch(self)
                #craftOrFletchWKnife(self)
                #enchantBolts(self)
                #fletchDartsLastInvSlot4k(self)
                #plantSapplings(self)

            #Herb-------------------------------herb
                #cleanHerbs(self)
                #makePots(self)
                #makeCombats(self)
                #makePotsWithUnfs(self)
                #openPacks(self)

                #craftOrFletch(self) #stams
                #birdNest(self)
                #gatherMortFungi(self)
            # Hunter-------------------------------Hunter
                #maniMonkeys(self)
                #just for dropping
                #mmDropInventory(self)
            #mining-------------------------------mining
                #quick60to120RandomAutoClicker(self)
                #amethyst(self)
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
                #caveKracken(self)
                #mageTrainingArenaGraveyard(self)
                #mageTrainingArenaEnchant(self)
            #range-------------------------------range
            #prayer-------------------------------prayer
                #basicReanimation(self)
                #adeptReanimation(self)
                #expertReanimation(self)
                #masterReanimation(self)
                #wildyAlter(self)
            #melee-------------------------------melee
                #amaniteCrabs2(self)
                #amaniteCrabs3(self)
                #afkDags(self)
            #runecrafting-------------------------------runecrafting
                #runBloo-=-ds(self)
                runSouls(self)
                #tempSouls(self)
                #zmi(self)
                #findLadder(self)
                #pixelRangeTest(self)
            #thieving-------------------------------thieving
                #ardyKnights(self)
                #fruitStalls(self)
                #masterFarmerHouseLure(self)
                #masterFarmerGuild(self)
            #smithing-------------------------------smithing
                #prifSmith(self)
                #walkingSteelBlastFurnace(self)
                #goldBlastFurnace(self)
                #BlastFurnaceForMithBars(self)
                #BlastFurnaceForAddyBars(self)
                #BlastFurnaceForRuneBars(self)
                #BlastFurnaceForSteelBars(self)
                #runCannonBalls(self)
                #varrockSmithing(self)
                #edgevilleFurnace(self)
                #pixelRangeTest(self)
                #buyBlastFurnaceOres(self)
                #drinkStam(self)
            #woodcutting-------3------------------------woodcutting
                #clickAndFletchIntoShafts(self)
                #clickAndFletchIntoBows(self)
                #cutFossilIslandTreesAndBank(self)
                #cutFossilIslandTest(self)
                #yewsAndBank(self)
                #blisterwood(self)
                #redwoods(self)
                #redwoodsBonfire(self)
                #blisterwoodBonfire(self)
                #clickBonfireFeet(self)
            #multiUse-------------------------------multiUse

                #pixelRangeTest(self)
                #quick10through15RandomAutoClicker(self)
                #autoClicker(self,45,60)
                #cannonAutoClicker(self,60,120)
                #cannonAutoClicker(self,.3,.6)
                #emptyInventoryInBank(self)
                #clickAndDropInv(self)
                #leftClickDropInventory(self)
                #openPacks(self)
                #checkRange(self)
                #dropInventory(self)
                #quickAFRandomAutoClicker(self)
                #highAlch(self)
                #sellItemsToShop(self)

                #leagues
                #varrockSmithing(self)
                #quickAFRandomAutoClicker(self)

                #lumbymith(self)
                #lumbyaddy(self)
                #fossilRune(self)
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
    num = np.random.randint(minInt, maxInt)
    print(num)
    return num

def returnFloat(minF, maxF):
    num = np.random.uniform(minF, maxF)
    print(num)
    return num

def moveMouse(x,y):
    mouse.position = (x+5, y)

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
def lumbymith(self):
    moveMouse(returnInt(592, 660), returnInt(541, 608))

    waitClickWait(self, 7,8)
    moveMouse(returnInt(428, 500), returnInt(373, 451))

    waitClickWait(self, 7,8)
    moveMouse(returnInt(577, 656), returnInt(212, 280))

    waitClickWait(self, 7,8)
def fossilRune(self):
    if(returnInt(1,25)>20):
        spec(self)
    moveMouse(returnInt(608, 615), returnInt(466, 472))

    waitClickWait(self, 9,12)
    moveMouse(returnInt(660, 670), returnInt(380, 385))

    waitClickWait(self, 9,12)
def lumbyaddy(self):
    if(returnInt(1,25)>20):
        spec(self)
    moveMouse(returnInt(428, 500), returnInt(373, 451))

    waitClickWait(self, 9,10)
    moveMouse(returnInt(577, 656), returnInt(212, 280))

    waitClickWait(self, 9,10)

def quick10through15RandomAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(10,15)
    # tenPercentChanceOfE()
    time.sleep(delay)
def prayerFlickAutoClick(tick,self):
    mouse.click(self.button)
    time.sleep(random.uniform(.5,.59))
    mouse.click(self.button)
def quick60to120RandomAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(60,120)
    # tenPercentChanceOfE()
    time.sleep(delay)
#assumes ligned up 4 ores
def amethyst(self):
    mouse.click(self.button)
    delay = np.random.randint(15,25)
    # tenPercentChanceOfE()
    time.sleep(delay)
#bank set to all standing infront of bank with empty inv. GP  not in first or last slot
#zoomed out camera. WEAR GRACEFUL. have tab on 1 to grab stams
def buyBlastFurnaceOres(self):
    #runs before drinking stam
    for ii in range (4):
        #runs per world
        for i in range (4):
            #move mouse to ore guy
            moveMouse(returnInt(413, 419), returnInt(256, 260))

            waitClickWait(self,5,6)
            #move mouse to gold
            moveMouse(returnInt(582, 597), returnInt(237, 250))
            waitClick(self)
            #move mouse to iron
            moveMouse(returnInt(437, 451), returnInt(236, 252))
            waitClick(self)
            #move mouse to bank
            moveMouse(returnInt(838, 851), returnInt(573, 584))
            waitClickWait(self,5,6)
            clickFirstInvSlot(self)
            clickLastInvSlot(self)
            clickEsc(self)
        switchWorlds(self)
        time.sleep(random.uniform(10,11))
        keyboard.press('e')
        keyboard.release('e')

    # move mouse to bank
    moveMouse(returnInt(624, 635), returnInt(434, 443))
    drinkStam(self,"1")
    clickEsc(self)


# Define window coordinates (scaled)
window_top_left = (645,37)#(572, 38)
window_bottom_right = (1111,957)#(764, 805)

SKIP_PIXELS = 20
GREEN_THRESHOLD = 130
GREEN_THRESHOLD = 130
# Function to check if pixel color is green
def is_green(pixel):
    return pixel[1] > GREEN_THRESHOLD and pixel[0] < 100 and pixel[2] < 100

# Function to check if pixel color is green
def is_black(pixel):
    return pixel[1] < 15 and pixel[0] < 15 and pixel[2] < 15

def zulrahScales(self):
    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Iterate through screen coordinates, skipping pixels each time
    green_found = False
    for y in range(window_top_left[1], window_bottom_right[1], SKIP_PIXELS):
        for x in range(window_top_left[0], window_bottom_right[0], SKIP_PIXELS):
            pixel = screenshot.getpixel((x, y))
            if is_green(pixel):
                time.sleep(returnInt(1, 2))
                # Calculate actual mouse position based on screen coordinates
                mouse.position = (x, y)
                mouse.click(pyB.left)
                time.sleep(returnFloat(.1,.2))
                mouse.click(pyB.left)
                time.sleep(0.0001)  # Adjust as necessary to avoid rapid clicking
                print("Green found at:", x, y)
                green_found = True
                break  # Break out of the inner loop
        if green_found:
            break  # Break out of the outer loop if green pixel was found

    #time.sleep( returnInt(120,180))  # Wait for a specified time

    total_wait_time = returnInt(60, 80)
    elapsed_time = 0
    CHECK_INTERVAL = returnInt(9,12)
    while elapsed_time < total_wait_time:
        time.sleep(CHECK_INTERVAL)
        elapsed_time += CHECK_INTERVAL

        screenshot = pyautogui.screenshot()
        x_check = 1522
        y_check = 942
        pixel = screenshot.getpixel((x_check, y_check))
        if is_green(pixel):
            for i in range(returnInt(25, 27)):
                plantSapplingsPysical(self)
            break  # Exit the loop if green pixel was found
        else:
            print("No green found at:", x_check, y_check)
    t = returnInt(60, 80)
    if elapsed_time >= total_wait_time:
        if(t - elapsed_time >0):
            time.sleep(t - elapsed_time)


def prifSmith(self):
    clickSecondOrThirdInvSlot(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    #click anvil
    moveMouse(returnInt(480, 490), returnInt(505, 512))
    waitClickWait(self, 5, 6)
    clickSpace(self)
    #plates
    #sleep(returnInt(15,17))
    sleep(returnInt(60,65))
    #click bank
    moveMouse(returnInt(768, 779), returnInt(322, 328))
    waitClickWait(self, 5, 6)
#camera north zoomed in
def makeWines(self):
    # empty inv
    emptyInventoryInBank(self)
    # grab herb and water
    clickFirstBankSpot(self)
    clickSecondBankSpot(self)
    clickEsc(self)
    # mix
    clickMiddleInvSlots(self)
    time.sleep(random.uniform(.82, .94))
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(random.uniform(16,17))
    # bank
    clickCraftingGuildBank(self)

#bank set to all,camera east
#rune pouch in inv, mory legs + graceful,flail
#equipment open
def gatherMortFungi(self):
    print("loop 1 int (3,4):")
    for iii in range (returnInt(3,4)):
        #tele to start
        moveMouse(returnInt(1150, 1166), returnInt(563, 580))
        waitClickWait(self, 3,4)
        #run to logs
        moveMouse(returnInt(252, 259), returnInt(153, 159))
        waitClickWait(self, 16,17)
        print("loop 2 int (3,4):")
        for ii in range(returnInt(3,4)):
            #click bloom two or 3 times

            print("bloom and pick")
            for i in range(returnInt(2,4)):
                moveMouse(returnInt(1094, 1109), returnInt(605, 612))
                waitClickWait(self, 2.2,2.5)
            #pick up items and return to starting spot
            #SE
            moveMouse(returnInt(642, 652), returnInt(396, 404))
            waitClickWait(self, .6,.8)
            #NW
            moveMouse(returnInt(612, 615), returnInt(449, 456))
            waitClickWait(self, 1,1.2)
            #SW
            moveMouse(returnInt(647, 650), returnInt(419, 421))
            waitClickWait(self, .7,.8)
            #N
            moveMouse(returnInt(628, 631), returnInt(379, 388))
            waitClickWait(self, .7,.8)
        #tele back to bank
        moveMouse(returnInt(1148, 1171), returnInt(561, 583))
        waitClickWait(self, 3,4)
        #click bank
        moveMouse(returnInt(1029, 1045), returnInt(359, 386))
        waitClickWait(self, 7,8)
        clickSecondOrThirdInvSlot(self)
        clickEsc(self)
    teleToPoh(self)
    #open inv back up
    keyboard.press('3')
    time.sleep(random.uniform(0.2, .3))
    keyboard.release('3')
    #Click pool
    moveMouse(returnInt(563, 572), returnInt(461, 471))
    time.sleep(random.uniform(2,3))
    waitClickWait(self, 3,4)

def teleToPoh(self):
    # tele to poh
    keyboard.press('f')
    time.sleep(random.uniform(0.2, .3))
    keyboard.release('f')
    time.sleep(random.uniform(0.2, .3))
    moveMouse(returnInt(1103, 1112), returnInt(590, 599))
    waitClickWait(self, 2,3)

#camera north zoomed in spellbook open
def humidifyJugs(self):
    clickFirstInvSlot(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    #click hummidify
    moveMouse(returnInt(1154, 1168), returnInt(546, 555))
    waitClickWait(self, 2,3)
    clickCraftingGuildBank(self)
#zoom north
def mythCooking(self):
    emptyInventoryInBank(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    moveMouse(returnInt(788, 840), returnInt(355, 467))
    time.sleep(random.uniform(0.6, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(0.6, 1))
    clickSpace(self)
    time.sleep(random.uniform(55,60))
    moveMouse(returnInt(570, 680), returnInt(226, 316))
    waitClickWait(self, .7,.9)

#draw distance at 90
#rune pouch soul, astral, mind, cosmic
#lunar spell book
#bank placeholders on with pouchs in inv
#start at bank
def zmi(self):

    for i in range(2):
        clickFirstBankSpot(self)
        clickFirstInvSlot(self)
    clickFirstBankSpot(self)
    #click alter
    moveMouse(returnInt(173, 201), returnInt(34, 42))
    waitClickWait(self, 31,33)
    #empty click on repeat
    for i in range(2):
        clickFirstInvSlot(self)
        #click alter
        moveMouse(returnInt(560, 594), returnInt(399, 422))
        waitClickWait(self, .7, .9)
    #teleport to oookania
    pressF(self)
    findLadder(self)
    pressE(self)
    #click bank
    moveMouse(returnInt(663, 679), returnInt(346, 351))
    waitClickWait(self, 2.5,3)
    #click deposit all (placeholders on so pouches shouldnt go in)
    depositAll(self)
    #33% chance of eating food and staming
    if(returnInt(0,10)>6):
        drinkStam(self,'2')
        #eat shark
        moveMouse(returnInt(632, 647), returnInt(509, 522))
        waitClickWait(self, .3,.4)
        keyboard.press(Key.shift)
        clickSecondInvSlot(self)
        keyboard.release(Key.shift)
def findLadder(self):
    #teleport there
    moveMouse(returnInt(1113, 1124), returnInt(573, 584))
    waitClickWait(self, 4, 5)

    #click fence
    moveMouse(returnInt(1131, 1154), returnInt(422, 436))
    waitClickWait(self, 6.2,7)
    #push against fence
    moveMouse(returnInt(648, 661), returnInt(393, 407))
    waitClickWait(self, .2,.3)
    #click ladder
    moveMouse(returnInt(644, 659), returnInt(25, 28))
    waitClickWait(self, 6.3,6.4)
    #double tap just in case
    moveMouse(returnInt(624, 636), returnInt(397, 403))
    waitClickWait(self, 1,2)


def fullInvOfDark(self):
    mineNmakeDark(self)
    # run back and craft all essence
    moveMouse(returnInt(919, 927), returnInt(548, 563))
    time.sleep(random.uniform(0.6, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(0.6, 1))
    for i in range(returnInt(14, 15)):
        plantSapplings(self)
    # run to half wall while plnting saps
    moveMouse(returnInt(1163, 1175), returnInt(451, 464))
    time.sleep(random.uniform(0.6, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(0.6, 1))
    for i in range(returnInt(13, 14)):
        plantSapplings(self)
    waitClickWait(self, 1, 2)
    sleep(returnInt(1, 2))
    # climb rock
    moveMouse(returnInt(625, 633), returnInt(433, 439))
    waitClickWait(self, 2, 2.2)
    # double click to avoid null pointer
    time.sleep(random.uniform(0.1, .2))
    mouse.click(self.button)
    # click ess
    moveMouse(returnInt(656, 693), returnInt(633, 677))
    waitClickWait(self, 12, 13)
    # mine again
    mineNmakeDark(self)

#camera north, graceful boots and cape on, chisel in second to last inv slot
#starting at north rock
#minimap zoomed out, GPU set to 50
def runSouls(self):
    fullInvOfDark(self)
    #from the alter go to the soul alter
    moveMouse(returnInt(1161, 1171), returnInt(239, 246))
    waitClickWait(self, 12,14)
    moveMouse(returnInt(1243, 1252), returnInt(397, 405))
    waitClickWait(self, 12,14)
    moveMouse(returnInt(1099, 1107), returnInt(434, 443))
    waitClickWait(self, 12,14)
    #click minimapfor alter
    moveMouse(returnInt(1192, 1193), returnInt(176, 179))
    waitClickWait(self, 15,17)
    #click alter
    moveMouse(returnInt(615, 625), returnInt(470, 480))
    waitClickWait(self, 2,3)
    waitClickWait(self, .3,.6)
    #chip again
    for i in range(26):
        plantSapplings(self)
    #click alter again
    moveMouse(returnInt(627, 633), returnInt(434, 437))
    waitClickWait(self, 3,4)
    #run back
    moveMouse(returnInt(1156, 1158), returnInt(40, 42))
    waitClickWait(self, 12,14)
    moveMouse(returnInt(137, 148), returnInt(310, 318))
    waitClickWait(self, 10,11)
    #find and climb wall
    moveMouse(returnInt(624, 630), returnInt(764, 767))
    waitClickWait(self, 7,8)
    moveMouse(returnInt(627, 633), returnInt(434, 437))
    waitClickWait(self, 3,4)
    #run to wall 2 and climb
    moveMouse(returnInt(368, 377), returnInt(534, 544))
    waitClickWait(self, 10,12)
    #click ess to reset
    moveMouse(returnInt(656, 680), returnInt(644, 673))
    waitClickWait(self,10,12)
def tempSouls(self):
    moveMouse(returnInt(1192, 1194), returnInt(176, 179))


#camera north, graceful boots and cape on, chisel in second to last inv slot
#starting at north rock
#minimap zoomed out, GPU set to 50
def runBloods(self):
    fullInvOfDark(self)
    #from the alter go to the blood alter
    moveMouse(returnInt(1213, 1214), returnInt(169, 172))
    waitClickWait(self, 49,52)
    #moveMouse(returnInt(611, 636), returnInt(724, 750))
    #waitClickWait(self, 10,12)
    #click alter
    moveMouse(returnInt(228, 242), returnInt(784, 790))
    waitClickWait(self, 13,15)
    time.sleep(random.uniform(0.6, 1))
    for i in range(25):
        plantSapplings(self)
    #click alter again
    moveMouse(returnInt(568, 593), returnInt(384, 400))
    waitClickWait(self, .5,.8)
    #run back
    moveMouse(returnInt(921, 931), returnInt(103, 110))
    waitClickWait(self, 11,12)
    moveMouse(returnInt(750, 759), returnInt(270, 280))
    waitClickWait(self, 9,10)
    #click ess to reset
    moveMouse(returnInt(816, 855), returnInt(340, 382))
    waitClickWait(self,6,7)
def mineNmakeDark(self):

    spec(self)
    # mine
    moveMouse(returnInt(640, 676), returnInt(350, 388))
    waitClickWait(self, 20, 35)
    for i in range (3):
        #click north rock
        moveMouse(returnInt(640, 694), returnInt(556, 617))
        waitClickWait(self, 33, 35)
        #if(i!=2):
        #click south rock
        moveMouse(returnInt(649, 684), returnInt(244, 279))
        waitClickWait(self, 30, 35)

    # run to first agil spot (if no above if)
    #moveMouse(returnInt(605, 616), returnInt(50, 60))
    #waitClickWait(self, 13, 14)
    #run to almost wall
    #moveMouse(returnInt(588, 597), returnInt(67, 77))
    #waitClickWait(self, 10,11)
    #climb wall
    #moveMouse(returnInt(642, 649), returnInt(319, 329))
    #waitClickWait(self, 5,6)
    #run to wall from north rock
    moveMouse(returnInt(604, 612), returnInt(44, 58))
    waitClickWait(self, 12,13)
    # run halfway to alter
    moveMouse(returnInt(172, 184), returnInt(399, 405))
    waitClickWait(self, 10, 11)
    # run to alter
    moveMouse(returnInt(344, 350), returnInt(275, 293))
    waitClickWait(self, 7, 8)
    swapThrirdAndLast(self)

def swapThrirdAndLast(self):

    #swap 3rd inv spot with last to verify theres ess there
    moveMouse(returnInt(columnNums[4], columnNums[5]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.press(buttonLeftClick)
    time.sleep(random.uniform(.2,.3))
    #last
    moveMouse(returnInt(columnNums[6], columnNums[7]), returnInt(rowNums[12], rowNums[13]))
    time.sleep(random.uniform(0.3, 1))
    mouse.release(buttonLeftClick)
    time.sleep(random.uniform(.2,.3))

#assumes all runes for all reanimations are in inv
#assumes 24 basics are in inventory (non heads in last spots)
#auto rel on
def adeptReanimation(self):
    #click each inv slot
    for i in range(4):
        for ii in range(6):
            #Click spell
            moveMouse(returnInt(1155, 1165), returnInt(568, 581))
            waitClickWait(self, .5,.8)
            #click inv slot
            moveMouse(returnInt(columnNums[i * 2], columnNums[i * 2 + 1]),
                      returnInt(rowNums[ii * 2], rowNums[ii * 2 + 1]))
            time.sleep(random.uniform(0.27, .32))
            mouse.click(self.button)
            #wait 3 seconds for kill

            time.sleep(random.uniform(16,20))

def fireLines(self):
    #click logs
    clickFirstBankSpot(self)
    #50% chance of escape
    if(returnInt(0,9)>5):
        clickEsc(self)

    #click starting square or beside it
    moveMouse(returnInt(1001, 1012), returnInt(539, 549))
    #run there and light all logs
    waitClickWait(self, 8,9)
    useLastItemOnAllOtherItems(self)
    #click bank and run there
    moveMouse(returnInt(697, 710), returnInt(283, 293))
    time.sleep(random.uniform(1,2))
    waitClickWait(self, 4,5)

    #do it again for the other line
    # click logs
    clickFirstBankSpot(self)
    # 50% chance of escape
    if (returnInt(0, 9) > 5):
        clickEsc(self)

    # click starting square or beside it
    moveMouse(returnInt(993, 1005), returnInt(556, 563))
    # run there and light all logs
    waitClickWait(self, 8, 9)
    useLastItemOnAllOtherItems(self)
    # click bank and run there
    moveMouse(returnInt(696, 711), returnInt(267, 275))
    time.sleep(random.uniform(1, 2))
    waitClickWait(self, 4, 5)
def nmz(self):
    for i in range (returnInt(15,20)):
        time.sleep(random.uniform(.1,.3))
        mouse.click(self.button)
        time.sleep(random.uniform(.58,.59))
        mouse.click(self.button)
    time.sleep(random.uniform(.5,.59))
    keyboard.press('e')
    moveMouse(returnInt(1214, 1224), returnInt(741, 757))
    waitClickWait(self, .5,.8)
    time.sleep(random.uniform(.5,.59))
    keyboard.press('r')
    time.sleep(random.uniform(.1,.3))
    moveMouse(returnInt(1109, 1122), returnInt(717, 724))
#assumes all runes for all reanimations are in inv
#assumes 24 basics are in inventory (non heads in last spots)
#auto rel on
def expertReanimation(self):
    #click each inv slot
    for i in range(4):
        for ii in range(6):
            #Click spell
            moveMouse(returnInt(1239, 1246), returnInt(653, 660))
            waitClickWait(self, .5,.8)
            #click inv slot
            moveMouse(returnInt(columnNums[i * 2], columnNums[i * 2 + 1]),
                      returnInt(rowNums[ii * 2], rowNums[ii * 2 + 1]))
            time.sleep(random.uniform(0.27, .32))
            mouse.click(self.button)
            #wait 3 seconds for kill

            time.sleep(random.uniform(20,22))
    click_thread.kill_clicking()
    listener.stop()
#assumes all runes for all reanimations are in inv
#assumes 24 basics are in inventory (non heads in last spots)
#auto rel on
def masterReanimation(self):
    #click each inv slot
    for i in range(4):
        for ii in range(6):
            #Click spell
            moveMouse(returnInt(1157, 1165), returnInt(738, 748))
            waitClickWait(self, .5,.8)
            #click inv slot
            moveMouse(returnInt(columnNums[i * 2], columnNums[i * 2 + 1]),
                      returnInt(rowNums[ii * 2], rowNums[ii * 2 + 1]))
            time.sleep(random.uniform(0.27, .32))
            mouse.click(self.button)
            #wait 3 seconds for kill

            time.sleep(random.uniform(20,22))
    click_thread.kill_clicking()
    listener.stop()
def drinkStam(self,invSlot):
    moveMouse(returnInt(624, 635), returnInt(434, 443))
    waitClickWait(self, .5,.8)
    #grab stam
    moveMouse(returnInt(672, 691), returnInt(505, 521))

    keyboard.press(Key.shift)
    waitClickWait(self, .6,.8)
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
def drinkEnergy(self,invSlot):
    moveMouse(returnInt(624, 635), returnInt(434, 443))
    waitClickWait(self, .5,.8)
    #grab stam
    moveMouse(returnInt(676, 696), returnInt(471, 488))

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

def blisterwood(self):
    if(returnInt(0, 10)<8):
        spec(self)
    moveMouse(returnInt(1145, 1244), returnInt(220, 327))
    time.sleep(random.uniform(.2, .25))
    for i in range(returnInt(6,7)):
        mouse.click(self.button)
        time.sleep(random.uniform(10,15))
    dropInventory(self)
#zoomed in all the way left or rihgt of tree camera all the way down
def redwoods(self):
    if (returnInt(0, 10) > 3):
        spec(self)
    moveMouse(returnInt(576, 673), returnInt(90, 194))
    waitClickWait(self, 200, 210)
    moveMouse(returnInt(759, 892), returnInt(80, 189))
    waitClickWait(self, 200,211)
    dropInventory(self)
    moveMouse(returnInt(374, 483), returnInt(175, 250))
    waitClickWait(self, 1,2)
def wait(min,max):
    time.sleep(random.uniform(min,max))
#facing the tree starting on right side log
def redwoodsBonfire(self):
    if(returnInt(0, 10)>3):
        spec(self)
    moveMouse(returnInt(576, 673), returnInt(90, 194))
    waitClickWait(self,220,244)
    moveMouse(returnInt(759, 892), returnInt(80, 189))
    waitClickWait(self,219,240)
    lightFire(self)
    clickBonfireEast(self)
#tinderbox in last inv slot
#log in first
def lightFire(self):
    clickLastInvSlot(self)
    clickFirstInvSlot(self)
    wait(2,3)
#have bonfire going at feet
def blisterwoodBonfire(self):
    if (returnInt(0, 10) < 8):
        spec(self)
    moveMouse(returnInt(1230, 1248), returnInt(356, 496))
    time.sleep(random.uniform(.2, .25))
    for i in range(returnInt(6, 8)):
        mouse.click(self.button)
        time.sleep(random.uniform(10, 15))
    #clickSecondOrThirdInvSlot(self)
    clickBonfireFeet(self)


#assumes north camera zoomed in
def clickBonfireEast(self):
    clickSecondOrThirdInvSlot(self)
    moveMouse(returnInt(760, 808), returnInt(399, 439))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(1,2))
    clickSpace(self)
    time.sleep(random.uniform(48,56))
#assumes north camera zoomed in
def clickBonfireFeet(self):
    #clickSecondOrThirdInvSlot(self)
    moveMouse(returnInt(588, 644), returnInt(396, 434))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(1,1.2))
    clickSpace(self)
    time.sleep(random.uniform(54,58))
def switchWorlds(self):
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.right)
    time.sleep(random.uniform(.2,.4))
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release(Key.right)
    clickSpace(self)
#assumed zoomed in north facing camera lecturn in bottom left
def makeTablets(self):
    moveMouse(returnInt(589, 663), returnInt(280, 324))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    #click house option
    time.sleep(random.uniform(2,3))
    moveMouse(returnInt(448, 540), returnInt(290, 320))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)

    #click create
    time.sleep(random.uniform(2,3))
    moveMouse(returnInt(597, 682), returnInt(448, 468))
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
def afkDags(self):
    teleToPoh(self)
    
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
    # run roof 4 walk across steep roof
    #highAlch(self)
    moveMouse(returnInt(672,684), returnInt(574,584))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(9, 10))
    # jump down
    #highAlch(self)
    moveMouse(returnInt(633,645), returnInt(427,451))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(11, 12))
    # climb starting point to reset
    #highAlch(self)
    moveMouse(returnInt(713,728), returnInt(401,404))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(6, 7))


#start ontop of spot one
def ardyCourseHA(self):
    highAlch(self)
    #run roof 1 jump to roof two
    moveMouse(returnInt(611,624), returnInt(190,233))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    #run roof 2 walk plank to roof 3
    highAlch(self)
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

    highAlch(self)
    #run roof 3 jump to roof 4
    moveMouse(returnInt(561,580), returnInt(406,438))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(6,7))
    #run roof 4 jump gap
    highAlch(self)
    moveMouse(returnInt(620,631), returnInt(500,535))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(5,6))
    #run roof 4 walk across steep roof
    highAlch(self)
    moveMouse(returnInt(672,684), returnInt(574,584))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(9,10))
    #jump down
    highAlch(self)
    moveMouse(returnInt(633,645), returnInt(427,451))
    time.sleep(random.uniform(.2, .25))
    mouse.click(self.button)
    time.sleep(random.uniform(11,12))
    #climb starting point to reset
    highAlch(self)
    moveMouse(returnInt(713,728), returnInt(401,404))
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
#assums on 4k monitor stretched mode on
def fletchDartsLastInvSlot4k(self):
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
def plantSapplingsPysical(self):
    moveMouse(returnInt(1465,1480), returnInt(928,950))
    time.sleep(random.uniform(.2,.25))
    mouse.click(self.button)
    time.sleep(random.uniform(.1,.2))
    moveMouse(returnInt(1515,1546), returnInt(924,943))
    time.sleep(random.uniform(.2,.25))
    mouse.click(self.button)
def chiselEss(self):
    clickThirdInvSlot(self)
    time.sleep(random.uniform(.1,.2))

#bolder to the left, zoomed in with left click set to empty
#have inv full of bannana baskets 3 in spots just banana
#basket left click drop bannana left click use
def maniMonkeys(self):
    if (returnInt(0,10)>8):
        mmDropInventory(self)
    #click rock
    moveMouse(returnInt(456,493), returnInt(353,406))
    time.sleep(random.uniform(.2,.4))
    mouse.click(self.button)
    time.sleep(returnInt(5,6))
    mouse.click(self.button)
    delay = np.random.randint(10,15)
    # tenPercentChanceOfE()
    time.sleep(delay)
def cannonballAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(45,60)
    # tenPercentChanceOfE()
    time.sleep(delay)
def pixelRangeTest(self):
    moveMouse(returnInt(585,594), returnInt(151,164))
    time.sleep(random.uniform(0.2,.3))
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



def cannonAutoClicker(self,min,max):
    keyboard.press(Key.shift)
    time.sleep(random.uniform(.2,.3))
    mouse.click(self.button)
    time.sleep(random.uniform(.2,.3))
    keyboard.release(Key.shift)
    delay = np.random.uniform(min,max)
    # tenPercentChanceOfE()
    time.sleep(delay)
def autoClicker(self,min,max):
    time.sleep(random.uniform(.2,.3))
    mouse.click(self.button)
    delay = np.random.randint(min,max)
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
    clickFirstInvSlot(self)
    clickFirstBankSpot(self)
    clickEsc(self)
    leftClickDropInventory(self)
    time.sleep(random.uniform(3,4))
    clickCraftingGuildBank(self)
#set x to 6
def makeCombats(self):
    depositAll(self)
    clickFirstBankSpot(self)
    clickSecondBankSpot(self)
    clickThirdBankSpot(self)
    clickForthBankSpot(self)
    clickEsc(self)
    clickFirstInvSlot(self)
    clickInventorySlot(self,7)
    sleep(returnInt(6,8))
    clickCraftingGuildBank(self)
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
def makePotsWithUnfs(self):
    #empty inv
    clickSecondOrThirdInvSlot(self)
    clickThirdBankSpot(self)
    clickForthBankSpot(self)
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
    time.sleep(random.uniform(0.1,0.15))  # random.uniform(0.3, .5)
    mouse.click(self.button)
    # click inv spot 5
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[2], rowNums[3]))
    time.sleep(random.uniform(0.1,0.15))  # random.uniform(0.3, .5)
    mouse.click(self.button)  # start herb animation
def bolts(self):
    # click inv spot one
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.6,.8))  # random.uniform(0.3, .5)
    mouse.click(self.button)
    # click inv spot 5
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[2], rowNums[3]))
    time.sleep(random.uniform(0.6,.8))  # random.uniform(0.3, .5)
    mouse.click(self.button)  # start herb animation
    time.sleep(random.uniform(0.6,.8))  # random.uniform(0.3, .5)
    clickSpace(self)
    time.sleep(returnInt(20,30))
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
def craftOrFletchWKnife(self):
    clickWestBankZoomedIn(self)
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


def fourteenFourteenCraft(self):
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
def pyspec(self):
    moveMouse(returnInt(1394,1408),returnInt(213,228))
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
def  varrockSmithing(self):
    clickSecondInvSlot(self)
    clickFirstBankSpot(self)
    #click anvil
    moveMouse(returnInt(679,685), returnInt(672,681))
    waitClickWait(self,8,10)
    #click space
    clickSpace(self)
    #1 bar items
    #time.sleep(random.uniform(54,68))
    #2 bar items
    time.sleep(random.uniform(28,32))
    #plate bodys
    #time.sleep(random.uniform(13,14))
    #time.sleep(random.uniform(23,27))
    #click bank
    moveMouse(returnInt(585,594), returnInt(151,164))
    waitClickWait(self,9,10)
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

#fishing explosibes in spot 1 standing on start square with camera nort
def caveKracken(self):
    #click fishing explosive
    clickFirstInvSlot(self)
    #click pool
    moveMouse(returnInt(585,678),returnInt(200,284))
    time.sleep(random.uniform(0.42,.6))
    mouse.click(self.button)
    time.sleep(random.uniform(4,5))
    #click pool
    moveMouse(returnInt(585,678),returnInt(200,284))
    time.sleep(random.uniform(0.42,.6))
    mouse.click(self.button)
    #trident
    time.sleep(random.uniform(65,70))
    #scepter
    #time.sleep(random.uniform(70,75))
    #scepter no praY
    #time.sleep(random.uniform(81,84))
    #click drop
    moveMouse(returnInt(624,628),returnInt(414,417))
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
def pressE(self):
    keyboard.press('e')
    time.sleep(random.uniform(.3, .5))
    keyboard.release('e')
def pressF(self):
    keyboard.press('f')
    time.sleep(random.uniform(0.42,.6))
    keyboard.release('f')
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
    moveMouse(returnInt(1227, 1232), returnInt(612, 618))
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
def clickWestBankZoomedIn(self):
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

def runCannonBalls(self):
    #deposit all cannonballs
    clickSecondInvSlot(self)
    #grab more bars
    clickFirstBankSpot(self)

    #click furnace
    moveMouse(returnInt(878, 891), returnInt(324, 335))
    waitClickWait(self,6,8)
    #click space
    clickSpace(self)
    time.sleep(random.uniform(70,80))
    #click bank
    moveMouse(returnInt(389, 403), returnInt(523, 532))
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
#zzomed in camera north
def iron(self):
    for ii in range(8):
        moveMouse(returnInt(572, 672), returnInt(216, 297))
        waitClickWait(self, 1.75,2)
        moveMouse(returnInt(584, 672), returnInt(528, 621))
        waitClickWait(self, 1.7,2)
        moveMouse(returnInt(418, 516), returnInt(374, 464))
        waitClickWait(self, 1.75,2)
    dropInventory(self)

    if(returnInt(0, 10)>7):
        spec(self)


columnNums = [1079,1099,1119,1143,1165,1187,1210,1226] #X
rowNums = [523,542,563,582,601,614,635,651,672,689,710,724,740,758] #Y
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
    for i in range(np.random.randint(10,15)):
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

#coal bag in first inv slot and empty, fill hopper with a inv or 2 of coal
def BlastFurnaceForSteelBars(self):
    for x in range (8):
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

                clickSecondOrThirdInvSlot(self)
                drinkEnergy(self,"2")

#assumes starting with full run and coffer filled and goldsmith gaunts on with ice in inv1
def  goldBlastFurnace(self):
    for x in range (8):
        #click last inv spot
        clickLastInvSlot(self)

        clickFirstBankSpot(self)
        time.sleep(random.uniform(0.8, 1))
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
#assumes ore in spot 1 in bank coal in spot 2. Bag is in inv spot 1 and quantity set to all
def BlastFurnaceForRuneBars(self):
    for x in range (5):
        for y in range (3):
            #deposit bars
            clickSecondInvSlot(self)
            #grab addy
            if(y==0 or y==1 ):
                #grab coal
                clickSecondBankSpot(self)
            if(y==2):
                #grab rune
                clickFirstBankSpot(self)
            #grab coal
            if y!=2:
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
            if y!=2:
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
def clickForthBankSpot(self):
    moveMouse(returnInt(482,499), returnInt(112,124))
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
    if(returnInt(0, 10)<7):
        spec(self)
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

    if(returnInt(0, 10)<5):
        #click first ore spot
        moveMouse(returnInt(601,610), returnInt(415,423))
        waitClickWait(self,36,39)
    

    if(returnInt(0, 10)<5):
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
    for i in range (8):
        mythCape(self)
    time.sleep(random.uniform(.3, .6))
    #open settings
    #keyboard.press('0')
    #time.sleep(random.uniform(.3, .6))
    #keyboard.release('0')
    #call butler
    time.sleep(random.uniform(.3, .6))
    moveMouse(returnInt(1172, 1191), (returnInt(700, 720)))
    time.sleep(random.uniform(.3, .6))
    waitClickWait(self, .6,.8)
    waitClickWait(self,.6,.8)
    #make a myth cape to axe supplies
    mythCape(self)
    #call butler
    time.sleep(random.uniform(.3, .6))
    moveMouse(returnInt(1172, 1191), (returnInt(700, 720)))
    time.sleep(random.uniform(.3, .6))
    waitClickWait(self, .6,.8)
    waitClickWait(self,1.2,1.4)
    #order supplies
    keyboard.press('1')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('1')
    #wait for butler
    time.sleep(random.uniform(8,10))

#assumes zoomed in and walking from north to position camera
#butler called and on the square behind144
def mahogTables(self):
    for i in range (4):
        mahogTable(self)
    time.sleep(random.uniform(.3, .6))
    #open settings
    #keyboard.press('0')
    #time.sleep(random.uniform(.3, .6))
    #keyboard.release('0')
    #call butler
    time.sleep(random.uniform(.3, .6))
    moveMouse(returnInt(1172, 1191), (returnInt(700, 720)))
    time.sleep(random.uniform(.3, .6))
    waitClickWait(self, .6,.8)
    waitClickWait(self,.6,.8)
    #make a myth cape to axe supplies
    mahogTable(self)
    #call butler
    time.sleep(random.uniform(.3, .6))
    moveMouse(returnInt(1172, 1191), (returnInt(700, 720)))
    time.sleep(random.uniform(.3, .6))
    waitClickWait(self, .6,.8)
    waitClickWait(self,1.2,1.4)
    #order supplies
    keyboard.press('1')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('1')
    #wait for butler
    time.sleep(random.uniform(8,10))

def mythCape(self):
    moveMouse(returnInt(593, 664), (returnInt(477, 490)))
    waitClickWait(self, .6, 1.2)
    #add
    keyboard.press('4')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('4')
    #remove
    time.sleep(random.uniform(.6,.8))
    waitClickWait(self, .8,1)
    keyboard.press('1')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('1')
def mahogTable(self):
    moveMouse(returnInt(496, 584), (returnInt(544, 622)))
    waitClickWait(self, .6, 1.2)
    #add
    keyboard.press('6')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('6')
    #remove
    time.sleep(random.uniform(.6,.8))
    waitClickWait(self, .8,1)
    keyboard.press('1')
    time.sleep(random.uniform(.3, .6))
    keyboard.release('1')

#assumes north faceing zoomed out camera
#money in slot 1
#set quantity to all, wear full gracefull dumbass
def runPlanks(self):
    for i in range(2):
        # click first bank spot
        clickFirstBankSpot(self)
        # click square
        # wait while running
        moveMouse(returnInt(863,867), returnInt(82,90))
        waitClickWait(self, 12, 13)
        # click sawmill dude
        moveMouse(returnInt(896, 903), returnInt(399, 407))
        waitClickWait(self, 8, 9)
        # click space
        clickSpace(self)
        # click square
        # wait while running
        moveMouse(returnInt(64, 70), returnInt(524, 535))
        waitClickWait(self, 10, 12)
        # click bank
        moveMouse(returnInt(493, 495), returnInt(779, 784))
        waitClickWait(self, 8, 10)

        # click second inv spot
        clickSecondOrThirdInvSlot(self)
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

#camera facing norht zoomed into range at top of screen
def hosidiousCookingBot(self):
    #empty inventory
    emptyInventoryInBank(self)
    #click karams
    clickFirstBankSpot(self)
    #press esc
    keyboard.press(Key.esc)
    time.sleep(random.uniform(.3,.6))
    keyboard.release(Key.esc)
    #click range and run there

    moveMouse(returnInt(713,732), returnInt(124,144))
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
    moveMouse(returnInt(526,549), returnInt(688,708))
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

def clickInventorySlot(self, slot):
    if slot < 1 or slot > 28:
        raise ValueError("Inventory slot must be between 1 and 28")

    row = (slot - 1) // 4
    col = (slot - 1) % 4

    x = returnInt(columnNums[col * 2], columnNums[col * 2 + 1])
    y = returnInt(rowNums[row * 2], rowNums[row * 2 + 1])

    moveMouse(x, y)
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(0.8, 1))
def clickFirstInvSlot(self):
    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
    time.sleep(random.uniform(0.3, 1))
    mouse.click(self.button)
    time.sleep(random.uniform(.8,1))
#def clickInvSlot(self):
#    moveMouse(returnInt(columnNums[0], columnNums[1]), returnInt(rowNums[0], rowNums[1]))
#    time.sleep(random.uniform(0.3, 1))
 #   mouse.click(self.button)
 #   time.sleep(random.uniform(.8,1))
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
def clickForthInvSlot(self):
    moveMouse(returnInt(columnNums[6], columnNums[7]), returnInt(rowNums[0], rowNums[1]))
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
def useLastItemOnAllOtherItems(self):
    for i in range(4):
        for ii in range(6):
            #rowLow=i*2
            #rowHigh=i*2+1
            #colLow=ii*2
            #colHigh=ii*2+1
            clickLastSlot(self)
            time.sleep(random.uniform(0.2, .3))
            moveMouse(returnInt(columnNums[i*2], columnNums[i*2+1]), returnInt(rowNums[ii*2], rowNums[ii*2+1]))
            time.sleep(random.uniform(0.2, .3))
            mouse.click(self.button)
            time.sleep(random.uniform(.8,1))
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
