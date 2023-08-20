print("Welcome to FizzBuzz Game")
for i in range(0,10000):
    if i%3==0 and i%4==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%4==0:
        print("Buzz")
    else:
        print(i)

    