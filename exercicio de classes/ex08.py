class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0

    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f"Abastecido com {litros}L. Combustível atual: {self.nivel_combustivel}L")

    def dirigir(self, distancia):
        consumo = distancia / 10  # 1 litro a cada 10 km
        if self.nivel_combustivel >= consumo:
            self.nivel_combustivel -= consumo
            print(f"O carro {self.modelo} andou {distancia} km.")
        else:
            print("Não há combustível suficiente.")

carro = Carro("Fusca")
carro.abastecer(5)
carro.dirigir(30)
carro.dirigir(40)
