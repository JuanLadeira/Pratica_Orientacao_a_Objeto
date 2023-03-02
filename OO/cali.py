import math
import scipy.stats as stats

class Instrumento():
    def __init__(self, faixa, resolucao):
        self.medicoes_por_ponto = []
        self.faixa = faixa
        self.resolucao = resolucao
    
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

    def calcular_incerteza_do_padrao(self, u_padrao, k):
        return u_padrao/k

    def calcular_incerteza_da_resolucao(self):
        return self.resolucao/math.sqrt(3)

    def calcular_incerteza_combinada(self, ponto):
        incerteza_da_repetitividade = self.calcular_incerteza_da_repetitividade(ponto)
        incerteza_do_padrao = self.calcular_incerteza_do_padrao(1,2)
        incerteza_da_resolucao = self.calcular_incerteza_da_resolucao()
        incerteza_combinada = math.sqrt((incerteza_da_repetitividade**2)+(incerteza_do_padrao**2)+(incerteza_da_resolucao**2))
        return incerteza_combinada
        
    def calcular_grau_de_liberdade(self, ponto):
        incerteza_combinada = self.calcular_incerteza_combinada(ponto)
        incerteza_repetitividade = self.calcular_incerteza_da_repetitividade(ponto)
        n = len(self.medicoes_por_ponto[ponto-1])
        return incerteza_combinada**4/(incerteza_repetitividade**4/(n-1))

    def calcular_fator_de_abrangencia(self, ponto):
        grau_de_liberdade = self.calcular_grau_de_liberdade(ponto)
        if grau_de_liberdade > 100:
            fator_de_abrangencia = 2.00
            return fator_de_abrangencia
        fator_de_abrangencia = stats.t.cdf(1-0,9545, grau_de_liberdade)
        return fator_de_abrangencia

    def calcular_incerteza_expandida(self, ponto):
        incerteza_combinada = self.calcular_incerteza_combinada(ponto)
        fator_de_abrangencia = self.calcular_fator_de_abrangencia(ponto)
        return incerteza_combinada * fator_de_abrangencia
    
    def exibir_resultados(self):
        for i, medicoes in enumerate(self.medicoes_por_ponto):
            media = self.calcular_media(i+1)
            desvio_padrao = self.calcular_desvio_padrao(i+1)
            incerteza_tipo_A = self.calcular_incerteza_da_repetitividade(i+1)
            incerteza_resolucao = self.calcular_incerteza_da_resolucao()
            incerteza_do_padrao = self.calcular_incerteza_do_padrao(1,2)
            incerteza_combinada = self.calcular_incerteza_combinada(i+1)
            fator_de_abrangencia = self.calcular_fator_de_abrangencia(i+1)
            grau_de_liberdade = self.calcular_grau_de_liberdade(i+1)
            incerteza_expandida = self.calcular_incerteza_expandida(i+1)
            print(f'----------------------------RESULTADOS-----------------------------------')
            print(f'Ponto {i+1}: média = {media:.2f}, desvio padrão = {desvio_padrao:.2f}')
            print(f'----------------------------INCERTEZAS-----------------------------------')
            print(f'Ua = {incerteza_tipo_A:.2f}, Uresolução = {incerteza_resolucao:.2f}, uPadrão = {incerteza_do_padrao:.2f}')
            print(f'Ucombinada = {incerteza_combinada:.2f}, grau de liberdade = {grau_de_liberdade:.2f}, fator de abrangencia = {fator_de_abrangencia:.4f}')
            print(f'Incerteza Expandida = {incerteza_expandida:.2f}')


if __name__ == "__main__":
    paquímetro = Instrumento(faixa='0 a 150 mm', resolucao=0.1)
    paquímetro.adicionar_medicao(1, 19)
    paquímetro.adicionar_medicao(1, 20)
    paquímetro.adicionar_medicao(1, 20)
    paquímetro.exibir_resultados()


