#Programa que lê 03 números e diz qual o maior e o menor
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if (n1 > n2 and n1 > n3):
    if n2 > n3:
        print(f'{n1} é o maior número e {n3} é o menor')
    else:
        print(f'{n1} é o maior número e {n2} é o menor')
if (n2 > n1 and n2 > n3):
    if n1 > n3:
        print(f'{n2} é o maior número e {n3} é o menor')
    else:
        print(f'{n2} é o maior número e {n1} é o menor')
if (n3 > n1 and n3 > n2):
    if n1 > n2:
        print(f'{n3} é o maior número e {n2} é o menor')
    else:
        print(f'{n3} é o maior número e {n1} é o menor')
if n1 == n2 == n3:
    print('Todos os números possuem o mesmo valor.')


