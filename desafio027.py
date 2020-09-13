#Programa que lê o nome completo e mostra o primeiro e o último nome
import emoji
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
primeironome = nome[0]
ultimonome = nome[len(nome) - 1]
print((emoji.emojize(f'Olá!:smiley:\nSeu primeiro nome é {primeironome}\nSeu último nome é {ultimonome}', use_aliases=True)))



