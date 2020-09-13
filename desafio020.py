#Sorteia a ordem entre 04 pessoas
import random
a1 = input('Estudante 01: ')
a2 = input('Estudante 02: ')
a3 = input('Estudante 03: ')
a4 = input('Estudante 04: ')
estudantes = (a1, a2, a3, a4)
print(f'A ordem de apresentação será {random.sample(estudantes, 4)}')


