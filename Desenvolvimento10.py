# Desenvolvimento 10
# autor: Alex Barros
# Data: 09/11/2022

def calculadora(num1, num2, operacao):
    if (operacao == 1): return num1 + num2
    elif (operacao == 2): return num1 - num2
    elif (operacao == 3):return num1 * num2
    elif (operacao == 4):return num1 / num2
    else: return 0
num1 = 9
num2 = 6
operacao = 4

resultado = calculadora(num1, num2, operacao)
print(resultado)
