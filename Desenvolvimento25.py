#Desenvolvimento 25
#Autor: Alex Barros
#Data: 19/01/2023

def maius_minus():
    frase_do_dia = "A felicidade é uma conquista diária!"
    print(frase_do_dia.upper())
    tudo_minusculo = frase_do_dia.lower()
    print(tudo_minusculo)
maius_minus()

def prim_maius():
    endereco = input("\nDigite seu endereço:")
    print(endereco.capitalize())
prim_maius()

def cont_letra():
    texto = input("\nCopie e cole o texto aqui e dê enter:")
    letra = input("\nDigite a letra que você quer contar no texto e dê enter:")
    t = (f"{texto}")
    l = (f"{letra}")
    print(f"A quantidade de letra \"{letra}\" no texto é: ", t.count(l))
cont_letra()