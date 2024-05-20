import math
choice = "y"

print("Tip Calculator")

while choice == "y":
    meal = float(input("Cost of meal: "))

    print("\n15%")
    tip = round((meal * .15),2)
    total = round((tip + meal),2)
    print(f"tip amount : ${tip}")
    print(f"total amount: ${total}")
    print("\n20%")
    tip = round((meal * .2),2)
    total = round((tip + meal),2)
    print(f"tip amount : ${tip}")
    print(f"total amount: ${total}")
    print("\n25%")
    tip = round((meal * .25),2)
    total = round((tip + meal),2)    
    print(f"tip amount : ${tip}")
    print(f"total amount: ${total}")

    choice = input("Continue (y/n)? ").lower()