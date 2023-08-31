
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(direction, text, shift):
    recommended_text = ""
    for letter in text:
        if letter in alpha:

            position = alpha.index(letter)
            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift
            new_letter = alpha[new_position]
            recommended_text+=new_letter
        else:
            recommended_text += letter
    print(f"your recommended text is {recommended_text}")
# ceaser(direction=direction, text=text, shift=shift1)
should = True
while should==True:
    direction = input(f"enter encode to encrypt your message or decode for decrypt your message\n")


    text = input("Enter your text here\n").lower()
    shift = int(input(f"enter the value for shifting message\n"))
    if shift>26:
        shift1 = shift%26
    else:
        shift1=shift
    
    ceaser(direction=direction, text=text, shift=shift1)
    answer = input("Do you want to do more? If yes type yes or no\n").lower()
    if answer == "yes":
        should=True
    elif answer=="no":
        should=False
    else:
        print("kindly answer correctly")
        answer = input("Do you want to do more? If yes type yes or no\n").lower()
        if answer == "yes":
            should=True
        elif answer=="no":
            should=False

print("Goodbye")