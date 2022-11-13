# Desenvolvimento 12
# autor: Alex Barros
# Data: 13/11/2022

print()
print("Digite o seu nome completo: ")
nome = input()
anoCorreto = False
while (anoCorreto == False):
    print("Digite o ano do seu nascimento: ")
    try:
        ano = int(input())
        if (ano >= 1922) and (ano <= 2021):
            anoCorreto = True
        else:
            print("O ano que você digitou está fora do período entre 1922 e 2021!")
    except:
        print("Caracter inválido!")

idade = 2022 - ano
print("Nome Completo: " + nome)
print("Você completou ou completará em 2022: " + str(idade) + " anos")