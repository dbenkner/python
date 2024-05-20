
#max/min


print("max and min...")
max_nbr = max(5, 25, 30) #30
print(f"max_nbr = {max_nbr}")
min_nbr = min(200, 75, 150) # 75
print(f"min_nbr = {min_nbr}")

total = sum([5, 200, 75, 22]) # Sum can handle an array of numbers
print(f"sum = {total}")

#rounding numbers
print("\n Rounding")
round_nbr = round(9.35782)

print(f"{round_nbr}")
nbr_1 = 9.55725
# round nbr_1 to 3 decimal places
round_nbr = round(nbr_1, 3)

print(f"rounded_nbr = {round_nbr}")

print("\n ceil and floor examples")
# from math import ceil, floor
import math
ceil_nbr = math.ceil(5.5)
floor_nbr = math.floor(5.5)

print(f"Ceiling is {ceil_nbr} Floor is {floor_nbr}")


print("\n Random numbers")
import random
die_roll = random.randint(1,6)

print(f"The die roll is {die_roll}")

print("\n String formating!!")
price = 20000
price_currency = "${:,.2f}".format(price)
print(f"The total is {price_currency}")
grade = .9995
grade_pct_1 = format(grade, '%')
print(f"Grade percentage is {grade_pct_1}")
grade_pct_2 = "{:.2%}".format(grade)
print(f"Grade percentage is {grade_pct_2}")