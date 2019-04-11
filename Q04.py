'''
Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo:
arquivo.txt

Bom dia
Voce pode falar agora?

Resultado na tela:

?aroga ralaf edop êcoV

aid moB
'''

import os
if os.path.isfile('Q04.txt'):
    texto = open('Q04.txt', 'r')

    linhas = texto.readlines()
    print(linhas)
    for n in range(len(linhas)-1,-1,-1):

        if '\\n' in linhas[n]:
            linhas[n].replace('\\n', '')

        print(linhas[n][::-1])

else:
    print('Crie um arquivo chamado "Q04.txt" com algum texto dentro')

