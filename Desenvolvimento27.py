#Desenvolvimento 27
#Autor: Alex Barros
#Data: 22/01/2023

def quant_palavras():
    try:
        arquivo = open('palavras.txt', 'r')
    except IOError:
        print('Não foi possível abrir o arquivo')
    else:
        print('O arquivo tem {} palavras'.format(len(arquivo.readlines())))
        arquivo.close()
quant_palavras()