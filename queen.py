
from piece import Piece
from movimientos import ReglasDeMovimientos

class Queen(Piece):
    
    def __init__(self, color):
        super().__init__(color)  # Llama al constructor de la clase Piece.
        self.__movimientos_queen__ = ReglasDeMovimientos()

    def valid_moves(self, from_row, from_col, to_row, to_col):
        # Valida el movimiento de la reina utilizando el método de movimiento de la clase ReglasDeMovimientos.
        self.__movimientos_queen__.queen_movement(from_row, from_col, to_row, to_col)
        return True

    def __str__(self):
        # Devuelve el símbolo de la reina según su color.
        return "♕" if self.get_color() == "white" else "♛"
