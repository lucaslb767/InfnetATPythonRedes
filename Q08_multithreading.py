import random
import time
import threading

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

def fatorial_lista(funcao, vetor_a, vetor_b):
    for n in vetor_a:
        vetor_b.append(funcao(n))

a =[]
n = 5000
b = []
for i in range(0, n ):
    a.append(random.randint(2,10))

tamanho = len(a)
print('Vetor a',tamanho)
tempo_inicial = time.time()

t0 = threading.Thread(target=fatorial_lista, args=(fatorial,a[0:int(tamanho/4)],b))
t0.start()
t1 = threading.Thread(target=fatorial_lista, args=(fatorial,a[int(tamanho/4): int(tamanho/2)],b))
t1.start()
t2 = threading.Thread(target=fatorial_lista, args=(fatorial,a[int(tamanho/2) : int(tamanho*(3/4))],b))
t2.start()
t3 = threading.Thread(target=fatorial_lista, args=(fatorial,a[int(tamanho*(3/4)) : int(tamanho)],b))
t3.start()

t0.join()
t1.join()
t2.join()
t3.join()

print('vetor b', len(b))
tempo_final = time.time()
print(f'O tempo total de multithreading foi de: {tempo_final - tempo_inicial}')