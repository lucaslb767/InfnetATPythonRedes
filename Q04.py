'''
Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo:
arquivo.txt

Bom dia
Voce pode falar agora?

Resultado na tela:

?aroga ralaf edop êcoV

aid moB
'''

texto = open('Q04.txt', 'r')

linhas = texto.readlines()

for n in range(len(linhas)-1,-1,-1):

    if '\\n' in linhas[n]:
        linhas[n].replace('\\n', '')

    print(linhas[n][::-1])

