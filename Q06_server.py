'''
Escreva um programa cliente e servidor sobre TCP em Python em que:
O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
'''

import socket
import os
import pickle

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtém o nome da máquina
host = socket.gethostname()
porta = 9999
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
while True:
  # Aceita alguma conexão
  (socket_cliente,addr) = socket_servidor.accept()
  print("Conectado a:", str(addr))
  path = socket_cliente.recv(1024)
  # Decodifica mensagem em ASCII
  print (path.decode('ascii'))

  arquivos =[]
  for arquivo in os.listdir(path):

    try:
      if os.path.isfile(arquivo):
        arquivos.append(arquivo)

      else:
        print(arquivo, 'não é considerado um arquivo')
    except Exception as e:
      print(e)
  lista_arquivo = pickle.dumps(arquivos)

  socket_cliente.send(lista_arquivo)
  socket_cliente.close()