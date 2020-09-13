#Programa que pergunta o ano e diz se é bissexto ou não
import datetime
ano = str(input('Digite o ano: '))
ano2 = int(ano)
numano = int(ano[len(ano) -2:len(ano)])
if numano == 00:
    if ano2 % 400 == 0:
        print('Ano bissexto')
    else:
        print('Não é bissexto')
if numano != 00:
    if ano2 % 4 == 0:
        print('Ano bissexto')
    else:
        print('Não é bissexto')


