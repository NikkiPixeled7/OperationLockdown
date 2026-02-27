############## Import ##############
import random, time, sys, tkinter, os, shutil, platform
from ASCIIArt import gameLogo


############## Global Variables ##############

choice = 0
winCounter = 0
loseCounter = 0
invalidChoice = 0

############## (Reusable) Definitions ##############

## Typewriter
def typeWriter(text):
    sleep_time = 0.02

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleep_time)

#  How to use --->   print_centre("enter text here")
def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def endMsg():
    msgNum = random.randint(1,4)
    if msgNum == 1:
        print("\nMission failed… better luck next time!")
    elif msgNum == 2:
        print("\nYou didn’t make it this time.")
    elif msgNum == 4:
        print("\nOperation unsuccessful. Try again.")
    else:
        print("\nThe mission ends here. Don’t give up!")



def clearText():
    print(platform.system())
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input("\033[1mPress \033[32mEnter\033[0;1;39m To Continue\033[0m\n")


# How to Use Animated Text Func
"""
Animated Text Func (use this, textInput = input("Example Text: \n"))
                            speed = ...
                            length = ...
                            load_animation(textInput, speed, length)
"""


def load_animation(load_str, speed, length):
    str_len = len(load_str)

    animation = "|/-\\"
    anicount = 0

    count_time = 0

    i = 0

    while count_time != length:
        time.sleep(speed)

        load_str_list = list(load_str)

        x = ord(load_str_list[i])


        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
    res = ''
    for j in range(str_len):
        res = + load_str_list[j]

    sys.stdout.write("\r" + res + animation[anicount])
    sys.stdout.flush()

    load_str = res

    anicount = (anicount + 1) % 4
    i = (i + 1) % str_len
    count_time = + 1


if os.name == "nt":
    pass
else:
    os.system("clear")


# Choose Option Function

def chooseOption(numOfOpt):
    global choice
    choice = 0
    while choice < 1 or choice > numOfOpt:
        print("\nChoose A Number 1 to " + str(numOfOpt) + "\n>>> ", end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = 0
        else:
            choice = int(choice)

        if choice == 0:
            clearText()
            global invalidChoice
            print("Invalid Choice, Please Try Again.. " + str(invalidChoice))
            invalidChoice += 1

        print("\n\n")
    return choice



############## (Single Use/ + Retry Use) Definitions ##############

### Level A (Front Lobby) ###
def rushLobby():
    clearText()
    trl1 = "You charge into the lobby head-on, risking a firefight."
    typeWriter(trl1)
    time.sleep(.67)
    print("\n")
    print("Where Will You Go?")
    print("   1. Push Stairs")
    print("   2. Clear Side Rooms")
    print("   3. Hold Lobby")
    chooseOption(3)
    clearText()
    if choice == 1:
        pushStairs()
    elif choice == 2:
        clearSideRooms()
    else:
        holdLobby()

def flashbangEntry():
    clearText()
    tfe1 = "You throw a flashbang to stun enemies before moving."
    typeWriter(tfe1)
    time.sleep(.67)
    print("\n")
    print("Where Will You Go?")
    print("   1. Advance After Flash")
    print("   2. Reload & Wait")
    print("   3. Retreat & Regroup")
    chooseOption(3)
    clearText()
    if choice == 1:
        advanceAfterFlash()
    elif choice == 2:
        reloadAndWait()
    else:
        retreatAndRegroup()

def droneRecon():
    clearText()
    tdr1 = "You use a drone to scout the lobby for hostiles or hostages."
    typeWriter(tdr1)
    time.sleep(.67)
    print("\n")
    print("Where Will You Go?")
    print("   1. Follow Intel")
    print("   2. Ignore Intel")
    print("   3. Reposition")
    chooseOption(3)
    clearText()
    if choice == 1:
        followIntel()
    elif choice == 2:
        ignoreIntel()
    else:
        reposition()

def fallBack():
    clearText()
    tfb1 = "You retreat to plan your next move, but taking too long allows the enemies to reinforce their positions. By the time you return, the lobby is heavily guarded, and your chance for a quick entry is lost."
    typeWriter(tfb1)
    time.sleep(.67)
    print("\n")
    global loseCounter
    loseCounter += 1

##### Level A1 ##

def pushStairs():
    clearText()
    tps1 = "Move up the stairs to reach upper floors."
    typeWriter(tps1)
    time.sleep(.67)
    print("\n")
    print("What Next? (What Will You Pick \U0001F914)")
    print("   1. Breach Objective")
    chooseOption(1)
    clearText()
    if choice == 1:
        breachObjective()

def breachObjective():
    clearText()
    tps1 = "You breach the objective room successfully, but the tension is high. If your timing is perfect, you defuse the bomb and complete the mission.\n\
    If not, a misstep triggers the explosives, ending the operation in failure. (33% Chance)"
    typeWriter(tps1)
    time.sleep(.67)
    breachGuess = random.randint(1,3)
    if breachGuess == 2:
        print("\nGood Job You Win!!!")
        global winCounter
        winCounter += 1
    elif breachGuess == 3 or breachGuess == 1:
        endMsg()
        global loseCounter
        loseCounter += 1

def clearSideRooms():
    clearText()
    tcsr1 = "You spend too long searching the side rooms. While you were distracted, enemy reinforcements secure the main objective, leaving you no choice but to retreat. The mission is compromised."
    typeWriter(tcsr1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def holdLobby():
    clearText()
    thl1 = "You try to hold the lobby, but the enemies quickly flank your position. Overwhelmed, you’re forced to pull back, and the mission fails before you can reach the objective."
    typeWriter(thl1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

##### Level A2 ##

def advanceAfterFlash():
    clearText()
    taaf1 = "You push forward too quickly, but the enemies recover faster than expected. You’re forced to retreat."
    typeWriter(taaf1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def reloadAndWait():
    clearText()
    traw1 = "Waiting gives the enemies time to regroup. Your advance is blocked, and the mission fails."
    typeWriter(traw1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def retreatAndRegroup():
    clearText()
    traw1 = "Pulling back takes too long, and the opportunity slips away. You’re forced to abort the mission."
    typeWriter(traw1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

##### Level A3 ##

def followIntel():
    clearText()
    tfi1 = "You follow the intel carefully, avoid enemy patrols, and reach the objective safely. The mission is a success!"
    typeWriter(tfi1)
    time.sleep(.67)
    print("\n")
    print("Nice Job, You Won!")
    global winCounter
    winCounter += 1

def ignoreIntel():
    clearText()
    tit1 = "Without guidance, you stumble into enemy territory and must retreat. The operation ends here."
    typeWriter(tit1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def reposition():
    clearText()
    tr1 = "Repositioning wastes too much time, letting the enemies gain the advantage. You’re forced to abort the mission."
    typeWriter(tr1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

### End of Level A, Start of Level B ###

def skylightEntry():
    clearText()
    tse1 = "You drop into the building through a skylight."
    typeWriter(tse1)
    time.sleep(.67)
    print("\n")
    print("What Will You Do?")
    print("   1. Wait Backup")
    print("   2. Scan Room")
    print("   3. Drop In")
    chooseOption(3)
    clearText()
    if choice == 1:
        waitBackup()
    elif choice == 2:
        scanRoom()
    else:
        dropIn()

## B1 Level #

def dropIn():
    clearText()
    tse1 = "You drop into the building through a skylight."
    typeWriter(tse1)
    time.sleep(.67)
    print("\n")
    print("What Will You Do?")
    print("   1. Enter Objective")
    print("   2. Enter Through Breach")
    chooseOption(1)
    clearText()
    if choice == 1:
        enterObjective()
    else:
        enterThroughBreach()

def scanRoom():
    clearText()
    tsr1 = "You spend too long scanning the room, and enemies notice your presence. The rooftop entry is compromised, forcing you to retreat."
    typeWriter(tsr1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def waitBackup():
    clearText()
    twb1 = "Backup takes longer than expected. By the time they arrive, the enemies have reinforced the area and the mission is cancelled."
    typeWriter(twb1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def enterObjective():
    clearText()
    tfi1 = "You enter the objective room, knowing one wrong move could end the mission.\n\
Everything comes down to timing, awareness, and a bit of luck."
    typeWriter(tfi1)
    time.sleep(.67)
    print("\n")
    print("Nice Job, You Won!")
    global winCounter
    winCounter += 1

def enterThroughBreach():
    clearText()
    tsr1 = "You breach the opening at the perfect moment and catch the enemies off guard.\n\
With the room secured and the objective under control, the mission is a success."
    typeWriter(tsr1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global winCounter
    winCounter += 1

##### Level B2 ##

def stairwellApproach():
    clearText()
    tsa1 = "You take the stairs quietly to avoid detection."
    typeWriter(tsa1)
    time.sleep(.67)
    print("\n")
    print("What Will You Do?")
    print("   1. Fall Back")
    print("   2. Silent Takedown")
    print("   3. Avoid Patrol")
    chooseOption(3)
    clearText()
    if choice == 1:
        fallBack2()
    elif choice == 2:
        silentTakedown()
    else:
        avoidPatrol()


def fallBack2():
    clearText()
    tfb21 = "You retreat to reassess the situation, but the window to strike closes.\n\
The enemies secure the building, and the operation is called off."
    typeWriter(tfb21)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def avoidPatrol():
    clearText()
    tap1 = "You attempt to sneak around the patrol, but the delay costs you the element of surprise.\n\
Enemies lock down the area, forcing the mission to end."
    typeWriter(tap1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def silentTakedown():
    clearText()
    tst1 = "You take the stairs quietly to avoid detection."
    typeWriter(tst1)
    time.sleep(.67)
    print("\n")
    print("What Next?")
    print("   1. 1 Try, 35% Chance Win")
    print("   2. 4 Tries, 8% Chance per try")
    chooseOption(2)
    clearText()
    if choice == 1:
        oneTry()
    else:
        fourTries()

def oneTry():
    win = random.randint(1, 100)
    if win <= 35:
        print("You win the 35/65, nice job!")
        print(win)
        global winCounter
        winCounter += 1
    else:
        print("You \033[1;31mlost\033[0m the 35/65 \U0001F61E")
        global loseCounter
        loseCounter += 1

def fourTries():
    j = 0
    l = 0
    while j < 4:
        win2 = random.randint(1, 100)
        if win2 >= 1 and win2 <= 8:
            print("You \033[1;32mwin\033[0m the 8% chance \U0001F92F")
            global winCounter
            winCounter += 1
            l = 67 #hehe 67
            break
        else:
            j += 1

        if j >= 4:
            print("You lost \U0001F61E")
            global loseCounter
            loseCounter += 1




##### Level B3 ##

def roofHop():
    clearText()
    trh1 = "You move across the rooftops, but enemy lookouts spot your movement. The element of surprise is lost, and the mission is aborted."
    typeWriter(trh1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

##### Level B4 ##

def abortMission():
    clearText()
    tam1 = "You decide the rooftop approach is too risky and pull back. While retreating, the enemies secure the building, and the operation is called off."
    typeWriter(tam1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

### End of Level B, Start of Level C ###


## C1 #

def shadowMove():
    clearText()
    tsm1 = ("You move silently between vehicles, but an enemy patrol catches movement in the dark.\n\
You think you lost but there is the smallest chance of turnaround... (pick a number from 1 through 67)")
    typeWriter(tsm1)
    time.sleep(.67)
    print("\n")
    rep = 1 # repeat -> rep
    while rep < 2:
        shadowMoveGuess = int(input("\n(1-67)  >>> "))
        if 1 <= shadowMoveGuess <= 67:
            shadowMoveNum = random.randint(1, 67)
            if shadowMoveGuess == shadowMoveNum:
                print("Wow. You.. Actually... Won... Good Job!")
                global winCounter
                winCounter += 1
                rep += 5
            else:
                print("You lost \U0001F61E")
                global loseCounter
                loseCounter += 1
                rep += 5
        else:
            print("I said from 1-67, no more, no less..")


## C2 #

def useFlashlight():
    clearText()
    tsa1 = "You light the area to see better, but your position is immediately revealed."
    typeWriter(tsa1)
    time.sleep(.67)
    endMsg()
    global loseCounter
    loseCounter += 1

## C3 #

def searchVehicles():
    clearText()
    tsa1 = "You search nearby vehicles and find useful supplies or intel."
    typeWriter(tsa1)
    time.sleep(.67)
    print("\n")
    print("What Next?")
    print("   1. Use Supplies")
    print("   2. Move Deeper")
    print("   3. Wait And Plan")
    chooseOption(3)
    clearText()
    if choice == 1:
        useSupplies()
    elif choice == 2:
        moveDeeper()
    else:
        waitAndPlan()

def useSupplies():
    clearText()
    tus1 = "You equip the gear you found and move forward with confidence. Using the supplies to your advantage,\n\
you avoid enemy patrols and successfully secure the objective. Mission accomplished."
    typeWriter(tus1)
    time.sleep(.67)
    print("\n")
    global winCounter
    winCounter += 1

def moveDeeper():
    clearText()
    tmd1 = "You push deeper into the garage, but the noise echoes through the structure.\n\
Enemy patrols close in, forcing you to abort the mission."
    typeWriter(tmd1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

def waitAndPlan():
    clearText()
    twap1 = "Waiting too long gives the enemies time to reposition and secure the area.\n\
Your chance to move forward is gone, and the mission ends."
    typeWriter(twap1)
    time.sleep(.67)
    print("\n")
    endMsg()
    global loseCounter
    loseCounter += 1

## C4 #

def retreat():
    clearText()
    tsa1 = "You fall back to rethink your approach and spot a safer entry route."
    typeWriter(tsa1)
    time.sleep(.67)
    print("\n")
    print("What Next?")
    print("   1. Side Entrance")
    print("   2. Hold Position")
    print("   3. Reroute")
    chooseOption(3)
    clearText()
    if choice == 1:
        sideEntrance()
    elif choice == 2:
        holdPosition()
    else:
        reroute()

### End of Level C ###

def gameIntro():
    clearText()
    welcomeText = "\033[1;35mWelcome\033[0m To Operation Lockdown"
    width = 30
    centeredText = welcomeText.center(width)
    print(centeredText)
    gameLogo()
    name = str(input("What Can I Call You?\n\
    >>> "))
    print("\n")
    time.sleep(.25)
    print("I Hope You Are Ready\033[1;31m Mr. " + (name) + "\033[0m.\n")

    pause()
    clearText()

    text = """\033[1;35mOperation Lockdown\033[0m is a text-based choose-your-own-adventure game inspired by the tactical gameplay of Rainbow Six Siege,\n\
you will be taking on the role of an elite operator during a \033[1;35mhigh-risk \033[0mhostage rescue mission. \n \
You will make choices on what happens next, be careful though since some  paths may lead to an \033[1;35mabrupt ending.\033[0m\n\
There are many different endings, some \033[32mgood\033[0m and some \033[31mbad\033[0;1m. Have fun.\033[0m\n"""
    sleep_time = 0.015

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleep_time)

    print("Win Counter: " + str(winCounter))
    print("Lose Counter: " + str(loseCounter))
    print("\n\n")

def frontLobby():
    clearText()
    tfl1 = "You enter the lobby where enemies are waiting and alarms may trigger."
    typeWriter(tfl1) #text front lobby 1
    time.sleep(.67)
    print("\n")
    print("Where Will You Go?")
    print("   1. Rush Lobby")
    print("   2. Flashbang Entry")
    print("   3. Drone Recon")
    print("   4. Fall Back")
    chooseOption(4)
    clearText()
    if choice == 1:
        rushLobby()
    elif choice == 2:
        flashbangEntry()
    elif choice == 3:
        droneRecon()
    else:
        fallBack()

def rooftopRappel():
    trr1 = "You rappel onto the roof to make a stealthy entry."
    typeWriter(trr1)
    time.sleep(.67)
    print("\n")
    print("Where Will You Go?")
    print("   1. Skylight Entry")
    print("   2. Stairwell Approach")
    print("   3. Roof Hop")
    print("   4. Abort Mission")
    chooseOption(4)
    clearText()
    if choice == 1:
        skylightEntry()
    elif choice == 2:
        stairwellApproach()
    elif choice == 3:
        roofHop()
    else:
        abortMission()

def parkingGarage():
    tpg1 = "You move through the dark garage where sound and shadows hide danger."
    typeWriter(tpg1)
    time.sleep(.67)
    print("\n")
    print("Where Will You Go?")
    print("   1. Shadow Move")
    print("   2. Use Flashlight")
    print("   3. Search Vehicles")
    print("   4. Retreat")
    chooseOption(4)
    clearText()
    if choice == 1:
        shadowMove()
    elif choice == 2:
        useFlashlight()
    elif choice == 3:
        searchVehicles()
    else:
        retreat()

def level_1_entry(): #######################temp commented out
    tl1e1 = "You arrive outside the building where \033[1mhostages\033[0m are being held. "
    tl1e2 = "Police sirens echo behind you as your team waits for your command.\n"
    tl1e3 = "This is the moment where \033[1;32myou\033[32m decide how to enter the building\033[0m, knowing that your choice will affect how \033[1;31mdangerous\033[0m the mission becomes.\033[0m"
    typeWriter(tl1e1) #tl1e means "text level 1 entry" text 1
    time.sleep(.67)
    typeWriter(tl1e2) #tl1e text 2
    time.sleep(.90)
    typeWriter(tl1e3) #tl1e text 3

    ##
    time.sleep(1)
    print("\n")
    print("Where Will You Go?")
    print("   1. Front Lobby")
    print("   2. Rooftop Rappel")
    print("   3. Parking Garage")
    chooseOption(3)
    if choice == 1:
        frontLobby()
    elif choice == 2:
        rooftopRappel()
    else:
        parkingGarage()


def startGame():
    pause()
    time.sleep(.75)
    clearText()
    level_1_entry()

############## Main Loop ##############
while True:
    # start game function
    gameIntro()

    startGame()


    ######### play again function
    ynInput = input("\nWould you like to play again? " + "\U00002705 " + " Y" + \
                    " / " + "\U0000274C " + " N\n")
    if ynInput == 'y' or ynInput == 'Y':
        gameIntro()
        clearText()
    elif ynInput == 'n' or ynInput == 'N':
        clearText()
        i = 0
        while i < 4:
            print("Quitting")
            time.sleep(0.25)
            clearText()
            time.sleep(0.25)
            i += 1
            if i == 3:
                print("This is intentional")
                time.sleep(1)
            else:
                pass

        break
    elif ynInput != 'y' and ynInput != 'Y' and ynInput != 'N' and ynInput != 'n':
        print("Type Y or N to reply: ")
    else:
        print("Why is this here?")

# quit the game if no play again or start

print("Quitting...")

sys.exit(0)
