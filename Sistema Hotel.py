quartos = ['', 'simples', 'duplo', 'luxo']
valores = [0,100,150,250]
quantidade_pessoas = int(input('Pessoas: '))

if quantidade_pessoas == 1:

    nome = input(' nome: ')
    idade = input('Idade :')

    escolha = int(input('''
1 - Simples: R$ 100,00 por dia.
2 - Duplo: R$ 150,00 por dia.
3 - Luxo: R$ 250,00 por dia.
'''))

    q_dias = int(input(' quantidade de dias:'))
    print('hospedagem:')
    print('Quantidade de dias', q_dias)
    print('quarto', quartos[escolha])
    total = q_dias * valores[escolha]

    print('R$', total)

elif quantidade_pessoas == 2:

    nome = input(' nome: ') 
    idade = input('Idade :')

    nome = input(' nome: ') 
    idade = input('Idade :')


    escolha = int(input('''
1 - Simples: R$ 100,00 por dia.
2 - Duplo: R$ 150,00 por dia.
3 - Luxo: R$ 250,00 por dia.
'''))
    
    q_dias = int(input(' quantidade de dias:'))
    print('hospedagem:')
    print('Quantidade de dias', q_dias)
    print('quarto', quartos[escolha])
    total = q_dias * valores[escolha]

    print('R$', total)

    escolha = int(input('''
1 - Simples: R$ 100,00 por dia.
2 - Duplo: R$ 150,00 por dia.
3 - Luxo: R$ 250,00 por dia.
'''))

    q_dias_2 = int(input(' quantidade de dias:'))
    print('hospedagem:')
    print('Quantidade de dias', q_dias_2)
    print('quarto', quartos[escolha])
    total2 = q_dias_2 * valores[escolha]

    print('R$', total2)
elif quantidade_pessoas == 3:


    nome = input(' nome: ') 
    idade = input('Idade :')

    nome = input(' nome: ') 
    idade = input('Idade :')


    nome = input(' nome: ') 
    idade = input('Idade :')


    escolha = int(input('''
1 - Simples: R$ 100,00 por dia.
2 - Duplo: R$ 150,00 por dia.
3 - Luxo: R$ 250,00 por dia.
'''))

    q_dias = int(input(' quantidade de dias:'))
    print('hospedagem:')
    print('Quantidade de dias', q_dias)
    print('quarto', quartos[escolha])
    total = q_dias * valores[escolha]

    print('R$', total)


    escolha = int(input('''
1 - Simples: R$ 100,00 por dia.
2 - Duplo: R$ 150,00 por dia.
3 - Luxo: R$ 250,00 por dia.
'''))

    q_dias_2 = int(input(' quantidade de dias:'))
    print('hospedagem:')
    print('Quantidade de dias', q_dias_2)
    print('quarto', quartos[escolha])
    total2 = q_dias_2 * valores[escolha]

    print('R$', total)


    escolha = int(input('''
1 - Simples: R$ 100,00 por dia.
2 - Duplo: R$ 150,00 por dia.
3 - Luxo: R$ 250,00 por dia.
'''))

    q_dias_3 = int(input(' quantidade de dias:'))
    print('hospedagem:')
    print('Quantidade de dias', q_dias_3)
    print('quarto', quartos[escolha])
    total3 = q_dias_2 * valores[escolha]

    print('R$', total3)
else:

    print('Digite alçgo valido')    
