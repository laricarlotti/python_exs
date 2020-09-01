# Exercise 12

wall_width = float(input("Type the width of your wall: "))
wall_height= float(input("Type the height of your wall: "))

area = wall_width * wall_height
ink = area / 2

print(f"The area you want to paint has {area}m2. Therefore, you'll need {ink}L of ink :)")