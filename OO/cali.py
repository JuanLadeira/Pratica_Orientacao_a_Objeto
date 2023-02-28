class Incertezas():
    def __init__(self, lista):
        self.medicoes = lista
    
    
    def calcular_media(self):
        soma = 0
        for medicao in self.medicoes:
            soma += medicao
        média = soma/len(self.medicoes)
        return média
    



if __name__ == "__main__":
    medicoes = [10, 10 , 10, 10]
    incerteza = Incertezas(medicoes)
    média = incerteza.calcular_media()

    print(média)