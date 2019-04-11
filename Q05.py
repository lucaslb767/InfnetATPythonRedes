'''
Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:

a.txt

1 15 -42 33 -7 -2 39 8

b.txt

19 56 -43 23 -7 -11 33 21 61 9

Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela. Isto é, o primeiro elemento de a.txt deve ser
somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt,
e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.
'''
import os

if (os.path.isfile('a.txt')) and (os.path.isfile('b.txt')):
    def soma_arquivos(arquivo_a, arquivo_b):

        a = open(arquivo_a, 'r')
        b = open(arquivo_b, 'r')

        lista_a = list(map(int,a.read().split(' ')))
        print('lista a',lista_a)
        lista_b = list(map(int,b.read().split(' ')))
        print('lista b',lista_b)
        resultado =[]

        if len(lista_a) == len(lista_b):
            for number in range(0, len(lista_a)):
                resultado.append(lista_a[number] + lista_b[number])

        elif len(lista_a) > len(lista_b):
            for number in range(0, len(lista_b)):
                resultado.append(lista_a[number] + lista_b[number])

            for number in range(len(lista_b), len(lista_a)):
                resultado.append(lista_a[number]+0)

        elif len(lista_a) < len(lista_b):
            for number in range(0, len(lista_a)):
                resultado.append(lista_a[number] + lista_b[number])

            for number in range(len(lista_a) , len(lista_b)):
                resultado.append(lista_b[number] + 0)

        return print(f' A soma de elemento por elemento dos arquivos é {resultado}')
    a = 'a.txt'
    b = 'b.txt'

    soma_arquivos(a,b)

else:
    print('Verifique se os arquivos "a.txt" e "b.txt" existem e contem números')

