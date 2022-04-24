class TV:  # OBJETO TV
    COR = 'Preta'   # ATRIBUTO DE CLASSE, OU SEJA, CASO FOR ALTERADO, ALTERARÁ TODOS OS DEMAIS
    # OBJETOS QUE UTILIZAREM ESSA CLASE.

    def __init__(self):  # ATRIBUTOS DO OBJETO TV
        self.tamanho = 50
        self.canal = 'Netflix'
        self.volume = 60
        self.status = False

    def ligar_tv(self):
        self.status = True

    def mudar_de_canal(self, novo_canal):  # METODO DE TROCAR DE CANAL DO OBJETO TV
        self.canal = novo_canal
        print(f'Canal da Tv alterado para {novo_canal}.')

    def aumentar_volume(self, volume=1):  # METODO DE AUMENTAR O VOLUME DO OBJETO TV
        self.volume += volume
        print(f'Volume da TV aumentado para {self.volume}.')

    def diminuir_volume(self, volume=1):  # METODO DE DIMINUIR VOLUME DO OBJETO TV
        self.volume -= volume
        print(f'Volume reduzido para {self.volume}.')


if __name__ == '__main__':  # TESTES DE FUNCIONAMENTO
    tv_sala = TV()
    tv_sala.diminuir_volume(10)
    tv_quarto = TV()
    tv_quarto.mudar_de_canal('Youtube')
    print(tv_sala.volume)
    print(tv_quarto.volume)
