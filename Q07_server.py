'''
Escreva um programa cliente e servidor sobre UDP em Python que:
O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera
receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes
(ainda esperando 5s a resposta) antes de desistir.


O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de
memória há no servidor e envia a resposta ao cliente de volta.
'''

import socket
import psutil
import pickle

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 9991                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')

while True:

    (msg, cliente) = udp.recvfrom(1024)

    if msg.decode('ascii') == 'fim':
        break

    print(f"Enviando dados de memória para {cliente}, {msg.decode('ascii')}")
    resposta = []
    mem = psutil.virtual_memory()
    mem_total = mem.total
    resposta.append(mem_total)
    mem_used = mem.used
    resposta.append(mem_used)

    bytes_resp = pickle.dumps(resposta)
    udp.sendto(bytes_resp, cliente)

udp.close()
