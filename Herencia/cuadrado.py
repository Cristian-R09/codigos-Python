from Figura import FiguraGeometrica
from Color import Color

        

class Cuadrado (FiguraGeometrica, Color):
    def __init__(self, ancho, alto,color ):
        # super().__init__(ancho, color)
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area (self):
        return self.ancho * self.alto
    
    def __str__(self) -> str:
        return super().__str__()