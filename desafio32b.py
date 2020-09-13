#Ano bissexto ou não (outra maneira de fazer
import datetime
ano = int(input('Qual ano deseja analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
    print('O ano é bissexto.')
else:
    print('Não é bissexto.')
