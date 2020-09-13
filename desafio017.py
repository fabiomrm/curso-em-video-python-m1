#Lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#Calcula e mostra o comprimento da hipotenusa
from math import hypot
catetooposto = float(input('Digite valor do cat opo: '))
catetoadjacente = float(input('Digite valor do cat adj: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
print(f'Hipotenusa: {hipotenusa}')
