import socket
import pickle
import os
# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 9999))
    msg = os.getcwd()
    # Envia mensagem codificada em bytes ao servidor
    s.send(msg.encode('ascii'))


    msg2 = s.recv(10000)
    lista_arquivo= pickle.loads(msg2)

    print(f'Os arquivos encontrados em {msg} '
          f'\nsão : {lista_arquivo} ')
    # Fecha conexão com o servidor
    s.close()
except Exception as erro:
    print(str(erro))