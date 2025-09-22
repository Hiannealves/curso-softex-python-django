class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem motor de {self.motor.potencia} cavalos.")

carro = Carro("Ferrari", 500)
carro.exibir_potencia()
