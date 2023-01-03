# Desenvolvimento 18
# autor: Alex Barros
# Data: 02/01/2023

class numerocomplexo:
    def __init__(self):
          self.num1 = 0
          self.num2 = 0
          self.num3 = 0
    def soma(self):
          return self.num1 + self.num2 + self.num3
    def subtracao(self):
          return self.num1 - self.num2 - self.num3
    def multiplicacao(self):
          return self.num1 * self.num2 * self.num3
    def divisao(self):
          return self.num1 / self.num2 / self.num3

for n in range(1,4):
    print()
    r = int(input("digite a parte real do "+str(n)+"º"+" número: "))
    i = int(input("digite a parte imaginária do "+str(n)+"º"+" número: "))
    if n == 1:
        n1 = complex(r,i)
        print(str(n)+"º"+" número: ",n1)
    elif n == 2:
        n2 = complex(r,i)
        print(str(n)+"º"+" número: ",n2)
    else: n3 = complex(r,i); print(str(n)+"º"+" número: ",n3)

nc = numerocomplexo()
nc.num1 = n1
nc.num2 = n2
nc.num3 = n3
print()
print("Soma = ", nc.soma())
print("Subtração = ", nc.subtracao())
print("Multiplicação = ", nc.multiplicacao())
print("Divisão = ", nc.divisao())
print()
print("Parte real do primeiro número: ", nc.num1.real)
print("Parte img do primeiro número: ", nc.num1.imag)
print()
print("Parte real do segundo número: ", nc.num2.real)
print("Parte img do segundo número: ", nc.num2.imag)
print()
print("Parte real do terceiro número: ", nc.num3.real)
print("Parte img do terceiro número: ", nc.num3.imag)
