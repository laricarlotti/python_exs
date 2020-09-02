# Exercise 17

from math import sqrt

num = int(input("Type a number: "))
square = sqrt(num)
print(f"The square root of {num} is {square.__trunc__()}")