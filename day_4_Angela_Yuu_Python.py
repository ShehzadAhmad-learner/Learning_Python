import random
# random_number = random.randint
# (1,10)
# print(random_number)
# random_float = random.random
# print(random_float)
print("Welcome to the Tossing Program")
YourChoice = input("what do you choose Head or Tail?\n")
toss = random.randint(0,1)
if toss==1:
    print("its Head")
else:
    print("its tail")
if YourChoice == "Head" and toss==1:
    print("Congrats You won")
elif YourChoice=="Tail" and toss==0:
    print("Congrats you have won")
else:
    print("You loose")