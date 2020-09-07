# Exercise 24

import random

students = ['Chandler', 'Phoebe', 'Rachel', 'Joey', 'Monica', 'Ross']

chosen_student = random.sample(students, 6)

c = 0
for c in range(0, 6):
    print(f'The random student chosen is:', c, '-', chosen_student[c])

