'''x = 2
if x > 10:
    print('X é maior que 10')
else:
    print('X não é maior que 10')'''
'''from time import sleep

lista = [1, 2, 3, 4, 678, 'fera', 'Jc']'''

'''for i in range(10 + 1):
    sleep(0.5)
    print('Rodada ', i)'''

'''for i in lista:
    print('Valor', i)
    sleep(0.5)'''

'''def soma(num1, num2):
    resul = num1 + num2
    print('A soma é: ', resul)
soma(7, 1)'''

'''import random

def gerarJogo():
    for c in range(6):
        print('Número', random.randint(0, 60))

gerarJogo()'''

import random

def gerarJogo():
    sorteados = []
    num = random.randint(0, 50)
    sorteados.append(num)
    num = random.randint(0, 50)
    for c in range(5):
        while num in sorteados:
            num = random.randint(0, 60)
        sorteados.append(num)
    print('NÚMEROS DA SORTE', sorteados)

gerarJogo()