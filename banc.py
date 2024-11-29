from collections import deque

class ContaBancaria:
    def __init__(self, numero, titular, saldo_inicial=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +{valor:.2f}")
            return f"Depósito de R${valor:.2f} realizado com sucesso!"
        return "Valor de depósito inválido."

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -{valor:.2f}")
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente ou valor inválido para saque."

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f"Transferência para {conta_destino.numero}: -{valor:.2f}")
            conta_destino.historico.append(f"Transferência de {self.numero}: +{valor:.2f}")
            return f"Transferência de R${valor:.2f} para a conta {conta_destino.numero} realizada com sucesso!"
        return "Saldo insuficiente ou valor inválido para transferência."

    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    def exibir_historico(self):
        return "\n".join(self.historico) if self.historico else "Sem transações registradas."


class SimuladorBanco:
    def __init__(self):
        self.contas = {}
        self.fila_atendimento = deque()

    def cadastrar_conta(self, numero, titular, saldo_inicial=0.0):
        if numero in self.contas:
            return "Conta já existente."
        self.contas[numero] = ContaBancaria(numero, titular, saldo_inicial)
        return f"Conta {numero} cadastrada com sucesso!"

    def consultar_conta(self, numero):
        conta = self.contas.get(numero)
        if conta:
            return f"Titular: {conta.titular}, Saldo: R${conta.saldo:.2f}"
        return "Conta não encontrada."

    def remover_conta(self, numero):
        if numero in self.contas:
            del self.contas[numero]
            return f"Conta {numero} removida com sucesso!"
        return "Conta não encontrada."

    def adicionar_cliente_fila(self, numero_conta, operacao, valor=0, conta_destino=None):
        if numero_conta not in self.contas:
            return "Conta não encontrada na fila."
        self.fila_atendimento.append((numero_conta, operacao, valor, conta_destino))
        return f"Cliente da conta {numero_conta} adicionado à fila para {operacao}."

    def processar_fila(self):
        if not self.fila_atendimento:
            return "Nenhum cliente na fila de atendimento."
        numero_conta, operacao, valor, conta_destino = self.fila_atendimento.popleft()
        conta = self.contas[numero_conta]

        if operacao == "depositar":
            return conta.depositar(valor)
        elif operacao == "sacar":
            return conta.sacar(valor)
        elif operacao == "transferir" and conta_destino in self.contas:
            return conta.transferir(valor, self.contas[conta_destino])
        elif operacao == "consultar_saldo":
            return conta.consultar_saldo()
        return "Operação inválida ou dados incorretos."


# Exemplo de uso:
if __name__ == "__main__":
    banco = SimuladorBanco()

    # Cadastro de contas
    print(banco.cadastrar_conta(1, "Alice", 1000))
    print(banco.cadastrar_conta(2, "Bob", 500))

    # Operações diretas
    print(banco.contas[1].depositar(200))
    print(banco.contas[1].sacar(150))
    print(banco.contas[1].transferir(300, banco.contas[2]))
    print(banco.contas[1].exibir_historico())

    # Simulação de fila
    print(banco.adicionar_cliente_fila(1, "sacar", 50))
    print(banco.adicionar_cliente_fila(2, "consultar_saldo"))
    print(banco.processar_fila())
    print(banco.processar_fila())
