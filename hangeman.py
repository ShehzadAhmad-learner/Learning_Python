import random
from replit import clear

world_list =["shehzad","fawad","hammad"]

stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#randomly chosing
chosen = random.choice(world_list)
word_len = len(chosen)
print(chosen)
display = []
#displaying _ in blank spaces
for _ in range(word_len):
    display += "_"
print(display)
#chosing an end point
end_of_game = False
lives = 7
anime=0
undisplay =[]
while not end_of_game:

    guess = input(f"Enter \n").lower()
    if guess in display:
        print(f"you have already entered {letter}")
    else:
            
        for position in range(word_len):
            letter = chosen[position]
        #  print(f"current Position :{position}\n current letter :{letter}\n current guess :{guess}")
            if letter==guess:
                display[position]=letter
        print(display)
        if guess not in chosen:
            
            print(stage[anime])
            anime+=1
            lives-=1
            if lives==0:
                end_of_game=True
                print("you lose")
            
        if "_" not in display:
            end_of_game = True
            print("you win")