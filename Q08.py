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