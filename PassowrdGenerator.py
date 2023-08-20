import random
number = ['1','2','3','4','5','6','7','8','9','0']
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# print(len(alphabets))
symbols = ['!','@','#','%','^','&','*','(',')']
question = int(input("Enter how long password do you want?\n"))
q_letter = int(input("How much letters do you want to have?\n"))
q_number = int(input("How much Numbers do you want to have?\n"))
q_symbol = int(input("How much Symbol do you want to have?\n"))
password = []
for char in range(1,q_letter+1):
    random_char = random.choice(alphabets)
    password+=random_char
# print(password)
for num in range(1,q_number+1):
    random_num = random.choice(number)
    password+=random_num
# print(password)
for sym in range(1,q_symbol+1):
    random_sym = random.choice(symbols)
    password+=random_sym
# print(f"You password should be:'{password}'")
random.shuffle(password)
passvard = ""
for pas in list(password):
    passvard +=pas
print(f"Your randomly generated password is {passvard}")