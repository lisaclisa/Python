ask = input("When are you travelling (Summer or Winter)?")
if ask == "Summer":
    location = input("Do you want to go to America or Asia?")
    if location == "America":
        print("The price is £1500.")
    elif location == "Asia":
        print("The price is £1700")
    else:
        print("Sorry, this place is not valid")
elif ask == "Winter":
    location = input("Do you want to go to America or Asia?")
    if location == "America":
        print("The price is £1800.")
    elif location == "Asia":
        print("The price is £1650")
    else:
        print("Sorry, this place is not valid")
else:
    print("Sorry, this place is not valid.")
    
    
