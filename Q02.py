'''
Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows
bloco de notas (notepad) para abrir o arquivo.
'''

import subprocess

nome_do_arquivo = input('Digite o nome do arquivo e sua extensão (arquivo.txt) ')

subprocess.Popen(['notepad', nome_do_arquivo])