user = 0
while True:
    user = int(input("Farenheit to celcious 1    farenheit to kelvin 2   press 3 to end  "))
    if user == 1:
        value = float(input("value for farenheit to celcious  "))
        celcious = (5/9)*(value - 32)
        print(f"{value} farenheit equals to {celcious} celcious")
    elif user == 2:
        value = float(input("value for farenheit to kelvin  "))
        kelvin = (5/9)*(value - 32)+ 273.15 
        print(f"{value} farenheit equals to {kelvin} kelvin ")   
    elif user == 3:
        print("End program")
        break
    else:
        print("Invalid input, see instructions")