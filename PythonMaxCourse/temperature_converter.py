choice = "y"

while choice.lower() == "y":
    f = float(input("Enter Degrees in Fahrenheit "))
    c =  (f - 32) * (5 / 9)
    c_formated = "{:,.2f}".format(c)
    print(f"Degrees in celsius = {c_formated}")
    choice = input("Continue y/n?")
print("Goodbye")