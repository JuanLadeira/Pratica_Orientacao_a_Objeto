import math

class Instrumento():
    def __init__(self):
        self.medicoes_por_ponto = []
    
    def adicionar_medicao(self, ponto, medicao):
        if len(self.medicoes_por_ponto) < ponto:
            self.medicoes_por_ponto.append([medicao])
        else:
            self.medicoes_por_ponto[ponto-1].append(medicao)

    def calcular_media(self, ponto):
        medicoes = self.medicoes_por_ponto[ponto-1]
        return sum(medicoes)/ len(medicoes)

    def calcular_desvio_padrao(self, ponto):
        medicoes = self.medicoes_por_ponto[ponto-1]
        media = self.calcular_media(ponto)
        return math.sqrt(sum([(medicao - media)**2 for medicao in medicoes])/ (len(medicoes)-1))
    
    def calcular_incerteza_da_repetitividade(self, ponto):
        medicoes = self.medicoes_por_ponto[ponto-1]
        desvio_padrao = self.calcular_desvio_padrao(ponto)
        return desvio_padrao/math.sqrt(len(medicoes))
    
    def exibir_resultados(self):
        for i, medicoes in enumerate(self.medicoes_por_ponto):
            media = self.calcular_media(i+1)
            desvio_padrao = self.calcular_desvio_padrao(i+1)
            incerteza_tipo_A = self.calcular_incerteza_da_repetitividade(i+1)
            print(f'Ponto {i+1}: média = {media:.2f}, desvio padrão = {desvio_padrao:.2f}, Ua = {incerteza_tipo_A:.2f}')

    



if __name__ == "__main__":
    instrumento = Instrumento()
    instrumento.adicionar_medicao(1, 19)
    instrumento.adicionar_medicao(1, 20)
    instrumento.adicionar_medicao(1, 20)
    instrumento.exibir_resultados()


