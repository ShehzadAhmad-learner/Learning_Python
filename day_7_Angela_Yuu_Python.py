import random
world_list =["shehzad","fawad","hammad"]
chosen = random.choice(world_list)
word_len = len(chosen)
print(chosen)
display = []
for _ in range(word_len):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:

    guess = input(f"Enter \n").lower()
    for position in range(word_len):
        letter = chosen[position]
        print(f"current Position :{position}\n current letter :{letter}\n current guess :{guess}")
        if letter==guess:
            display[position]=letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")
