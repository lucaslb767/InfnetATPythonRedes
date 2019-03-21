'''
Escreva um programa cliente e servidor sobre UDP em Python que:
O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera
receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes
(ainda esperando 5s a resposta) antes de desistir.


O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de
memória há no servidor e envia a resposta ao cliente de volta.
'''