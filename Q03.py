'''
Escreva um programa em Python que:
gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam
em disco. Obtenha o nome do diretório do usuário.


Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
gere um arquivo texto com os valores desta estrutura ordenados.
'''

import os
import pprint

def arquivos_diretorio(diretorio):

    arquivos = []

    total_ocupado = []

    if diretorio == '':

        for arquivo in os.listdir(os.getcwd()):

            try:
                if os.path.isfile(arquivo):
                    arquivos.append(arquivo)
                    total_ocupado.append(os.stat(arquivo).st_size)

                else:
                    print(arquivo, 'não é considerado um arquivo')
            except Exception as e:
                print(e)

    else:
        for arquivo in os.listdir(diretorio):

            try:
                if os.path.isfile(str(diretorio+'\\'+arquivo)):
                    arquivos.append(arquivo)
                    total_ocupado.append(os.stat(diretorio+'\\'+arquivo).st_size)

                else:
                    print(arquivo, 'não é considerado um arquivo')
            except Exception as e:
                print(e)

    dic_organizado = dict(zip(arquivos, total_ocupado))


    total_ocupado_sorted = sorted(total_ocupado, reverse=True)

    pares_finais = []

    for tamanho in total_ocupado_sorted:
        for arquivo_dic, size in dic_organizado.items():
            if size == tamanho:
                pares_finais.append([arquivo_dic, size])

    print('Arquivos Organizados em Ordem descrescente')
    pprint.pprint(pares_finais)

    texto = open('Q03.txt','w')

    for pares in pares_finais:
        texto.writelines(f'\nO arquivo {pares[0]} tem tamanho de {pares[1]} bytes')
    texto.close()


dir = input('Digite o path desejado ou deixe em branco para utilizar o diretorio onde se encontra: ')

if os.path.exists(dir) or dir == '':
    arquivos_diretorio(dir)

else:
    print('Diretorio não encontrado, por favor digite o caminho completo (Ex: C:\\Users\\Lucas\\Downloads )')