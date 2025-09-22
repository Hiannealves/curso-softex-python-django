class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("Ana", 100)
conta.sacar(50)   # sucesso
conta.sacar(100)  # insuficiente
