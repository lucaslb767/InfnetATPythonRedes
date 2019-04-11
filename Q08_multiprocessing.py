import random
import time
import multiprocessing

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

def fatorial_lista(funcao, vetor_a,q):

    vetor_b =[]
    for n in vetor_a:
        vetor_b.append(funcao(n))

    q.put(vetor_b)

    # print(queue.get())
    # print(len(queue.get()))

if __name__ == "__main__":

    a =[]
    n = 10000000
    b = []
    q = multiprocessing.Queue()
    for i in range(0, n ):
        a.append(random.randint(2,10))

    tamanho = len(a)
    print('Vetor a',tamanho)
    tempo_inicial = time.time()

    p0 = multiprocessing.Process(target=fatorial_lista, args=(fatorial,a[0:int(tamanho/4)],q))
    p0.start()
    p1 = multiprocessing.Process(target=fatorial_lista, args=(fatorial,a[int(tamanho/4): int(tamanho/2)],q))
    p1.start()
    p2 = multiprocessing.Process(target=fatorial_lista, args=(fatorial,a[int(tamanho/2) : int(tamanho*(3/4))],q))
    p2.start()
    p3 = multiprocessing.Process(target=fatorial_lista, args=(fatorial,a[int(tamanho*(3/4)) : int(tamanho)],q))
    p3.start()

    while len(a) != len(b):
        while q.empty() is False:
            b += q.get()

    p0.join()
    p1.join()
    p2.join()
    p3.join()


    print('vetor b', len(b))
    tempo_final = time.time()
    print(f'O tempo total de multiprocessing foi de: {tempo_final - tempo_inicial}')