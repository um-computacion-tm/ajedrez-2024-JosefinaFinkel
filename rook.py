

# from piece import Piece
# from movimientos import ReglasDeMovimientos
# from excepciones import InvalidMoveVerticalHorizontal


# class Rook(Piece):


#     def __init__(self, color):
#         super().__init__(color)
#         self.__movimientos_rook__ = ReglasDeMovimientos()

#     def __str__(self):
#         return "♖" if self.get_color() == "WHITE" else "♜"

#     def valid_moves(self, from_row, from_col, to_row, to_col, board):
#         # Verificar que el movimiento es estrictamente vertical o horizontal
#         if not (from_row == to_row or from_col == to_col):
#             raise InvalidMoveVerticalHorizontal("El movimiento solo puede ser en vertical o horizontal")
        
#         # Verificar si el camino está despejado
#         if not board.is_path_clear(from_row, from_col, to_row, to_col):
#             raise InvalidMoveVerticalHorizontal("El camino no está despejado")
        
#         return True

from piece import Piece
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMoveVerticalHorizontal
from excepciones import InvalidMove

class Rook(Piece):
    
    def __init__(self, color):
        super().__init__(color)
        self.movimientos = ReglasDeMovimientos()

   
   
    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        if from_row != to_row and from_col != to_col:
            raise InvalidMoveVerticalHorizontal("El movimiento no es vertical u horizontal.")
        
        if not board.is_path_clear(from_row, from_col, to_row, to_col):
            raise InvalidMoveVerticalHorizontal("El camino no está despejado.")
        
        return True  # Si todo es válido



    def __str__(self):
        return "♖" if self.get_color() == "WHITE" else "♜"




    