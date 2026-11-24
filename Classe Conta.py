class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depositado R${valor:.2f}")
        else:
            print("Valor inválido!")

    def get_saldo(self):
        return self.__saldo

conta = Conta(100.00)
print(f"Saldo inicial: R${conta.get_saldo():.2f}")

conta.depositar(50.00)

print(f"Saldo final: R${conta.get_saldo():.2f}")