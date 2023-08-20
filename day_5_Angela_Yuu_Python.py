students_score = input("Enter the Score of students\n").split()
for i in range(0,len(students_score)):
    students_score[i]=int(students_score[i])
print(students_score)
highest = 0
for i in students_score:
    if i>highest:
        highest=i
print(f"The highest score in list is {highest}")
