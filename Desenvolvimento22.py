#Desenvolvimento 22
#Autor: Alex Barros
#Data: 13/01/2023

class Conta:

    total_contas = 0

    def __init__(self, saldo):
        self._saldo = saldo
        Conta.total_contas += 1

c1 = Conta(100.0)
c2 = Conta(200.0)
c3 = Conta(300.0)
print("c1=",c1.total_contas)
print("c2=",c2.total_contas)
print("c3=",c3.total_contas)