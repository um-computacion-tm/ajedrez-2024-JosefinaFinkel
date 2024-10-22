

# from piece import Piece
# from movimientos import ReglasDeMovimientos
# from excepciones import InvalidMoveDiagonal

# class Bishop(Piece):
    
#     def __init__(self, color):
#         super().__init__(color)  # Llama al constructor de la clase Piece.
#         self.__movimientos_bishop__ = ReglasDeMovimientos()  # Instancia de las reglas de movimientos.
    
#     def __str__(self):
#         # Devuelve el símbolo del alfil según su color.
#         return "♗" if self.get_color() == "WHITE" else "♝"

#     def valid_moves(self, from_row, from_col, to_row, to_col, board):
#         # Verificar movimiento diagonal
#         if not self.__movimientos_bishop__.diagonal_move(from_row, from_col, to_row, to_col):
#             raise InvalidMoveDiagonal("El movimiento solo puede ser en diagonal")
        
#         # Verificar si el camino está despejado
#         if not board.is_path_clear(from_row, from_col, to_row, to_col):
#             raise InvalidMoveDiagonal("El camino no está despejado")
        
#         return True

from piece import Piece
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMoveDiagonal
from excepciones import InvalidMove

class Bishop(Piece):
    
    def __str__(self):
        return "♗" if self.get_color() == "WHITE" else "♝"


    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        if abs(from_row - to_row) != abs(from_col - to_col):
            raise InvalidMoveDiagonal("El movimiento no es diagonal.")
        
        if not board.is_path_clear(from_row, from_col, to_row, to_col):
            raise InvalidMoveDiagonal("El camino no está despejado.")
        
        return True  # Si todo es válido
