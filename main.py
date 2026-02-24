############## Import ##############
import random, time, sys, tkinter, os, shutil, platform
from ASCIIArt import gameLogo
# test push
# test pull
############## (Reusable) Definitions ##############

# Typewriter Effect


#  How to use --->   print_centre("enter text here")
def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))


def clearText():
    print(platform.system())
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input("\033[1mPress \033[31mEnter\033[0;1;39m To Continue\033[0m\n")


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
    choice = 0
    while choice < 1 or choice > numOfOpt:
        print("\nChoose A Number 1 to " + str(numOfOpt), end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            choice = int(choice)
        print("\n\n")
        return choice


############## (Single Use/ + Retry Use) Definitions ##############

def gameIntro():
    welcomeText = "\033[1;35mWelcome\033[0m To Operation Lockdown"
    width = 30
    centeredText = welcomeText.center(width)
    print(centeredText)
    gameLogo()
    name = str(input("What Can I Call You?\n\
    >>> "))
    print("\n")
    time.sleep(1.25)
    print("I Hope You Are Ready Mr. " + (name) + ".\n")

    pause()
    clearText()

    text = """\033[1;35mOperation Lockdown\033[0m is a text-based choose-your-own-adventure game inspired by the tactical gameplay of Rainbow Six Siege,\n \
    you will be taking on the role of an elite operator during a \033[1;35mhigh-risk \033[0mhostage rescue mission. \n \
    You will make choices on what happens next, be careful though since some  paths may lead to an \033[1;35mabrupt ending.\033[0m\n \
    There are many different endings, some \033[32mgood\033[0m and some \033[31mbad\033[0m. Have fun."""
    sleep_time = 0.015

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleep_time)
    print("\n\n")
def level_1_entry():
    print("You arrive outside the building where hostages are being held. Police sirens echo behind you as your team waits for your command.\n \
         This is the moment where you decide how to enter the building, knowing that your choice will affect how dangerous the mission becomes.")
    time.sleep(1)
    print("\n")
    print("Where Will You Go?")
    print("   1. Front Lobby")
    print("   2. Rooftop Rappel")
    print("   3. Parking Garage")
    chooseOption(3)
    pause() #stopped here

def startGame():
    pause()
    time.sleep(1.5)
    clearText()
    level_1_entry()



############## ASCII Art ##############


############## Game Options ##############


############## Test Things ##############


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

quit()
