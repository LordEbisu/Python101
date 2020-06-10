totalPrice = 0
while True:
    user = int(input("select product for purchase  1.McWopper  2.crispy McFish 3.Fries menue 4.Soda menue 5.Happy meal  6.Family deal 7.End order  8.Close program  "))
    if user == 1:
        print("     McWopper")
        totalPrice += 6.89
    elif user == 2:
        print("     Crispy Mcfish")
        totalPrice += 4.99
    elif user == 3: 
        userFries =int(input("Select fries size "))
        if userFries == 1:
            print("  Small fries") 
            totalPrice += 0.99
        elif userFries == 2:
            print("  Medium fries")
            totalPrice += 1.99
        elif userFries == 3:
            print("  Large fries")
            totalPrice += 2.99 
        else:
            print("Choose between 1 - 3 for fries.Now start from the beginning ")       
    elif user == 4:
        userSoda =int(input("Select soda size "))
        if userSoda == 1:
            print("  Small soda") 
            totalPrice += 0.50
        elif userSoda == 2:
            print("  Medium soda")
            totalPrice += 1.50
        elif userSoda == 3:
            print("  Large soda")
            totalPrice += 2.50
        else:
            print("Choose between 1 - 3 for soda.Now start from the beginning ")   
    elif user == 5:
        print("     Happy meal")
        totalPrice += 6.99
    elif user == 6:
        print("     Family deal") 
        totalPrice += 19.99
    elif user == 7:
       total = (0.08875*totalPrice)+totalPrice
       print("thanks For stopping By")
       print(f"Purchase price $ {totalPrice} ")
       print(f"the total (including tax) $ {total}") 
    elif user == 8:
        break   
    else:
        print("Please refer to the instruction.")       