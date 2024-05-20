choice = "y"
while choice != "n":
    grade =  int(input("\nPlease enter a grade score: "))
    if(grade >= 88):
        print("\nThe Student got an A")
    elif(grade >= 80):
        print("\nThe Student got a B")
    elif(grade >= 67):
        print("\nThe Student got a C")
    elif(grade >= 60):
        print("\nThe Student got a D")
    elif(grade >= 0):
        print("\nThe student got an F")
    else:
        print("\nGrade must be greater than 0!")
    choice = input("\nEnter another grade? (y/n)").lower
print("GoodBye")