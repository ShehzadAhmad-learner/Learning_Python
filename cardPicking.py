import random
RandomSeed = int(input("Enter the seed number\n"))
random.seed(RandomSeed)
NameAsCSV = input("enter the everybodies name, among whom can be selected for paying\n")
name = NameAsCSV.split(", ")
people = len(name)

selectednumber = random.randint(0,people-1)
print(name[selectednumber]," is going to pay for meal today")
if selectednumber==0:
    print(name[0]," is Selected for Paying Every Bodies Meal")
elif selectednumber==1:
    print(name[1]," is Selected for Paying Every Bodies Meal")
elif selectednumber==2:
    print(name[2]," is Selected for Paying Every Bodies Meal")
elif selectednumber==3:
    print(name[3]," is Selected to pay for everyboies meal Today")
else:
    print(name[4]," is Selected for Paying Every Bodies Meal")
