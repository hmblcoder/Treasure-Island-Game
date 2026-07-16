print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


level_one = input("You have 2 paths to choose from, where does your heart direct you, adventurer?\n      Type 'Left' or 'Right'\n      ")
if level_one == "Right" or level_one == "right":
    print("Your heart is pure and guides you to a giant mountain.")
    level_two = input("There are 2 paths leading to the top, which will you choose?\n     'Left' or 'Right'?\n      ")
    if level_two == "Left" or level_two == "left":
        print("As you climb the steep steps you feel as if you are being followed")
        level_three = input("You turn around and see a group of bandits running towards you. You have 2 options, enter a dark cave on the Left or attempt to slide down the mountain on your Right.\n     'Left' or 'Right'?\n      ")
        if level_three == "left" or level_three == "Left":
            print("As you enter the cave a bunch of rocks fall and block the entrance, you hear the bandits walk away.")
            print("You look ahead in the cave and find the treasure chest! However you are not sure how to get out.")
            print("Upon closer inspection you notice there are 2 doorways on your Left and Right, both leading to dimly lit corridors.")
            level_four = input("Which door will you choose?\n     'Left' or 'Right'?\n      ")
            if level_four == "right" or level_four == "Right":
                print("You follow the path for what seems like eternity to reach an opening back to the island!\n     YOU WIN!")



            elif level_four == "left" or level_four == "Left":
                print("You follow the path for what seems like eternity and fall into a spike trap\n     GAME OVER")

        elif level_three == "right" or level_three == "Right":
            print("As you try to slide down the mountain you lose your footing and fall to your demise.\n     GAME OVER")

    elif level_two == "Right" or level_two == "right":
        print("As you climb the steep steps you are ambushed by a group of bandits\n     GAME OVER")

elif level_one == "Left" or level_one == "left":
    print("Your heart has misguided you and now your path ends here\n      GAME OVER")






