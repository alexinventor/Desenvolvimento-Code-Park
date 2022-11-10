# Desenvolvimento 11
# autor: Alex Barros
# Data: 10/11/2022

opcao = ""
num1 = 0
num2 = 0

while (opcao != 0):
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    print("Digite o número para a operação: ")
    opcao = int(input())
    if (opcao > 4):
        print("Essa opção não existe!")
        print()
        continue
    elif (opcao == 0):
        break
    else:
        print("Digite o primeiro número: ")
        num1 = int(input())
        print("Digite o segundo número: ")
        num2 = int(input())
    if (opcao == 1):
        operacao = num1 + num2
    elif (opcao == 2):
        operacao = num1 - num2
    elif (opcao == 3):
        operacao = num1 * num2
    elif (opcao == 4):
        operacao = num1 / num2

    res = operacao
    print("O resultado da operação é: " + str(res))
    print()