# import math
# def greet(name,surename):
#     print("hello")
#     if name=='shehzad':
#         print(f"Hey Shehzad {surename} how do you do?")
#     else:
#         print(f"Hey {name} {surename}how do you do?")
# greet("shehzad","Ahmad")
# def greet_with(name,location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
# greet_with(location="Mardan",name="Shehzad")
# def paint_calc(height, width, cover):
#     area_of_paint = height*width
#     number_of_cans = math.ceil((area_of_paint)/cover)
#     print(f"The number of cans required to paint area of {area_of_paint} is {number_of_cans}")
# test_h = int(input('enter the height of area you want to paint\n'))
# test_w = int(input("enter the width of area that you want to paint\n"))
# test_cover = int(input("enter the area covered by 1 can of paint\n"))
# paint_calc(height=test_h,width=test_w,cover=test_cover)
def prime_checker(number):
    is_prime = True
    for i in range(2,number-1):
        if number%i==0:
            is_prime=False
            # print(f"{number} is not a Prime Number")
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
            # print(f"{number} is a Prime Number")
n = int(input("Enter the number you want to check if it is a prime number or not\n"))
prime_checker(number=n) 