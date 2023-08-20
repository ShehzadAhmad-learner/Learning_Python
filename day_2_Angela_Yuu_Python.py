# print(3+2)
# print(int(3*3+3/3-3))
# height1 = int(input("Enter Your Height in inches\n"))
# weight = int(input("Enter Your Weight in Kilograms\n"))
# Height = (height1*2.53/100)
# BMI = (weight/(Height**2))
# print("your BMI = ",BMI)
# if BMI<18.5:
#     print("common eat something you are like matchstick")
# elif 25< BMI >18.5:
#     print("you are really smart Good Job")
# elif 30<BMI>25:
#     print("you just need to  work alitlle bit more and your are gonna look like Tome cruise")
# else:
#     print("your are really Obese I know you are from eating family but atleast do exercise you are gonna blust")
#Tip Calculator
print("Welcome to Tip calcualtor")
Total_Bill = int(input("Enter your total Bill: $"))
Percentage_of_tip = int(input("Amount of Tip You want to pay 10% , 20% or 25%\n"))
tip = Percentage_of_tip * Total_Bill/ 100
Total_people = int(input("Amoung how many people you want to share bill? \n"))
print("the amount of bill each person have to pay = $",(tip+Total_Bill)/Total_people)