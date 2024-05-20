choice = "y"
print("Welcome to the squares and cubes!")
while choice == "y":
    num = int(input("Enter an integer: "))
    for n in range(1,num+1):
        square = n * n
        cube = n * n * n
        print(f"{n} {square} {cube}")
    choice = input("Continue? (y/n): ").lower()
