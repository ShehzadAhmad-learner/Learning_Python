students_score = {
    "Shehzad":89,
    "Farhan":92,
    "Kamran":90,
    "Ehtisham":84,
    "Majid":87,

}
entry = True
while entry ==True:
    name = input("Enter the student name:\n")
    marks = int(input("Enter their marks in exam\n"))
    students_score[name]=marks
    continues= input("Do you want to input more students marks in the dictionary? if yes type yes else type no\n").lower()
    if continues=="yes":
        entry=True
    elif continues=="no":
        entry=False
    else:
        print("Kindly answer correctly")
        continues= input("Do you want to input more students marks in the dictionary? if yes type yes else type no\n").lower()
        if continues=="yes":
            entry=True
        elif continues=="no":
            entry=False
        
print(students_score)

students_grades = {

}
for key in students_score:
    student_name = key
    values = students_score[key]
    if values<101 or values >0:
        grade=""

        if values>90 and values<=100:
            grade = "Outstanding"
        elif values>80 and values<=90:
            grade = "Exceeds Expectations"
        elif values>70 and values<=80:
            grade = "Acceptable"
        else:
            grade="Fail"
    else:
        print("we are sorry your marks are either more than 100 or less than 0\ntry to run again and provide marks between 0 and 100")
    students_grades[student_name]=grade
for key in students_grades:
    print(key)
    print(students_grades[key])
    


