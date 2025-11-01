import random 

numero = random.randrange(1,10)
escolha = int(input('escolha um numero de 1 a 10 -->'))

if numero == escolha:
    print('voce ganhou o jogo🎉🥳')
else: 
    print('errou feio!!❌')

