from datetime import datetime
import pytz


class ContaCorrente:  # CRIAÇÃO DA CLASSE CONTA CORRENTE

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    @staticmethod
    def linha():
        print('=-' * 20)

    def __init__(self, nome, cpf, agencia, num_conta, saldo=0):  # ATRIBUTOS DE CLASSE
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):  # METODO PARA CONSULTAR SALDO
        print(f'O saldo atual da conta inscrita sob o CPF:{self.cpf} é de R${self.saldo:,.2f}')
        ContaCorrente.linha()
        return f'O seu saldo atual é de R${self.saldo:,.2f}'

    def depositar(self, valor):  # METODO PARA DEPOSITAR DINHEIRO
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):  # METODO PRIVADO PARA DEFINIR LIMITE DA CONTA, PARECIDO COM UM CHEQUE ESPECIAL
        self.limite = -1000
        return self.limite

    def sacar(self, valor):  # METODO PARA SACAR DINHEIRO
        if self.saldo <= self._limite_conta():
            print(f'Saldo insuficiente para sacar o valor, {self.consultar_saldo()}')
            ContaCorrente.linha()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def transferencia(self, valor, outra_conta):  # METODO PARA TRANSFERIR DINHEIRO PARA OUTRA CONTA.
        # CASO O SALDO DA CONTA SEJA INFERIOR AO VALOR DE TRANSFERÊNCIA A TRANSAÇÃO SERÁ RECUSADA.
        if self.saldo - valor <= self._limite_conta():
            print(f'Saldo insuficiente para concluir a operação, {self.consultar_saldo()} e o valor que deseja '
                  f'transferir é de R${valor:,.2f}')
            ContaCorrente.linha()
        else:
            self.saldo -= valor
            outra_conta.saldo = valor
            print(f'O valor de R${valor:,.2f} foi transferido para conta do(a) {outra_conta.nome} com sucesso!!')
            ContaCorrente.linha()

    def consultar_limite_cheque_especial(self):  # METODO PARA CONSULTAR LIMITE DE CHEQUE ESPECIAL.
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')
        ContaCorrente.linha()

    def visualizar_historico(self):
        for transacao in self.transacoes:
            ContaCorrente.linha()
            print(f'Data da transação: {transacao[2]}\n'
                  f'Valor da transação R${transacao[0]:,.2f}\n'
                  f'Saldo da conta: RS{transacao[1]:,.2f}')





if __name__ == '__main__':
    # CRIANDO A CONTA FELIPE
    conta_felipe = ContaCorrente('Felipe', '111.222.333-55', '0001', '5065741', 50)
    # DEPOSITANDO NA CONTA FELIPE
    conta_felipe.depositar(100)
    # SANCANDO DA CONTA FELIPE
    conta_felipe.sacar(50)
    # CONSULTANDO SALDO DA CONTA FELIPE
    conta_felipe.consultar_saldo()
    # CRIANDO A CONTA FERNANDO
    conta_fernando = ContaCorrente('Fernando', '132.231.444-56', '0001', '5095743')
    # TRANSFERINDO SALDO DA CONTA FELIPE PARA A CONTA FERNANDO
    conta_felipe.transferencia(200, conta_fernando)
    # CONSULTANDO SALDO DA CONTA FERNANDO
    conta_fernando.consultar_saldo()
    # CONSULTANDO LIMITE DO CHEQUE ESPECIAL DA CONTA FERNANDO
    conta_fernando.consultar_limite_cheque_especial()
    # CONSULTANDO O HISTORICO DE TRANSAÇÕES DA CONTA FELIPE
    print(conta_felipe.transacoes)
    conta_felipe.visualizar_historico()
