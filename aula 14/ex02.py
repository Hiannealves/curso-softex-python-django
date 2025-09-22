class Circulo:
    pi = 3,14    
    def __init__(self, raio:float):
        self._raio = raio
          

    @property
    def raio(self):
              return self._raio    
    
    @raio.setter 
    def raio (self, valor:float):
        if isinstance (valor,float) and valor > 0:
            self._raio = valor
            
        else:
            print("Erro: o raio deve ser positivo")

    def calcular_area(self):
        return Circulo.pi*(self._raio**2)    
    
    def mostrar_area(self):
         print(self.calcular_area )

         