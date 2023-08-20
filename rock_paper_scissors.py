# '''✋✊✌️
# ✌️'''
# import random
# print("Welcome to rock paper scissor game against Python Vscode")
# your_choice = (input("Enter \n1 or Rock for rock.\n2 or Paper for paper.\n3 or Scissor for scissor\n"))
# if your_choice=="1" or your_choice=="2" or your_choice=="3":
#     your_choice=int(your_choice)
# if your_choice==1 or your_choice=="Rock":
#     print("Rock")
#     print("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)
# elif your_choice==2 or your_choice=="Paper":
#     print("Paper")
#     print("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)
# else:
#     print("Scissor")
#     print("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
# computer_choice = random.randint(1,3)
# if computer_choice==1:
#     print("Rock")
#     print("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)
# elif computer_choice==2:
#     print("Paper")
#     print("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)
# else:
#     print("Scissor")
#     print("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
# if your_choice=="Rock":
#     your_choice=1
# if your_choice=="Paper":
#     your_choice=2
# if your_choice=="Scissor":
#     your_choice=3
# #For Rock
# if your_choice==1  and computer_choice==1:
#     print("its a Draw go for it again")
# elif your_choice==1  and computer_choice==2:
#     print("You lose")
# elif your_choice==1  and computer_choice==3:
#     print("you won")
# #For Paper
# elif your_choice==2 and computer_choice==1:
#     print("You Won Congrats")
# elif your_choice==2  and computer_choice==2:
#     print("its a Draw go for it again")
# elif your_choice==2  and computer_choice==3:
#     print("You Lose")
# #For Scissor
# elif your_choice==3  and computer_choice==1:
#     print("You Lose")
# elif your_choice==3 and computer_choice==2:
#     print("You Won Congrats")
# elif your_choice==3 and computer_choice==3:
#     print("its a Draw go for it again")
# else:
#     print("type Carefully")
import random
print("Welcome to Rock Paper Scissor Game")
user_choice = int(input("Enter\n0 for Rock\n1 for Paper\n2 for Scissor\n"))
computer_choice = random.randint(0,2)

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [Rock, Paper, Scissor]
print(computer_choice)
print('user chooses: ',game_images[user_choice])
print('computer chooses: ',game_images[computer_choice])
if user_choice==0 and computer_choice==2:
    print("You won")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif user_choice<0:
    print("You lose, you typed incorrectly")
elif user_choice>2:
    print("you type incorrectly you lose")
elif user_choice>computer_choice:
    print("You won")
elif computer_choice> user_choice:
    print("You lose")

elif computer_choice==user_choice:
    print("its a draw")
else:
    print("let me check")