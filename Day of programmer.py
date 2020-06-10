user =int(input("Input the year to find exact date  "))
if user>= 1700 and user <= 2700:
    if user % 4 == 0:
        print("This year progeamming day is 09.12 (leap year)")
    elif user % 400 == 0:
        print("This year progeamming day is 09.12 (leap year)")
    elif user % 100 == 0:
        print("this year programing day is 09.13 (Not Leap year)")
    elif user == 1918:
        print("This year  the day should be 09.26 (special case)")       
else :
    print("Invalid year, pick between 1700 and 2700")        