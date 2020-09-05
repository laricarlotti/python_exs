# Exercise 22

from math import sin, cos, tan, radians
angle = float(input("Type an angle: "))
sin = sin(angle)
cos = cos(angle)
tan = tan(angle)

print(f"The sine of your angle {angle.__trunc__()}º is {round(sin, 2)}. It's cosine is {round(cos, 2)}, and tangent {round(tan, 2)}")
