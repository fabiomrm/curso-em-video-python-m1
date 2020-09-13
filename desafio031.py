#Programa que pergunta a distância da viagem e calcula preço
#R$ 0,50 por km para viagens até 200 km
#R$ 0,45 por km para viagens mais longas
print('####VALOR DA PASSAGEM####')
dist = int(input('Qual a distância da sua viagem? '))
if dist <= 200:
    preço1 = dist * 0.50
    print(f'O valor da sua passagem será: R$ {preço1:.2f}')
else:
    preço2 = dist * 0.45
    print(f'O valor da sua passagem será: R$ {preço2:.2f}')
print('BOA VIAGEM!')
