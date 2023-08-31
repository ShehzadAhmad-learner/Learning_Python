alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input(f"enter encode to encrypt your message or decode for decrypt your message\n")


text = input("Enter your text here\n").lower()
shift = int(input(f"enter the value for shifting message\n"))
def common_ground():
    note_text = ""
    for letter in note_text:
        
        position = alpha.index(letter)
        new_position = position + shift_amount
        new_letter = alpha[new_position]
        note_text +=new_letter
    print(note_text)
def encrypt(note_text, shift_amount):
    common_ground()
def decrypt(note_text,shift_amount):
    common_ground()


if direction=="encode":
    print("Thank You for selecting enryption")
    encrypt(note_text=text,shift_amount=shift)
elif direction=="decode":
    print("Thank You for selecting deryption")
    decrypt(note_text=text,shift_amount=shift)


