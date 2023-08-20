print("Welcome to Love Calculator")
name1 = input("Enter your name\n")
your_name = name1.lower()
name2 = input("Enter your love's name\n")
love_name = name2.lower()
combined_love = your_name + love_name
t = combined_love.count("t")
r = combined_love.count("r")
u = combined_love.count("u")
e = combined_love.count("e")
true_score = t+r+u+e
l = combined_love.count("l")
o = combined_love.count("o")
v = combined_love.count("v")
e = combined_love.count("e")
love_score = l+o+v+e
new_score = str(true_score)+str(love_score)
print(new_score)
int_new_score = int(new_score)
if int_new_score<10 or int_new_score>90:
    print(f"your score is {int_new_score}, your go together like coke and mentos.")
elif int_new_score>40 and int_new_score<50:
    print(f"your score is {int_new_score}, you are alright together")
else:
    print(f"your score is {int_new_score}"
          )