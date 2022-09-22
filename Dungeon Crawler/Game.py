from email.policy import strict
from time import strftime
import os 


player_Armour =  {}
player_Weapons = {}
inventory = []
player_Health = 0
evasion = 0
user_name = ""
xp = 0
xp_threshold = 5
player_level = 1
player_coins = 0
player_class = ""
run = True
menu = True
play = False
rules = False

def clear():
    os.system("cls")

def draw():
    print("xX-----------------------Xx")

def save_game():
    list = [user_name,
            str(player_Armour),

            ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")

def player_Spec_Warrior():
    global player_Health 
    global evasion
    global player_class
    player_class = "Warrior"
    player_Armour.update({"Breastplate":50})
    player_Weapons.update({"short sword":2})
    player_Health = 50
    evasion = 20

def player_spec_Rogue():
    global player_Health 
    global evasion
    global player_class
    player_class = "Rogue"
    player_Armour.update({"Light Armour":20})
    player_Weapons.update({"dagger":1})
    player_Health = 20
    evasion = 50

def fight():
    pass
        

def enemy_goblin(name : str, health: int):
    return {"name" : name, "Health": health}
    

def start_game_char():
    global user_name
    user_name = input("Enter your name: ")
    global type
    print("Rogue or Warrior")
    type = input("Chose your Class: ")
    print(f"Welcome {user_name}, You are about to find yourself trapped on a strange and dangerous island on one of the most forbidding planets in the galaxy: Tenopia.")
    print("Its important that you follow directions if you hope to escape!.")

    if type == "rogue":
        player_spec_Rogue()
        print(f"You have chosen {type}")
        print(player_Armour)
        print(f"Player Health: {player_Health}")
    elif type == "warrior":
        player_Spec_Warrior()
        print(f"You have chosen {type}")
        print(player_Armour)
        print(f"Player Health: {player_Health}")

def greeting():
    if type == "rogue":
        print("Well met rogue, will you be doing some sneaking?")
    elif type == "warrior":
        print("Well met warrior, will you be doing sme tanking today?")


def player_gain_xp(gain_xp):
    global xp_threshold
    global xp
    global player_level

    xp = xp + gain_xp
    if xp > xp_threshold:
        player_level +=1
        xp = 0
        print(f"You have gained{gain_xp}xp and leveled up to {player_level}")
    else:
        print(f"You have gained{gain_xp}xp")  

def player_take_damage(player_dmg):
    global player_Health
    player_Health -= player_dmg
    if player_Health <= 0:
        print("you have died.")
        quit()
    else:
        print(f"you have taken {player_dmg} damage")

def chose_door_right(user_choice):
    global xp
    global player_Health
    if user_choice == "right":
        print("you have found a treasure cheast")
        player_gain_xp(10)
        ans1a1 = input("Would you like to open the chest: ")
        if ans1a1 == "yes":
            print("you have found a helm")
            player_Armour.update({"helm":10})
        elif ans1a1:
            print("you have passed up on the item")
    elif user_choice == "left":
        print("you have fell down a well, oh no!")
        player_Health -= 30
        if player_Health <= 0:
            print("you have died, Start again")
            quit()
        else:
            print("you have lost 30 health")
            print(f"you now have {player_Health} health left")


def map_one():
    global xp, player_Health
    print("Left or Right")
    ans1 = input("Chose a door: ")
    if ans1 == "right":
        print("you have found a treasure cheast")
        player_gain_xp(10)
        print(f"you now have {xp}xp")
        print()
        ans1a1 = input("Would you like to open the chest: ")
        if ans1a1 == "yes":
            print("you have found a helm")
            player_Armour.update({"helm":10})
        elif ans1a1:
            print("you have passed up on the item")
        ans1a2 = input(f"You now see two doors in front of you, chose wisely you have {player_Health} health left, left or right: ")
        if ans1a2 == "right":
            print("you have found a treasure cheast")
            xp += 100
            print("you have gained 100xp")
            print(f"you now have {xp}xp")
        elif ans1a2 == "left":
            print("you have fell down a well, oh no!")
            player_take_damage(20)
    elif ans1 == "left":
        print("you have fell down a well, oh no!")
        player_take_damage(10)
        ans1b = input(f"You now see two doors in front of you, chose wisely you have {player_Health} health left, left or right: ")
        chose_door_right(ans1b)




#print(list(enemy1.items())[1])
#map_one()


while run:
    while menu:
        clear()
        draw()
        print("1: New Game")
        print("2: Load Game")
        print("3: Rules")
        print("4: Quit")
        draw()
        menu_choice = input(":> ")

        if menu_choice == "1":
            start_game_char()
            greeting()
            menu = False
            play = True
        elif menu_choice == "2":
            pass
        elif menu_choice == "3":
            pass
        elif menu_choice == "4":
            quit()


    while play:
        save_game()

        draw()
        print("Enter 0 to save and quit")
        draw()


        dest = input(":> ")

        if dest == "0":
            play = False
            menu = True
            save_game()