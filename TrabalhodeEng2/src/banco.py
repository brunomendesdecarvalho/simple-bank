class Conta:
    def __init__(self, conta_num, saldo_inicial=0):
        self.conta_num = conta_num
        self.balance = saldo_inicial

    def deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.balance += valor

    def saque(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if self.balance < valor:
            raise ValueError("Saldo insuficiente para o saque.")
        self.balance -= valor

    def transferencia(self, conta_destino, valor):
        if conta_destino is None:
            raise ValueError("Conta de destino inexistente.")
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        if self.balance < valor:
            raise ValueError("Saldo insuficiente para a transferência.")
        self.balance -= valor
        conta_destino.balance += valor
