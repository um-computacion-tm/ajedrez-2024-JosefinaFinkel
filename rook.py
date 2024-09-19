

from piece import Piece
from movimientos import ReglasDeMovimientos
from execpciones import InvalidMoveVerticalHorizontal


class Rook(Piece):


    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_rook__ = ReglasDeMovimientos()

    def __str__(self):
        return "♖" if self.get_color() == "WHITE" else "♜"

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        if not self.__movimientos_rook__.vertical_horizontal_move(from_row, from_col, to_row, to_col):
            raise InvalidMoveVerticalHorizontal("El movimiento solo puede ser en vertical o horizontal")
        return True




    