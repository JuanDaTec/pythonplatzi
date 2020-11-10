class Rectangulo:
    
    def __init__(self, base , altura):
        """
        Metodo constructor de la super clase.
        """
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura
    
class Cuadrado(Rectangulo):
    
    def __init__(self, lado):
        """
        Constructor de la clase Cuadrado, que extiende de la super clase Rectangulo
        """
        super().__init__(lado, lado) # Trae el metodo constructor de la super clase declarada.
    
if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print('El area del rectangulo es:', rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print('El area del cuadrado es:', cuadrado.area())