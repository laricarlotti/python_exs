# Exercise 04

user = input("Type something: ")

print(f"Has only spaces: {user.isspace()} \n",
      f"It's a number: {user.isnumeric()} \n",
      f"Is alphabetic: {user.isalpha()} \n",
      f"Is alphanumeric: {user.isalnum()} \n",
      f"It's uppercase: {user.isupper()} \n",
      f"It's lowercase: {user.islower()} \n",
      f"Is capitalized: {user.istitle()} \n")