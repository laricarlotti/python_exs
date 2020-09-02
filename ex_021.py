# Exercise 21

from math import hypot

first_cat = int(input("Adjacent cathetus value: "))
second_cat = int(input("Opposite cathetus value: "))
hypo = hypot(first_cat, second_cat)
print(f"The hypotenuse is: {hypo.__trunc__()}")