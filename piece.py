
from excepciones import *
    
WHITE = "WHITE"
BLACK = "BLACK"

class Piece:
    # La clase Piece es la clase base para todas las piezas. Obtienen su color y método str que devuelve el símbolo de la pieza.
    
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        # Devuelve el símbolo de la pieza (esto se definirá en las subclases).
        return "Pieza"

    def get_color(self):
        return self.__color__

    # Agregar la clase base con movimientos aquí
class PieceWithMovement(Piece):
    
    def __init__(self, color):
        super().__init__(color)
        self._initialize_movements()

    def _initialize_movements(self):
        """Inicializa las reglas de movimientos comunes"""
        from movimientos import ReglasDeMovimientos
        self.movimientos = ReglasDeMovimientos()


    def __str__(self):
        return "♗" if self.get_color() == WHITE else "♝"
