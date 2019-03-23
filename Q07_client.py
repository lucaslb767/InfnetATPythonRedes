import socket, time, pickle



# Cria o socket
udp= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9991
dest = (host, port)
try:
    # Tenta se conectar ao servidor
    # udp.connect((socket.gethostname(), 9999))
    msg = input('Digite qualquer comando para receber informações de memória ou digite fim para terminar ')

    if msg != 'fim':
        for i in range(5):
            # Envia mensagem vazia apenas para indicar a requisição
            udp.sendto(msg.encode('ascii'), dest)
            bytes = udp.recv(1024)
            # Converte os bytes para lista
            lista = pickle.loads(bytes)
            print(f'O total de memória é de: {lista[0]} bytes')
            print(f'A quantidade de memória usada é de: {lista[1]} bytes')
            time.sleep(5)
        msg = 'fim'
        udp.sendto(msg.encode('ascii'), dest)
    else:
        udp.sendto(msg.encode('ascii'), dest)
        udp.close()
except Exception as erro:
  print('OLHA O ERRO',str(erro))

# Fecha o socket
udp.close()

input("Pressione qualquer tecla para sair...")