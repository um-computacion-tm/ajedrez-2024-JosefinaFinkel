
from piece import Piece
from movimientos import ReglasDeMovimientos

class Pawn(Piece):
    
    def __init__(self, color):
        super().__init__(color)  # Llama al constructor de la clase Piece.
        self.__movimientos_pawn__ = ReglasDeMovimientos()  # Instancia de las reglas de movimientos.

    def valid_moves(self, from_row, from_col, to_row, to_col):
        # Valida el movimiento del peón utilizando el método de movimiento de la clase ReglasDeMovimientos.
        self.__movimientos_pawn__.pawn_movement(from_row, from_col, to_row, to_col)
        return True

    def __str__(self):
        # Devuelve el símbolo del peón según su color.
        return "♙" if self.get_color() == "WHITE" else "♟"
