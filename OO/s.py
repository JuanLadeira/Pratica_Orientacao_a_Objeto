from datetime import datetime
import pytz


class ContaCorrente:  # CRIAÇÃO DA CLASSE CONTA CORRENTE
    """
    Cria um objeto ContaCorrente que gerencia as contas dos clientes.
    Atributos:
        nome (str): Nome do cliente
        cpf (str): cpf do cliente
        saldo (float): saldo disponivel na conta do cliente
        limite (float): limite do cheque especial do cliente
        agencia (int): Agencia do cliente
        num_conta (int): Numero da conta do cliente
        transacoes (str): Historico de transações
    """
    @staticmethod
    def _data_hora():
        """
            Retorna a data e hora em que uma transação foi realizada.
        @rtype: object
        """
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    @staticmethod
    def linha():
        """
            Cria linhas para separação de código a fim de facilitar a visibilidade.
        @rtype: object
        """
        print('=-' * 21)

    def __init__(self, nome, cpf, agencia, num_conta, saldo=0):  # ATRIBUTOS DE CLASSE
        self._nome = nome
        self._cpf = cpf
        self._saldo = saldo
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    def consultar_saldo(self):  # METODO PARA CONSULTAR SALDO
        """
            Consulta o saldo disponivel do cliente.
        @rtype: object
        """
        print(f'O saldo atual da conta inscrita sob o _cpf:{self._cpf} é de R${self._saldo:,.2f}')
        ContaCorrente.linha()
        return f'O seu saldo atual é de R${self._saldo:,.2f}'

    def depositar(self, valor):  # METODO PARA DEPOSITAR DINHEIRO
        """
            Deposita dinheiro/valor na conta do cliente.
        @rtype: object
        @param valor: int
        """
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):  # METODO PRIVADO PARA DEFINIR LIMITE DA CONTA, PARECIDO COM UM CHEQUE ESPECIAL
        """
            Metodo privado que retorna o limite de cheque especial do cliente
        @return:
        """
        self._limite = -1000
        return self._limite

    def sacar(self, valor):  # METODO PARA SACAR DINHEIRO
        """
            Metodo que permite sacar o dinheiro da conta do cliente.
        @rtype: object
        @param valor: int
        """
        if self._saldo <= self._limite_conta():
            print(f'Saldo insuficiente para sacar o valor, {self.consultar_saldo()}')
            ContaCorrente.linha()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def transferencia(self, valor, outra_conta):  # METODO PARA TRANSFERIR DINHEIRO PARA OUTRA CONTA.
        """
            Metodo que permite transferir saldo entre as contas dos clientes.
        @rtype: object
        @param valor: int
        @param outra_conta: object
        """
        # CASO O SALDO DA CONTA SEJA INFERIOR AO VALOR DE TRANSFERÊNCIA A TRANSAÇÃO SERÁ RECUSADA.
        if self._saldo - valor <= self._limite_conta():
            print(f'Saldo insuficiente para concluir a operação, {self.consultar_saldo()} e o valor que deseja '
                  f'transferir é de R${valor:,.2f}')
            ContaCorrente.linha()
        else:
            self._saldo -= valor
            outra_conta._saldo = valor
            print(f'O valor de R${valor:,.2f} foi transferido para conta do(a) {outra_conta._nome} com sucesso!!')
            ContaCorrente.linha()

    def consultar_limite_cheque_especial(self):  # METODO PARA CONSULTAR LIMITE DE CHEQUE ESPECIAL.
        """
            Metodo que permite consultar o limite do cheque especial do cliente.
        @rtype: object
        """
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')
        ContaCorrente.linha()

    def visualizar_historico(self):
        for transacao in self._transacoes:
            print(f'**'*5 + 'HISTORICO DE TRANSAÇÕES'+'**'*5+'\n',
                  f'Data da transação: {transacao[2]}\n',
                  f'Valor da transação R${transacao[0]:,.2f}\n',
                  f'Saldo da conta: RS{transacao[1]:,.2f}')
        
        ContaCorrente.linha()





if __name__ == '__main__':
    # CRIANDO A CONTA FELIPE
    conta_felipe = ContaCorrente('Felipe', '111.222.333-55', '0001', '5065741', 50)
    # CRIANDO A CONTA FERNANDO
    conta_fernando = ContaCorrente('Fernando', '132.231.444-56', '0001', '5095743')
    # DEPOSITANDO NA CONTA FELIPE
    conta_felipe.depositar(100)
    # SANCANDO DA CONTA FELIPE
    conta_felipe.sacar(50)
    # CONSULTANDO SALDO DA CONTA FELIPE
    conta_felipe.consultar_saldo()
    # TRANSFERINDO SALDO DA CONTA FELIPE PARA A CONTA FERNANDO
    conta_felipe.transferencia(200, conta_fernando)
    # CONSULTANDO SALDO DA CONTA FERNANDO
    conta_fernando.consultar_saldo()
    # CONSULTANDO LIMITE DO CHEQUE ESPECIAL DA CONTA FERNANDO
    conta_fernando.consultar_limite_cheque_especial()
    # CONSULTANDO O HISTORICO DE TRANSAÇÕES DA CONTA FELIPE
    conta_felipe.visualizar_historico()
