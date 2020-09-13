#Programa que lê o nome completo de uma pessoa e mostra:
#1. O nome com todas MAIÚSCULAS
#2. O nome com todas minúsculas
#3. Quantas letras (sem considerar espaços)
#4. Quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')
#1.
print(nome.upper())
#2.
print(nome.lower())
#3.
nome2 = int(len(nome))
espaço = int(nome.count(' '))
print(f'Seu nome possui {nome2 - espaço} letras')
#4
dividido = nome.split()
print(f'Seu primeiro nome possui {len(dividido[0])} letras')





