class ContaCorrente:  # CRIAÇÃO DA CLASSE CONTA CORRENTE

    def __init__(self, nome, cpf, saldo=0):  # ATRIBUTOS DE CLASSE
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def consultar_saldo(self):  # METODO PARA CONSULTAR SALDO
        print(f'O saldo atual da conta inscrita sob o CPF:{self.cpf} é de R${self.saldo:,.2f}')
        return f'o seu saldo atual é de R${self.saldo:,.2f}'

    def depositar(self, valor):  # METODO PARA DEPOSITAR DINHEIRO
        self.saldo += valor

    def sacar(self, valor):  # METODO PARA SACAR DINHEIRO
        if self.saldo <= 0:
            print(f'Saldo insuficiente, {self.consultar_saldo()}')
        else:
            self.saldo -= valor

    def transferencia(self, valor, outra_conta):  # METODO PARA TRANSFERIR DINHEIRO PARA OUTRA CONTA.
        # CASO O SALDO DA CONTA SEJA INFERIOR AO VALOR DE TRANSFERÊNCIA A TRANSAÇÃO SERÁ RECUSADA.
        if self.saldo - valor <= 0:
            print(f'Saldo insuficiente para concluir a operação, {self.consultar_saldo()} e o valor que deseja '
                  f'transferir é de R${valor:,.2f}')
        else:
            self.saldo -= valor
            outra_conta.saldo = valor
            print(f'O valor de R${valor:,.2f} foi transferido com sucesso!!')



if __name__ == '__main__':
    conta = ContaCorrente('Felipe', '111.222.333-55', 50)
    conta.depositar(100)
    conta.sacar(50)
    conta.consultar_saldo()
    conta2 = ContaCorrente('Fernando', '132.231.444-56')
    conta.transferencia(200, conta2)
    conta2.consultar_saldo()
