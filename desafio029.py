#Programa que lê a velocidade de um carro
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7,00/km acima do limite.
velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    valor = float((velocidade - 80)*7)
    print(f'Você foi multado!\n O valor da multa será de: R$ {valor:.2f}\nDirija com mais cautela!')
else:
    print('Tudo certo! Siga conduzindo com cuidado.')