# Desenvolvimento 13
# autor: Alex Barros
# Data: 14/11/2022

import enum

votacao_cand_x = 0
votacao_cand_y = 0
votacao_cand_z = 0
votacao_brancos = 0
votacao_nulos = 0
fim_eleicao = False

class Eleicao(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0

while(fim_eleicao == False):
    print()
    print('********************************')
    print('********* ELEIÇÃO 2022 *********')
    print('********************************')
    print()
    print('889 - candidato_X')
    print('847 - candidato_Y')
    print('515 - candidato_Z')
    print('  0 - Voto em Branco')
    print()
    print('Digita o número do candidato: ')
    try:
        voto = int(input())
        print()
        print('Deseja finalizar a votação? s-sim ou n-não: ')
        finalizar = input()
        if (finalizar == 'n'):
            voto = 0
            continue
        else:
            print('********************************')
            print('************* FIM **************')
            print('********************************')
            if(voto == Eleicao.candidato_X.value):
                votacao_cand_x += 1
            elif(voto == Eleicao.candidato_Y.value):
                votacao_cand_y += 1
            elif(voto == Eleicao.candidato_Z.value):
                votacao_cand_z += 1
            elif(voto == Eleicao.branco.value):
                votacao_brancos += 1
            else:
                votacao_nulos += 1
    except:
        print('Caracter inválido!')
        print('Vote novamente!')
        continue
    print()
    print('Mesário, próximo eleitor? s-sim, n-não: ')
    proximo_eleitor = input()
    if(proximo_eleitor == 's'):
        continue
    elif(votacao_cand_x > votacao_cand_y) and (votacao_cand_x > votacao_cand_z):
        vencedor = Eleicao.candidato_X.name
    elif(votacao_cand_y > votacao_cand_x) and (votacao_cand_y > votacao_cand_z):
        vencedor = Eleicao.candidato_Y.name
    elif(votacao_cand_z > votacao_cand_x) and (votacao_cand_z > votacao_cand_y):
        vencedor = Eleicao.candidato_Z.name
    elif(votacao_cand_x == votacao_cand_y) and (votacao_cand_x != votacao_cand_z):
        vencedor = 'Empate entre: ' + Eleicao.candidato_X.name + ' e ' + Eleicao.candidato_Y.name
    elif (votacao_cand_x == votacao_cand_z) and (votacao_cand_x != votacao_cand_y):
        vencedor = 'Empate entre: ' + Eleicao.candidato_X.name + ' e ' + Eleicao.candidato_Z.name
    elif(votacao_cand_y == votacao_cand_z) and (votacao_cand_y != votacao_cand_x):
        vencedor = 'Empate entre: ' + Eleicao.candidato_Y.name + ' e ' + Eleicao.candidato_Z.name
    else:
        vencedor = 'Empate entre: ' + Eleicao.candidato_X.name + ', ' + Eleicao.candidato_Y.name + ' e ' + Eleicao.candidato_Z.name
    print('********************************')
    print('*****RESULTADO DA ELEIÇÃO*******')
    print('********************************')
    print()
    print('Candidato X: ' + str(votacao_cand_x) + ' votos.')
    print('Candidato Y: ' + str(votacao_cand_y) + ' votos.')
    print('Candidato Z: ' + str(votacao_cand_z) + ' votos.')
    print('Votos em Branco: ' + str(votacao_brancos))
    print('Votos nulos: ' + str(votacao_nulos))
    print()
    print('********************************')
    print('VENCEDOR: ' + vencedor)
    print('********************************')
    fim_eleicao = True

