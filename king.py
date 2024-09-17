from piece  import Piece
from movimientos import ReglasDeMovimientos

class King(Piece):
    
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos_king__.king_movement(from_row, from_col, to_row, to_col)
        return True

    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_king__ = ReglasDeMovimientos()

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♚"
        else:
            return "♔"
