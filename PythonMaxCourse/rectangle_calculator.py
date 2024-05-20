print("Welcome to the area and perimeter calculator")

choice = "y"

while choice == "y":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    perimeter = (2 * width) + (2 * length)
    print(f"\nArea: {area}")
    print(f"\nperimeter: {perimeter}")
    choice = input("\nContinue (y/n)").lower
print("\nGoodbye")