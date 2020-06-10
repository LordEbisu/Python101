user = int(input("Enter value to count untill "))
for x in range (1, user+1):
    if x % 3 == 0 and x % 7 != 0:
        print("Fizz")
    elif x % 7 == 0 and x % 3 != 0:
        print("Buzz")
    elif x % 3 == 0 and x % 7 == 0:
        print("FizzBuzz")
    else:
        print(x)    