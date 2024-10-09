

from piece import Piece
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMoveDiagonal

class Bishop(Piece):
    
    def __init__(self, color):
        super().__init__(color)  # Llama al constructor de la clase Piece.
        self.__movimientos_bishop__ = ReglasDeMovimientos()  # Instancia de las reglas de movimientos.

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        # Valida el movimiento del alfil utilizando el método de movimiento de la clase ReglasDeMovimientos.
        self.__movimientos_bishop__.diagonal_move(from_row, from_col, to_row, to_col)
        return True

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        if not self.__movimientos_bishop__.diagonal_move(from_row, from_col, to_row, to_col):
            raise InvalidMoveDiagonal("El movimiento solo puede ser en diagonal")
        return True
    
    def __str__(self):
        # Devuelve el símbolo del alfil según su color.
        return "♗" if self.get_color() == "WHITE" else "♝"
