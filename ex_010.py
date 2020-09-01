# Exercise 10

tab = int(input("I want the multiplication table from the number: "))
print(f"Mutiplication table of: {tab} \n")
for c in range(0, 10):
  c += 1
  print(tab, "X", c, "=", tab * c)