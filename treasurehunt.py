# row1 = [1, 1, 1]
# row2 = [2, 2, 2]
# row3 = [3, 3, 3]
# complete = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# value = input("enter the value you want to put in the box\n")
# coordinates = input(f'enter the coordinates where you want to put the {value}\n')
# horizontal = int(coordinates[0])
# vertical = int(coordinates[1])
# selected_row = complete[vertical-1]
# selected_row[horizontal-1]= value
# print(f"{row1}\n{row2}\n{row3}")
# complete[1][1] = 9
# print(complete)
a1 = [5,4,3,5,4,3]
a2 = [3,2,1,3,2,1]
a3 = [9,8,7,9,8,7]
compli=[a1,a2,a3]
print(f"{a1}\n{a2}\n{a3}\n")
val = int(input("enter the integer you want to put in the box\n"))
coordi = input(f"enter the coordinates you want to put the value {val} in ")
hori = int(coordi[0])
verti = int(coordi[1])
compli[verti-1][hori-1] = val
print(f"{a1}\n{a2}\n{a3}\n")