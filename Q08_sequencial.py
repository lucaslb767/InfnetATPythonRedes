'''
Escreva 3 programas em Python que resolva o seguinte problema:
Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.

Para calcular o fatorial, utilize a seguinte função:

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

a)sequencialmente (sem concorrência);
b)usando o módulo threading com 4 threads;
c)usando o módulo multiprocessing com 4 processos.
'''

import random
import time


def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

def fatorial_lista(funcao, vetor_a, vetor_b):
    for n in vetor_a:
        vetor_b.append(funcao(n))

a =[]
n = 10000000
b = []
for i in range(0, n ):
    a.append(random.randint(2,10))

print('Vetor a',len(a))
tempo_inicial = time.time()

fatorial_lista(fatorial,a,b)
print('Vetor b',len(b))
tempo_final = time.time()
print(f'O tempo total de sequencial foi de: {tempo_final - tempo_inicial}')

