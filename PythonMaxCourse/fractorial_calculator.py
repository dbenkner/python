
choice = "y"
print(f"Welcome to the factorial calculator")

while choice.lower() == "y":
    num = int(input("Enter an integer that's greater than 0 and less than 10: "))
    if num > 0:
        ans = 1
        for r in range(1,num+1):
            ans *= r
        print(f"The factorial of {num} is {ans}")
    else:
        print("Please enter a valid number!")
    choice = input("Continue? (y/n): ")