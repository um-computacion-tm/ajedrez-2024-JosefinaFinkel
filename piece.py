
from excepciones import *
    
class Piece:
    # La clase Piece es la clase base para todas las piezas. Obtienen su color y método str que devuelve el símbolo de la pieza.
    
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        # Devuelve el símbolo de la pieza (esto se definirá en las subclases).
        return "Pieza"

    def get_color(self):
        return self.__color__
