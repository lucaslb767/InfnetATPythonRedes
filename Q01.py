'''
Escreva um programa em Python que:
obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
imprima o nome do processo e seu PID;
imprima também o percentual de uso de CPU e de uso de memória.
'''

import os
import psutil
import pprint

print(psutil.pids())



process_names = []
process_pid = psutil.pids()
for pid in process_pid:

    name = psutil.Process(pid)
    process_names.append(name)

print(process_names)
