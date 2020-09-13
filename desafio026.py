#Programa que lê uma frase e mostra:
#1. Quantas vezes aparece a letra a;
#2. Em que posição ela aparece pela primeira vez;
#3. Em que posição ela aparece pela última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
#1.
letraa = frase.count('A')
print(f'A sua frase possui {letraa} letras a')
#2.
primeiroa = frase.find('A')
print(f'A primeira letra a aparece na posição {primeiroa}')
#3.
ultimoa = frase.rfind('A')
print(f'A última letra a aparece na posição {ultimoa}')









