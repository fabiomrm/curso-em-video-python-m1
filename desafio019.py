#Sorteia entre 04 pessoas e escreve o nome da sorteada
import random
a1 = input('Estudante 01: ')
a2 = input('Estudante 02: ')
a3 = input('Estudante 03: ')
a4 = input('Estudante 04: ')
alunos = (a1, a2, a3, a4)
print(f'Estudante sorteade foi: {random.sample(alunos, 1)}')