# from piece import Piece
# class Knight(Piece):
#     white_str_ = "♖"
#     black_str = "♜"

#     def possible_positions_vd(self, row, col):
#         possibles = []
#         for next_row in range(row + 1, 8):
#             possibles.append((next_row, col))
#         return possibles
    
# def possible_positions_va(self, row, col):
#         possibles = []
#         for next_row in range(row - 1, -1, -1):
#             possibles.append((next_row, col))
#         return possibles

from piece import Piece
from movimientos import ReglasDeMovimientos

class Knight(Piece):
    
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos_knight__.knight_movement(from_row, from_col, to_row, to_col)
        return True

    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_knight__ = ReglasDeMovimientos()

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♘"
        else:
            return "♞"
