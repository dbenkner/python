import random
choice = "y"

print("Welcome to Guessing Game!")

def guess_number(comp_choice):
    correct = False
    gusses = 1
    while correct == False:
        try:
            g = int(input("Please enter a number between 1 and 100: "))
            if g > 100 or g < 1:
                print("Please enter a number between 1 and 100!")
                continue
            if g == comp_choice:
                correct == True
                break
            elif g > comp_choice:
                print("Number is too high!")
            else:
                print("Number is too low")
            gusses = gusses + 1
        except(ValueError):
            print("Please enter a vald number")
    print(f"You got it in {gusses} tries.")
    if gusses <= 3:
        print("Great work! You are a mathemetical wizard")
    elif gusses <= 7:
        print("Not too bad! You've got some potential")
    else:
        print("What took you so long? Maybe you should take some lessons.")
def quit_app():
     while True:
        choice = input("Continue? (y/n): ").lower()
        if choice != "y" and choice != "n":
            print("Error! Entry must be 'y' or 'n'")
        else:
            return choice       


while choice == "y":
    rand_num = random.randint(1,100)
    guess_number(rand_num)
    choice = quit_app()

print("GoodBye!")
