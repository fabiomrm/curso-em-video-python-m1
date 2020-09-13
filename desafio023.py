#Programa que lê um número de 0 a 9999 e mostra cada dígito separado
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Seu número é {num} e ele possui \nUnidade: {u}\nDezena: {d}\nCentena:{c}\n Milhar: {m}')














