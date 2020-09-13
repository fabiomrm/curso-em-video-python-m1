#Programa que pergunta o salário do funcionário
#Acima de R$ 1.250,00 -> aumento de 10%
#Até R$ 1.250,00 -> aumento de 15%
salario = float(input('Qual o seu salário? '))
if salario <= 1250:
    reajuste = salario * 1.15
    print(f'Seu salário com aumento de 15% será de: R$ {reajuste:.2f}')
else:
    reajuste = salario * 1.10
    print(f'Seu salário com aumento de 10% será de: R$ {reajuste:.2f}')
