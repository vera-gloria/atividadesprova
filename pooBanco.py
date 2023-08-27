class ContaBancaria():
    def __init__(self, banco, agencia, numeroConta, saldoAtual):
        self.banco = banco
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.saldoAtual = saldoAtual
    def verificaSaldo(self):
        print(f"Banco: {self.banco} Conta:{self.numeroConta} Agência: {self.agencia} Saldo: {self.saldoAtual}")
    def deposito(self):
        print(f"Banco: {self.banco} Conta:{self.numeroConta} Agência: {self.agencia} Saldo Atual: {self.saldoAtual}")
        valorDeposito = float(input("Insira o valor do deposito: "))
        self.saldoAtual = self.saldoAtual + valorDeposito
        print(f"Seu novo saldo é: {self.saldoAtual}")
        return self.saldoAtual
    def saque(self):
        print(f"Banco: {self.banco} Conta:{self.numeroConta} Agência: {self.agencia} Saldo Atual: {self.saldoAtual}")
        valorSaque = float(input("Insira o valor do saque: "))
        self.saldoAtual = self.saldoAtual - valorSaque
        print(f"Seu novo saldo é: {self.saldoAtual}")

contaVera = ContaBancaria("Brasil", "3610-2","37.138-6", 10.00)
contaVera.deposito()
contaVera.saque()
contaVera.verificaSaldo()

    
