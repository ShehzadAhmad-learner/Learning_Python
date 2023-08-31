print("Welcome to the Rollercoster!")
height = int(input("Enter your height in cm\n"))
bill = 0
if height>120:
    print("you are eligible for Rollercoaster ride!Hooray")
    age = int(input("enter your age\n"))
    if age<12:
        bill=7
        print("For children bill is $7")
    elif age<18:
        bill=9
        print("For Teenager bill is $9")
    elif age>=45 and age<=55:
        print("Don't we got you. everything is free for you!")
    else:
        bill=12
        print("For adults bill is $12")
    photo = (input("Do you want to take photo with Rollercoaster? If yes type 'Y' if no type 'n'"))
    photo.upper
    if photo=='Y':
        bill+=3
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry to say but you need to be taller than 120cms")