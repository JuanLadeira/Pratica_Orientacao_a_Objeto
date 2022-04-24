import self as self

nome = 'Felipe'

print(type(nome))

print(nome.capitalize())


class TV:

    def __init__(self):
        self.cor = 'preta'
        self.tamanho = 50
        self.canal = 'Netflix'
        self.volume = 60
        self.status = False

    def mudar_de_canal(self, canal):
        self.canal = canal

    def aumentar_volume(self, volume=1):
        self.volume += volume

    def diminuir_volume(self, volume=1):
        self.volume -= volume


if __name__ == '__main__':
    tv_sala = TV()
    tv_sala.diminuir_volume(10)
    tv_quarto = TV()
    print(tv_sala.volume)
    print(tv_quarto.volume)
