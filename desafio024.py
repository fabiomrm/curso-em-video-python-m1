#Programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome da cidade: ')).strip()
maiusc = cidade.capitalize()
a = maiusc.split()
b = 'Santo' in a[0]
c = str(b)
print(f'A cidade digitada é {cidade}. Ela começa com o nome "Santo"?')
print(c.replace('True', 'Sim'))
print(c.replace('False', 'Não'))









