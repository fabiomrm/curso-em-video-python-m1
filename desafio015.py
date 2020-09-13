carrodiaria = float(input('Digite o valor da diária do carro: R$ '))
carrokm = float (input('Digite o valor da diária por km andado: R$ '))
distancia = float(input('KM percorrido:'))
dias = int(input('Quantidade de dias alugados:'))
custo = float(carrodiaria * dias + carrokm*distancia)
print(f'Valor a pagar: R$ {custo:.2f}')



