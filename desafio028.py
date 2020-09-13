#Programa em que o computador pensa em um número inteiro entre 0 e 5 ,
#pede para o usuário tentar descobrir e informa se ele venceu ou perdeu o jogo.
from random import randint
import emoji
print('====BEM VINDO AO JOGO DA ADIVINHAÇÃO!====')
num = randint(0, 5)
chute = int(input('Digite um número inteiro entre 0 e 5: '))
if num == chute:
    print((emoji.emojize('Parabéns! Você venceu!:clap:', use_aliases=True)))
else:
    print((emoji.emojize('Perdeu! Tente novamente!:cry:', use_aliases=True)))


