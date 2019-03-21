'''
Escreva um programa em Python que:
obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu
programa manipula suas informações;

imprima o nome do processo e seu PID;
imprima também o percentual de uso de CPU e de uso de memória.
'''

import psutil , pprint

lista_process =[]
try:
    for proc in psutil.process_iter():
        lista_process.append([proc.pid, proc.name()])

except Exception as e:
    print(f'Ao tentar capturar algum processo, o seguinte erro ocorreu: {e}')

print('LISTA PROCESSOS')
pprint.pprint(lista_process)
mem_virtual = psutil.virtual_memory()
mem_percent = mem_virtual.used / mem_virtual.total
print(f'A porcentagem de uso de CPU é : {psutil.cpu_percent()}%')
print(f'A porcentagem de uso de Ram é: {round(mem_percent*100,2)}% ')

