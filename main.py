############## Import ##############

import random, time, sys, os, shutil, platform
from ASCIIArt import gameLogo, mazeGame, shopAndQuit, sadFace, sadFace2, simpleSadFace, crown


############## Global Variables ##############

choice = 0
winCounter = 0
loseCounter = 0
invalidChoice = 0
introSkipCounter = 0
textSkipCounter = 0
doubleLuckCounter = 0
extraLifeCounter = 0

############## (Reusable) Definitions ##############

def playAgain():
    while True:
        ynInput = str(input("\nWould you like to play again? " + "\U00002705 " + " Y" + \
                            " / " + "\U0000274C " + " N\n"))
        if ynInput == 'y' or ynInput == 'Y':
            clearText()
            return
        elif ynInput == 'n' or ynInput == 'N':
            clearText()
            for _ in range(3):
                print("Quitting")
                time.sleep(0.25)
                clearText()
                time.sleep(0.25)

            print("This is intentional")
            time.sleep(1)
            print("Quitting...")
            sys.exit(0)
        elif ynInput != 'y' and ynInput != 'Y' and ynInput != 'N' and ynInput != 'n':
            print("Type Y or N to reply: ")
        else:
            print("Why is this here?")

## Typewriter
def typeWriter(text):
    sleep_time = 0.015

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
        time.sleep(1.5)
        sadFace()
    elif msgNum == 2:
        print("\nYou didn’t make it this time.")
        time.sleep(1.5)
        sadFace2()
    elif msgNum == 3:
        print("\nOperation unsuccessful. Try again.")
        time.sleep(1.5)
        simpleSadFace()
    else:
        print("\nThe mission ends here. Don’t give up!")
        time.sleep(1.5)
        simpleSadFace()

def skipIntro():
    skip = str(input("\nWould you like to skip intro? (y/n): "))
    if skip == 'y' or skip == 'Y':
        time.sleep(.2)
        global textSkipCounter
        textSkipCounter += 5
        clearText()
        startGame()
    elif skip == 'n' or skip == 'N':
        time.sleep(.2)
        gameIntro()

def clearText():
    print(platform.system())
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input("\033[1mPress \033[32mEnter\033[0;1;39m To Continue\033[0m\n")

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
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7' and choice != '8' and choice != '9': #just incase i need more options for the shop
            choice = 0
        else:
            choice = int(choice)

        if choice == 0:
            global invalidChoice
            print("Invalid Choice, Please Try Again.. " + str(invalidChoice))
            invalidChoice += 1

        print("\n\n")
    return choice



############## (Single Use/ + Retry Use) Definitions ##############

##### Level A1 ##

def breachObjective():
    clearText()
    global doubleLuckCounter, extraLifeCounter, winCounter, loseCounter
    tps1 = "You breach the objective room successfully, but the tension is high. If your timing is perfect, you defuse the bomb and complete the mission.\n\
    If not, a misstep triggers the explosives, ending the operation in failure. (33% Chance)"
    typeWriter(tps1)
    time.sleep(.67)
    breachGuess = random.randint(1,3)
    if doubleLuckCounter >= 1:
        print("Double Luck used! Odds are doubled for this round!")
        time.sleep(2)
        if breachGuess == 1 or breachGuess == 2:
            print("\nGood Job You Win!!!")
            winCounter += 1
            crown()
            doubleLuckCounter -= 1
        elif breachGuess == 3:
            if extraLifeCounter >= 1:
                endMsg()
                print("You lost, but an extra life saved you!")
                print("+0 Losses")
                doubleLuckCounter -= 1
                extraLifeCounter -= 1
            else:
                endMsg()
                loseCounter += 1
                doubleLuckCounter -= 1

    else:
        if breachGuess == 2:
            print("\nGood Job You Win!!!")
            winCounter += 1
            crown()
        elif breachGuess == 3 or breachGuess == 1:
            if extraLifeCounter >= 1:
                endMsg()
                print("You lost, but an extra life saved you!")
                print("+0 Losses")
                extraLifeCounter -= 1
            else:
                endMsg()
                loseCounter += 1

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

def clearSideRooms():
    clearText()
    tcsr1 = "You spend too long searching the side rooms. While you were distracted, enemy reinforcements secure the main objective, leaving you no choice but to retreat. The mission is compromised."
    typeWriter(tcsr1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

def holdLobby():
    clearText()
    thl1 = "You try to hold the lobby, but the enemies quickly flank your position. Overwhelmed, you’re forced to pull back, and the mission fails before you can reach the objective."
    typeWriter(thl1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
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
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

def reloadAndWait():
    clearText()
    traw1 = "Waiting gives the enemies time to regroup. Your advance is blocked, and the mission fails."
    typeWriter(traw1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

def retreatAndRegroup():
    clearText()
    trar1 = ("You fall back to regroup and rethink your approach. The area is confusing and tight, forcing you to navigate carefully.\n\
You are the ¥ symbol and can move one square at a time using W, A, S, D. Find your way to the X to successfully regroup and continue.\n\
You get 3 Tries")
    typeWriter(trar1)
    time.sleep(.67)
    print("\n")
    mazeGame()
    valid_routes = ["SSSSDDDWWDDDSSDDDDWWWWDW", "ssssdddwwdddssddddwwwwdw", "SSSSSSSDDWDDDDDDDDDDWWWWWWAW", "sssssssddwddddddddddwwwwwwaw", "SSSSSSSDDWDDDDDDDDDDSDDDDDWWWWWWWAAAAAAW", "sssssssddwddddddddddsdddddwwwwwwwaaaaaaw"]
    mazeWin = "SSSSDDDWWDDDSSDDDDWWWWDW"
    mazeWin1 = "ssssdddwwdddssddddwwwwdw"
    mazeWin2 = "SSSSSSSDDWDDDDDDDDDDWWWWWWAW"
    mazeWin21 = "sssssssddwddddddddddwwwwwwaw"
    mazeWin3 = "SSSSSSSDDWDDDDDDDDDDSDDDDDWWWWWWWAAAAAAW"
    mazeWin31 = "sssssssddwddddddddddsdddddwwwwwwwaaaaaaw"
    t = 1
    while t < 4:
        mazeInput = str(input("Be Careful With Your Inputs\n>>> "))
        if mazeInput in valid_routes:
            print("You successfully regroup and escape the area with a solid plan. The mission is completed successfully.\n")
            global winCounter
            winCounter += 1
            crown()
            break
        else:
            t += 1
            if t >= 4:
                pass
            else:
                print("That route didn’t work. Regroup and try again while you still have time.\n")

        if t >= 4:
            print("You fail to regroup in time. Confusion spreads, the enemies gain control, and the mission ends.\n")
            global extraLifeCounter
            if extraLifeCounter >= 1:
                print("You lost, but an extra life saved you!")
                print("+0 Losses")
                time.sleep(1.33)
                endMsg()
                extraLifeCounter -= 1
            else:
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
    crown()

def ignoreIntel():
    clearText()
    tit1 = "Without guidance, you stumble into enemy territory and must retreat. The operation ends here."
    typeWriter(tit1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

def reposition():
    clearText()
    tr1 = "Repositioning wastes too much time, letting the enemies gain the advantage. You’re forced to abort the mission."
    typeWriter(tr1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

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
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        extraLifeCounter -= 1
    else:
        global loseCounter
        loseCounter += 1

### End of Level A, Start of Level B ###

## B1 Level #

def scanRoom():
    clearText()
    tsr1 = "You spend too long scanning the room, and enemies notice your presence. The rooftop entry is compromised, forcing you to retreat."
    typeWriter(tsr1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

def waitBackup():
    clearText()
    twb1 = "Backup takes longer than expected. By the time they arrive, the enemies have reinforced the area and the mission is cancelled."
    typeWriter(twb1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
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
    print("Nice Job, You Won! *Number 2 is the fun path, go for it next*")
    global winCounter
    winCounter += 1
    crown()

## Door Replies (next def) ##

def door1():
    clearText()
    print("You push it open… and find a dimly lit room filled with mirrors reflecting your every move. ❌ Wrong choice — nothing here leads onward.")
    time.sleep(.33)
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        extraLifeCounter -= 1
    else:
        global loseCounter
        loseCounter += 1

def door2():
    clearText()
    print("The door swings to a corridor that ends abruptly in darkness. ❌ Wrong choice — this path goes nowhere.")
    time.sleep(.33)
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        extraLifeCounter -= 1
    else:
        global loseCounter
        loseCounter += 1

def door3():
    clearText()
    print("You enter, but the floor feels unstable. ❌ Wrong choice — retreat is your only option.")
    time.sleep(.33)
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        extraLifeCounter -= 1
    else:
        global loseCounter
        loseCounter += 1

def door4():
    clearText()
    print("Inside, a whisper promises guidance, but when you step forward, it vanishes. ❌ Wrong choice — you’re back where you started.")
    time.sleep(.33)
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        extraLifeCounter -= 1
    else:
        global loseCounter
        loseCounter += 1

def door5():
    clearText()
    print("The door opens smoothly, revealing a faintly glowing path that seems to call you forward. ✅ Correct choice — And the mission is a success!\n")
    crown()
    time.sleep(.33)
    global winCounter
    winCounter += 1

def whyDoor():
    clearText()
    global loseCounter
    print("Why would you even choose this, you know what.... Just for that you get 7 losses, I dont care")
    time.sleep(1)
    print("You deserve this.. Extra lives wont save you.")
    print("losses: " +str(loseCounter))
    time.sleep(1)
    print("VV")
    time.sleep(1)
    loseCounter += 7
    print("losses: " +str(loseCounter))
    time.sleep(1)
    print("\nHaha")
    time.sleep(1)
    endMsg()

## End of Door Replies ##

def enterThroughBreach():
    clearText()
    tsr1 = "You breach the opening at the perfect moment and catch the enemies off guard.\n\
With the room secured, you spot \033[1;31m5\033[0m door with a plaque says the following: "
    typeWriter(tsr1)
    time.sleep(.67)
    print("\n")
    print("""A distorted voice echoes:

“Only one path leads to survival.”

You must choose wisely. """)
    print("\n\n")
    print("""\033[1mDoor 1:\033[0m “The treasure is not behind me. At least one of the next two doors lies.”

\033[1mDoor 2:\033[0m “Door 1 is lying. The treasure is behind me or Door 5.”

\033[1mDoor 3:\033[0m “Door 2 is telling the truth, but the treasure is not behind me.”

\033[1mDoor 4:\033[0m “Exactly one of these five doors hides the treasure, and it is not me.”

\033[1mDoor 5:\033[0m “Door 3 lies, and the treasure is not behind Door 2.

\033[1mDoor 6:\033[0m "I am not in this riddle and im scared (dont do it.. it fails) (seriously)" """)
    chooseOption(6)
    if choice == 1:
        door1()
    elif choice == 2:
        door2()
    elif choice == 3:
        door3()
    elif choice == 4:
        door4()
    elif choice == 5:
        door5()
    else:
        whyDoor()
def dropIn():
    clearText()
    tdi1 = "You drop into the building through a skylight."
    typeWriter(tdi1)
    time.sleep(.67)
    print("\n")
    print("What Will You Do?")
    print("   1. Enter Objective")
    print("   2. Enter Through Breach")
    chooseOption(2)
    clearText()
    if choice == 1:
        enterObjective()
    else:
        enterThroughBreach()

##### Level B2 ##

def oneTry():
    win = random.randint(1, 100)
    global doubleLuckCounter, extraLifeCounter, winCounter, loseCounter
    if doubleLuckCounter >= 1:
        if win <= 70:
            print("Double Luck Used!")
            print("You win the 70/30, nice job!")
            print(win)
            winCounter += 1
            doubleLuckCounter -= 1
            crown()
        else:
            if extraLifeCounter >= 1:
                print("An Extra Life Has Saved You!")
                print("You \033[1;31mlost\033[0m the 70/30 \U0001F61E")
                print("+0 Loss")
                doubleLuckCounter -= 1
                extraLifeCounter -= 1
            else:
                print("You \033[1;31mlost\033[0m the 70/30 \U0001F61E")
                loseCounter += 1
                doubleLuckCounter -= 1

    else:
        if win <= 35:
            print("You win the 35/65, nice job!")
            print(win)
            winCounter += 1
            crown()
        else:
            if extraLifeCounter >= 1:
                print("An Extra Life Has Saved You!")
                print("You \033[1;31mlost\033[0m the 35/65 \U0001F61E")
                print("+0 Loss")
                extraLifeCounter -= 1
            else:
                print("You \033[1;31mlost\033[0m the 35/65 \U0001F61E")
                loseCounter += 1

def fourTries():
    j = 0
    l = 0
    global doubleLuckCounter, extraLifeCounter, loseCounter, winCounter
    if doubleLuckCounter >= 1:
        print("Double Luck Used!")
        while j < 4:
            win2 = random.randint(1, 100)
            if win2 >= 1 and win2 <= 16:
                print("You \033[1;32mwin\033[0m the 16% chance \U0001F92F")
                global winCounter
                winCounter += 1
                crown()
                l = 67  # hehe 67
                doubleLuckCounter -= 1
                break
            else:
                j += 1
                print(win2)

            if j >= 4:
                if extraLifeCounter >= 1:
                    print("An Extra Life Has Saved You!")
                    print("You lost \U0001F61E")
                    print("+0 Loss")
                    doubleLuckCounter -= 1
                    extraLifeCounter -= 1
                else:
                    print("You lost \U0001F61E")
                    global loseCounter
                    loseCounter += 1
                    doubleLuckCounter -= 1
    else:
        while j < 4:
            win2 = random.randint(1, 100)
            if 1 <= win2 <= 8:
                print("You \033[1;32mwin\033[0m the 8% chance \U0001F92F")
                winCounter += 1
                crown()
                l = 67  # hehe 67
                break
            else:
                j += 1
                print(win2)

            if j >= 4:
                if extraLifeCounter >= 1:
                    print("An Extra Life Has Saved You!")
                    print("You lost \U0001F61E")
                    print("+0 Loss")
                    extraLifeCounter -= 1
                else:
                    print("You lost \U0001F61E")
                    loseCounter += 1

def silentTakedown():
    clearText()
    tst1 = "You take the stairs quietly to avoid detection."
    typeWriter(tst1)
    time.sleep(.67)
    print("\n")
    print("What Next?")
    print("   1. 1 Try, 35% Chance Win (1-35 in 1-100)")
    print("   2. 4 Tries, 8% Chance per try (1-8 in 1-100)")
    chooseOption(2)
    clearText()
    if choice == 1:
        oneTry()
    else:
        fourTries()

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
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
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
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

##### Level B3 ##

def roofHop():
    global extraLifeCounter
    clearText()
    time.sleep(.67)
    print("\n")
    print("""
    Wind howls across the rooftop as your boots hit concrete.
Your drone feed glitches—then freezes on a locked access panel.
A distorted signal pulses across the screen, repeating in fragments.

The door won’t open unless you understand the message.
One mistake, and the defenders will know exactly where you are.
(Hint.. Binary)
    """)
    time.sleep(.67)
    print("""
“\nBlank, Two lights flick, one blank.
A pause of blanks.
Blank, then three blinks.”

The door accepts:
• what is seen
• what is counted
• what is translated

What is the code?
""")
    o = 0
    while o < 5:
        codeGuessInput = input("\n>>> ")
        if codeGuessInput.isdigit():
            codeGuess = int(codeGuessInput)
            correctAnswer = 607
            if 0 <= codeGuess <= 999:
                if codeGuess == correctAnswer:
                    clearText()
                    print("The anticipation...\n")
                    time.sleep(2)
                    print("Did you get it?\n")
                    time.sleep(2)
                    print("You did it! Good Job!!! The code binary code was 0110 0000 0111\n\
                    and the mission is successful")
                    global winCounter
                    winCounter += 1
                    crown()
                    break
                elif codeGuess != correctAnswer:
                    if extraLifeCounter >= 1:
                        clearText()
                        print("The anticipation...")
                        time.sleep(2)
                        print("Did you get it?")
                        time.sleep(2)
                        print("Incorrect code entered. Enemy forces respond—mission failed.\n")
                        time.sleep(.33)
                        print("An Extra Life Saved You!")
                        print("+0 Losses")
                        extraLifeCounter -= 1
                        break
                    else:
                        clearText()
                        print("The anticipation...")
                        time.sleep(2)
                        print("Did you get it?")
                        time.sleep(2)
                        print("Incorrect code entered. Enemy forces respond—mission failed.\n")
                        time.sleep(.33)
                        endMsg()
                        global loseCounter
                        loseCounter += 1
                        break
                else:
                    print("testing.. uh what..?")
            else:
                print("Hint, range from 0-999")
        else:
            print("Please Enter a number")


##### Level B4 ##

def abortMission():
    clearText()
    tam1 = "You decide the rooftop approach is too risky and pull back. While retreating, the enemies secure the building, and the operation is called off."
    typeWriter(tam1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

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
    global doubleLuckCounter, extraLifeCounter, winCounter, loseCounter
    if doubleLuckCounter >= 1:
        print("Double Luck Used!")
        while rep < 2:
            shadowMoveInput = input("\n(1-67)  >>> ")
            if shadowMoveInput.isdigit():
                shadowMoveGuess = int(shadowMoveInput)
                if 1 <= shadowMoveGuess <= 67:
                    shadowMoveNum = random.randint(1, 67)
                    shadowMoveNum2 = random.randint(1,67)
                    if shadowMoveNum == shadowMoveNum2:
                        shadowMoveNum = random.randint(1, 67)
                        shadowMoveNum2 = random.randint(1, 67)
                        if shadowMoveGuess == shadowMoveNum or shadowMoveGuess == shadowMoveNum2:
                            print("Wow. You.. Actually... Won... Good Job!")
                            global winCounter
                            winCounter += 1
                            crown()
                            rep += 5
                            doubleLuckCounter -= 1
                        else:
                            if extraLifeCounter >= 1:
                                print("Extra Life Saved You!")
                                print("You lost \U0001F61E")
                                print("+0 Loss")
                                rep += 5
                                extraLifeCounter -= 1
                                doubleLuckCounter -= 1
                            else:
                                print("You lost \U0001F61E")
                                global loseCounter
                                loseCounter += 1
                                rep += 5
                                doubleLuckCounter -= 1
                    else:
                        if shadowMoveGuess == shadowMoveNum or shadowMoveGuess == shadowMoveNum2:
                            print("Wow. You.. Actually... Won... Good Job!")
                            winCounter += 1
                            crown()
                            rep += 5
                            doubleLuckCounter -= 1
                        else:
                            if extraLifeCounter >= 1:
                                print("Extra Life Saved You!")
                                print("You lost \U0001F61E")
                                print("+0 Loss")
                                rep += 5
                                extraLifeCounter -= 1
                                doubleLuckCounter -= 1
                            else:
                                print("You lost \U0001F61E")
                                loseCounter += 1
                                rep += 5
                                doubleLuckCounter -= 1
                else:
                    print("I said from 1-67, no more, no less..")
            else:
                print("Invalid Input. No Letters!")
    else:
        while rep < 2:
            shadowMoveInput = input("\n(1-67)  >>> ")
            if shadowMoveInput.isdigit():
                shadowMoveGuess = int(shadowMoveInput)
                if 1 <= shadowMoveGuess <= 67:
                    shadowMoveNum = random.randint(1, 67)
                    if shadowMoveGuess == shadowMoveNum:
                        print("Wow. You.. Actually... Won... Good Job!")
                        winCounter += 1
                        crown()
                        rep += 5
                    else:
                        if extraLifeCounter >= 1:
                            print("Extra Life Saved You!")
                            print("You lost \U0001F61E")
                            print("+0 Loss")
                            rep += 5
                            extraLifeCounter -= 1
                        else:
                            print("You lost \U0001F61E")
                            loseCounter += 1
                            rep += 5
                else:
                    print("I said from 1-67, no more, no less..")
            else:
                print("Invalid Input. No Letters!")


## C2 #

def useFlashlight():
    clearText()
    tsa1 = "You light the area to see better, but your position is immediately revealed."
    typeWriter(tsa1)
    time.sleep(.67)
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

## C3 #

def useSupplies():
    clearText()
    global winCounter, loseCounter, extraLifeCounter
    print("The supply room is locked with an old mechanical keypad. Strange numbers and symbols are etched into the wall.\n\
You only have \033[1;31mtwo tries\033[0m to solve the puzzle and unlock the door to use the gear inside—\033[31mfail, and the supplies remain out of reach\033[0m.")
    time.sleep(.67)
    print("The Code is the result of this \033[1;32mFormula\033[0m")
    print("((12 × 7) + 48 ÷ 6) × 3 - 25 + (18 ÷ 3) + 14")
    numericCodeGuess = input("What is the code?\n\
>>> ")
    numericCodeAnswer = '271'
    wrongCounter = 0
    for _ in range(2):
        if numericCodeGuess == numericCodeAnswer:
            print("You cracked the code and completed the objective. Well done!")
            winCounter += 1
            crown()
        elif wrongCounter == 0:
            print("You're Wrong, Try again!")
            wrongCounter += 1
        elif wrongCounter == 1:
            if extraLifeCounter >= 1:
                print("Extra Life Saved You!")
                print("The code was incorrect, and the objective was lost.")
                print("+0 Loss")
                extraLifeCounter -= 1
                break
            else:
                print("The code was incorrect, and the objective was lost.")
                loseCounter += 1
                break
        else:
            print("You should not see this...")
            pass

def moveDeeper():
    clearText()
    tmd1 = "You push deeper into the garage, but the noise echoes through the structure.\n\
Enemy patrols close in, forcing you to abort the mission."
    typeWriter(tmd1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
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
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

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

## C4 #

def sideEntrance():
    clearText()
    tse12 = "You discover a side entrance connected to the garage and slip inside undetected. The enemies never see you coming, and you secure the objective successfully."
    typeWriter(tse12)
    time.sleep(.67)
    print("\n")
    global winCounter
    winCounter += 1
    crown()

def holdPosition():
    clearText()
    thp1 = "Holding your position gives the enemies time to regroup and sweep the area. You’re discovered, and the mission ends."
    typeWriter(thp1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

def reroute():
    clearText()
    trr1 = "You attempt to reroute through another section of the garage, but lose valuable time. Enemy patrols block your path, forcing you to abort the mission."
    typeWriter(trr1)
    time.sleep(.67)
    print("\n")
    global extraLifeCounter
    if extraLifeCounter >= 1:
        print("You lost, but an extra life saved you!")
        print("+0 Losses")
        time.sleep(1.33)
        endMsg()
        extraLifeCounter -= 1
    else:
        endMsg()
        global loseCounter
        loseCounter += 1

def retreat():
    clearText()
    tsa1 = "You fall back to rethink your approach and spot a safer entry route."
    typeWriter(tsa1)
    time.sleep(.67)
    print("\n")
    print("What Next?")
    print("   1. Reroute")
    print("   2. Hold Position")
    print("   3. Side Entrance")
    chooseOption(3)
    clearText()
    if choice == 1:
        reroute()
    elif choice == 2:
        holdPosition()
    else:
        sideEntrance()

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
    global introSkipCounter
    introSkipCounter += 100

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
    print("What Will You Do?")
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

def quitNow():
    clearText()
    print("Quitting...")
    time.sleep(1.5)
    sys.exit(0)

def exitShop():
    playAgain()

def secretCodeVar():
    global winCounter
    clearText()
    returnText = "return"
    answer = str(input("What is the secret code? ('return' to return)\n\
>>> "))
    if answer == 'wwssadadba':
        print("Nice, Secret Developer Cheat Code")
        print("+15 Wins")
        winCounter += 15
        time.sleep(1)
        playAgain()
    elif answer == returnText:
        enterSecretCode()
    elif answer == 'give1000wins':
        print("Uhhh, Okay..? +1000 Wins")
        winCounter += 1000
    else:
        print("Wrong Code, Try Again..")

def enterSecretCode():
    clearText()
    print("\033[1mWhy are you here?\033[0m")
    print("1. I am going to try the \033[1;31mSecret Code\033[0m.")
    print("2. Sorry, wrong place (return)")
    chooseOption(2)
    if choice == 1:
        secretCodeVar()
    else:
        shop()

def doubleLuck():
    clearText()
    global loseCounter, winCounter, doubleLuckCounter
    print("Doubles your odds of winning in a chance-based challenge")
    print("3 per purchase, -1 per luck based challenge. Each use applies to one challenge only.")
    print("Costs:\n")
    print("""
▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄
▌        ▐  ▌        ▐  ▌        ▐
▌1.3 Wins▐  ▌2.5 Loss▐  ▌3.Return▐
▌        ▐  ▌        ▐  ▌        ▐
▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀
    """)
    chooseOption(3)
    if choice == 1:
        if winCounter >= 3:
            doubleLuckCounter += 3
            winCounter -= 3
            print("Success!")
            print("\033[1;32mDouble Luck Uses\033[0m: " + str(doubleLuckCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(winCounter))
        else:
            print("You cannot afford this option, you need more wins!")
            print("\033[1;32mDouble Luck Uses\033[0m: " + str(doubleLuckCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(winCounter))
            time.sleep(1)
            print("Enter to return to shop")
            pause()
            shop()
    elif choice == 2:
        if loseCounter >= 5:
            doubleLuckCounter += 3
            loseCounter -= 5
            print("Success!")
            print("\033[1;32mDouble Luck Uses\033[0m: " + str(doubleLuckCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(loseCounter))
        else:
            print("You cannot afford this option, you need more losses!")
            print("\033[1;32mDouble Luck Uses\033[0m: " + str(doubleLuckCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(loseCounter))
            time.sleep(1)
            print("Enter to return to shop")
            pause()
            shop()
    else:
        print("Returning to shop...")
        time.sleep(1.5)
        shop()

def giveCode():
    clearText()
    print("Sucks you are down bad for the code, but it is simply...")
    pause()
    clearText()
    print("The Konami code using w, a, s, d for directions. Start is enter (to submit reply)")
    pause()
    shop()

def specialMessage():
    clearText()
    print("""
    Traveler, the path ahead hides rewards for those who remember the old sequence of steps:
\033[1mStep forward twice, then retreat twice.
Turn left, then right, then left again, followed by right.
Tap A, then B, and finally take a leap to start anew.
Only by following this secret rhythm exactly will the hidden door open.\033[0m
(Hint, secret code is coded in wasd)
""")
    print("1. I cant do it, just give me the code \U0001FAE0")
    print("2. Return, I got this!")
    chooseOption(2)
    if choice == 1:
        giveCode()
    else:
        shop()

def extraLife():
    clearText()
    global extraLifeCounter, winCounter, loseCounter
    print("Prevents a loss in a challenge.")
    print("3 per purchase, -1 per loss. Each use applies to one challenge only.")
    print("Costs:\n")
    print("""
    ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄
    ▌        ▐  ▌        ▐  ▌        ▐
    ▌1.5 Wins▐  ▌2.7 Loss▐  ▌3.Return▐
    ▌        ▐  ▌        ▐  ▌        ▐
    ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀
        """)
    chooseOption(3)
    if choice == 1:
        if winCounter >= 5:
            extraLifeCounter += 3
            winCounter -= 5
            print("Success!")
            print("\033[1;35mExtra Lives\033[0m: " + str(extraLifeCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(winCounter))
        else:
            print("You cannot afford this option, you need more wins!")
            print("\033[1;35mExtra Lives\033[0m: " + str(extraLifeCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(winCounter))
            time.sleep(1)
            print("Enter to return to shop")
            pause()
            shop()
    elif choice == 2:
        if loseCounter >= 7:
            extraLifeCounter += 3
            loseCounter -= 7
            print("Success!")
            print("\033[1;35mExtra Lives\033[0m: " + str(extraLifeCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(loseCounter))
        else:
            print("You cannot afford this option, you need more losses!")
            print("\033[1;35mExtra Lives\033[0m: " + str(extraLifeCounter))
            print("Your Current \033[1;32mBalance\033[0m: " + str(loseCounter))
            time.sleep(1)
            print("Enter to return to shop")
            pause()
            shop()
    else:
        print("Returning to shop...")
        time.sleep(1.5)
        shop()

def shop():
    if winCounter >= 10 and loseCounter >= 10:
        clearText()
        print("""
          ▄φφφφφφφφφφφφφSHOPφφφφφφφφφφφφ▄  
         █                               █ 
        ▐▌ 1. Double Luck        5. Exit ▐▌
        █▌ 2. Special Message            ▐█
        █▌ 3. Extra Life                 ▐█
        █▌ 4. Enter Secret Code          ▐█
        ▐▌                 Wins: """ + str(winCounter) + """      ▐▌
         █                 Losses: """ + str(loseCounter) + """    █ 
          ▀φφφφφφφφφφφφφφφφφφφφφφφφφφφφφ▀""")
    elif winCounter < 10 and loseCounter < 10:
        clearText()
        print("""
          ▄φφφφφφφφφφφφφSHOPφφφφφφφφφφφφ▄  
         █                               █ 
        ▐▌ 1. Double Luck        5. Exit ▐▌
        █▌ 2. Special Message            ▐█
        █▌ 3. Extra Life                 ▐█
        █▌ 4. Enter Secret Code          ▐█
        ▐▌                 Wins: """ + str(winCounter) + """       ▐▌
         █                 Losses: """ + str(loseCounter) + """     █ 
          ▀φφφφφφφφφφφφφφφφφφφφφφφφφφφφφ▀""")
    elif 100 <= winCounter <= 9999:
        clearText()
        print("""
                  ▄φφφφφφφφφφφφφSHOPφφφφφφφφφφφφ▄  
                 █                               █ 
                ▐▌ 1. Double Luck        5. Exit ▐▌
                █▌ 2. Special Message            ▐█
                █▌ 3. Extra Life                 ▐█
                █▌ 4. Enter Secret Code          ▐█
                ▐▌                 Wins: """ + str(winCounter) + """    ▐▌
                 █                 Losses: """ + str(loseCounter) + """     █ 
                  ▀φφφφφφφφφφφφφφφφφφφφφφφφφφφφφ▀""")
    elif winCounter >= 10:
        clearText()
        print("""
          ▄φφφφφφφφφφφφφSHOPφφφφφφφφφφφφ▄  
         █                               █ 
        ▐▌ 1. Double Luck        5. Exit ▐▌
        █▌ 2. Special Message            ▐█
        █▌ 3. Extra Life                 ▐█
        █▌ 4. Enter Secret Code          ▐█
        ▐▌                 Wins: """ + str(winCounter) + """      ▐▌
         █                 Losses: """ + str(loseCounter) + """     █ 
          ▀φφφφφφφφφφφφφφφφφφφφφφφφφφφφφ▀""")
    else:
        clearText()
        print("""
          ▄φφφφφφφφφφφφφSHOPφφφφφφφφφφφφ▄  
         █                               █ 
        ▐▌ 1. Double Luck        5. Exit ▐▌
        █▌ 2. Special Message            ▐█
        █▌ 3. Extra Life                 ▐█
        █▌ 4. Enter Secret Code          ▐█
        ▐▌                 Wins: """ + str(winCounter) + """       ▐▌
         █                 Losses: """ + str(loseCounter) + """    █ 
          ▀φφφφφφφφφφφφφφφφφφφφφφφφφφφφφ▀""")
    chooseOption(5)
    if choice == 1:
        doubleLuck()
    elif choice == 2:
        specialMessage()
    elif choice == 3:
        extraLife()
    elif choice == 4:
        enterSecretCode()
    else:
        exitShop()
    # Idea, get ascii and make a gui non-interactable but use chooseOption() to pick things

def funFact():
    clearText()
    print("\033[1;32mFun Fact\033[0;1m, This Game \033[1;35m34+\033[0;1m Possible Game Endings\033[0m\n\
As well as 1591 Lines Of Code, About One 1131th Of Minecraft's")
    time.sleep(1.5)

def level_1_entry(): #######################temp commented out
    if textSkipCounter < 3:
        tl1e1 = "You arrive outside the building where \033[1mhostages\033[0m are being held. "
        tl1e2 = "Police sirens echo behind you as your team waits for your command.\n"
        tl1e3 = "This is the moment where \033[1;32myou\033[32m decide how to enter the building\033[0m, knowing that your choice will affect how \033[1;31mdangerous\033[0m the mission becomes.\033[0m"
        typeWriter(tl1e1)  # tl1e means "text level 1 entry" text 1
        time.sleep(.16)
        typeWriter(tl1e2)  # tl1e text 2
        time.sleep(.225)
        typeWriter(tl1e3)  # tl1e text 3
    else:
        print("You arrive outside the building where \033[1mhostages\033[0m are being held.\
Police sirens echo behind you as your team waits for your command.\n\
This is the moment where \033[1;32myou\033[32m decide how to enter the building\033[0m, knowing that your choice will affect how \033[1;31mdangerous\033[0m the mission becomes.\033[0m\n")

    print("\n\n\033[1;32mWins\033[0m: " + str(winCounter))
    print("\033[1;31mLosses\033[0m: " + str(loseCounter))
    print("\033[1;32mDouble Luck Uses\033[0m: " + str(doubleLuckCounter))
    print("\033[1;35mExtra Lives\033[0m: " + str(extraLifeCounter))

    time.sleep(.25)
    print("\n")
    print("Where Will You Go?")
    print("   1. Front Lobby")
    print("   2. Rooftop Rappel")
    print("   3. Parking Garage")
    shopAndQuit()
    chooseOption(6)
    if choice == 1:
        frontLobby()
    elif choice == 2:
        rooftopRappel()
    elif choice == 3:
        parkingGarage()
    elif choice == 4:
        shop()
    elif choice == 5:
        quitNow()
    else:
        funFact()

def startGame():
    pause()
    time.sleep(.75)
    clearText()
    level_1_entry()

############## Main Loop ##############
while True:
    # start game function
    if introSkipCounter <= 0:
        gameIntro()
    else:
        skipIntro()
    startGame()
    playAgain()
