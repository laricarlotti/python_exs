# Exercise 16

km_traveled = float(input("How many kilometers did you travel with the car? "))
days_rented = int(input("For how many days did you rent it? "))

owned = (60 * days_rented) + (0.15 * km_traveled)

print(f"The total cost for the trip is R${owned}")
