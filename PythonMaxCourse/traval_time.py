import math
choice = "y"

while choice == "y":
    miles = float(input("Enter Miles: "))
    mph = float(input("Enter Miles per hour:"))
    print("\nEstimated time traveled")
    time_traveled = miles /mph
    print(f"{time_traveled}")
    hours = math.floor(time_traveled)
    minutes_float = time_traveled - hours
    minutes = math.floor(minutes_float * 60)
    print(f"{hours} Hours and {minutes} Minutes")
    choice  = input("Contiue? y/n  ")
print("GoodBye")