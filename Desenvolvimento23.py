#Desenvolvimento 23
#Autor: Alex Barros
#Data: 14/01/2023

class Conta:
    def __init__(self):
        self.titular = "João"
        self.saldo = 100.0
        self.deposito = 0

    def get_titular(self):
        return self.titular

    def set_titular(self, novo_titular):
        self.titular = novo_titular

    def get_deposito(self):
        return self.deposito

    def set_deposito(self, novo_deposito):
        if (novo_deposito >= 0):
            self.deposito = novo_deposito
        else:
            print("Depósito invalido!")

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, total_saldo):
        self.saldo = total_saldo

correntista = Conta()

print("Nome do titular:", correntista.get_titular())
print("Seu saldo é R$", correntista.get_saldo())

novo_deposito = int(input("Digite o valor depositado:"))
correntista.set_deposito(novo_deposito)
total_saldo = correntista.get_deposito() + correntista.get_saldo()
correntista.set_saldo(total_saldo)

print("Seu novo saldo é R$", correntista.get_saldo())