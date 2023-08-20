# #To check if a number that is input is odd or even?
# Num = int(input("Enter a number to check if it is odd or even: "))
# if Num % 2 == 0:
#     print("The number ",Num,"You just entered is even")
# else:
#     print("The number ",Num,"is odd")
# #RollerCoster
# height = int(input("Enter your height in centimeters.\n"))
# if height>=120:
#     print("yes you can ride:)")
#     age = int(input("Enter your age so we can tell you about your ticket"))
#     if age <12:
#         print("you have to pay $7. ")
#     elif age >= 18:
#         print("you have to pay $12 ")
#     else:
#         print("your ticket for roller coaster is $18")
# else:
#     print("sorry but you have to grow before you can ride a rollercoasater:")
# height = float(input("Enter Your Height in Meters:\n"))
# weight = float(input("Enter Your Weight in Kg:\n"))
# bmi = weight/height**2
# if bmi<18.5:
#     print("you are underweight")
# elif bmi<25:
#     print("you have normal weight")
# elif bmi<30:
#     print("you are slightly overweight")
# elif bmi<35:
#     print("You are Obese") 
# else:
#     print("You are slightly obese")
# year = int(input("Enter the year you want to know about if it is leap year or not:\n"))
# if year%4==0:
#     print("This year might be a leap year if it obeys certain rules")
#     if year%100==0:
#         print("this can be a leap year")
#         if year%400:
#             print(year," this is a leap Year")
#         else:
#             print("This is not a leap year")
#     else:
#         print(year, "this is a leap year")
# else:
#     print(year, "this year is not a leap year")
# print("Welcome to the Rollercoster!")
# height = int(input("Enter your height in cm\n"))
# bill = 0
# if height>120:
#     print("you are eligible for Rollercoaster ride!Hooray")
#     age = int(input("enter your age\n"))
#     if age<12:
#         bill=7
#         print("For children bill is $7")
#     elif age<18:
#         bill=9
#         print("For Teenager bill is $9")
#     else:
#         bill=12
#         print("For adults bill is $12")
#     photo = (input("Do you want to take photo with Rollercoaster? If yes type 'Y' if no type 'n'"))
#     photo.upper
#     if photo=='Y':
#         bill+=3
#     print(f"Your final bill is ${bill}")
    
# else:
#     print("Sorry to say but you need to be taller than 120cms")
# print("Welcome to PizzaHub")
# bill1= 0
# want_pizza = input("Do you want pizza?if yes type Y if no type N\n")
# if want_pizza == "Y":
#     size = input("which size of pizza do you want?Type S for small M for medium and L for large\n")
#     if size == 'S':
#         bill1 = 15
#         print(f"The cost for small pizza is ${bill1}")
#         add_pepperoni = input("Do you want Pepperoni?if yes type Y else N\n")
#         if add_pepperoni =="Y":
#             bill1+=2
#     elif size=='M':
#         bill1=20
#         print(f"The cost for medium pizza is ${bill1}")
#         add_pepperoni = input("Do you want Pepperoni?if yes type Y else N\n")
#         if add_pepperoni =="Y":
#             bill1+=3
#     else:
#         bill1 = 25
#         print(f"The cost for large pizza is ${bill1}")
#         add_pepperoni = input("Do you want Pepperoni?if yes type Y else N\n")
#         if add_pepperoni =="Y":
#             bill1+=3   
#     chesse = input("Do you want extra cheese?if yes type Y else N\n")
#     if chesse =="Y":
#         bill1+=1
#     print(f"Your final bill is ${bill1}")
# else:
#     print("thank you for coming wish to see you buy our pizza next time")
