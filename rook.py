

from piece import Piece
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMoveVerticalHorizontal


class Rook(Piece):


    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_rook__ = ReglasDeMovimientos()

    def __str__(self):
        return "♖" if self.get_color() == "white" else "♜"

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        if not self.__movimientos_rook__.vertical_horizontal_move(from_row, from_col, to_row, to_col):
            raise InvalidMoveVerticalHorizontal("El movimiento solo puede ser en vertical o horizontal")
        return True

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        # Validar que el movimiento es estrictamente vertical o horizontal
        return board.valid_position(from_row, from_col) and \
               (from_row == to_row or from_col == to_col)




    