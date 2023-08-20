print("Welcome to Treasure Island.\nYour Mission is to find the treasure.")
cross_road = input("you are a road cross over where do  do you want to go?\nYou have two direction 'left' or 'right' type as it is\n")
if cross_road == 'left':
    bank_river = input("Now you are at the bank of river which is full of crocodiles \nDo you want to swim or wait for boat\ntype swim if you want to swim or wait if you want to wait\n")
    if bank_river == "wait":
        door = input("you have reached the doorstep of treasure \nnow there are three doors as Red, Blue and Yellow \nType the same name for the door you want to choose\n")
        if door=="Yellow":
            print("congrats You have found the treasure, Your have won!")
        elif door=="Blue":
            print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")