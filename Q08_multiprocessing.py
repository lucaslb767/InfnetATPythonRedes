# import multiprocessing, time, random
# def somaProc(q1, q2):
#     lista = q1.get()
#     b = []
#     for numero in lista:
#         fat = numero
#         for i in range(numero-1,1,-1):
#             fat = fat * i
#         b.append(fat)
#     q2.put(b)
#
# if __name__ == "__main__":
#     N = int(input("Entre com o tamanho do vetor: "))
#     # Captura tempo inicial
#     t_inicio = float(time.time())
#     # Gera lista com valores aleatórios
#     lista = []
#     for i in range(N):
#         lista.append(random.randint(2, 10))
#
#     NProc = 4 # Número de processos a ser criado
#
#     # Fila de entrada dos processos
#     q_entrada = multiprocessing.Queue()
#
#     # Fila de saída dos processos
#     q_saida = multiprocessing.Queue()
#     lista_proc = []
#     for i in range(NProc):
#         ini = i * int(N/NProc) # início do intervalo da lista
#         fim = (i + 1) * int(N/NProc) # fim do intervalo da lista
#         q_entrada.put(lista[ini:fim])
#         p = multiprocessing.Process(target=somaProc, args=(q_entrada,
#         q_saida))
#         p.start() # inicia processo
#         lista_proc.append(p) # guarda o processo
#
#     for p in lista_proc:
#         p.join()  # Espera os processos terminarem
#
#     vetor_b = []
#     for i in range(0, NProc):
#         vetor_b += q_saida.get()
#     # Captura tempo final
#     t_fim = float(time.time())
#     # Imprime o resultado e o tempo de execução
#     print("Vector A", lista)
#     print("Vector B:", vetor_b)
#     print("Tempo total:", t_fim - t_inicio)

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
        b += q.get()

    p0.join()
    p1.join()
    p2.join()
    p3.join()




    print('vetor b', b)
    tempo_final = time.time()
    print(f'O tempo total foi de: {tempo_final - tempo_inicial}')