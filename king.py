
# from piece import Piece
# from movimientos import ReglasDeMovimientos

# class King(Piece):
    
#     def __init__(self, color):
#         super().__init__(color)  # Llama al constructor de la clase Piece.
#         self.__movimientos_king__ = ReglasDeMovimientos()  # Instancia de las reglas de movimientos.

#     def valid_moves(self, from_row, from_col, to_row, to_col):
#         # Valida el movimiento del rey utilizando el método de movimiento de la clase ReglasDeMovimientos.
#         self.__movimientos_king__.king_movement(from_row, from_col, to_row, to_col)
#         return True

#     def __str__(self):
#         # Devuelve el símbolo del rey según su color.
#         return "♔" if self.get_color() == "WHITE" else "♚"

# AMBOS FUNCIONAN, NO BORRAR A MENOS DE ESTAR SEGURA

from piece import Piece
from movimientos import ReglasDeMovimientos
from piece import PieceWithMovement

# class King(Piece):
    
#     def __init__(self, color):
#         super().__init__(color)
#         self.movimientos = ReglasDeMovimientos()  # Usar el nuevo enfoque para movimientos

#     def valid_moves(self, from_row, from_col, to_row, to_col, board):
#         # Valida el movimiento del rey
#         self.movimientos.king_movement(from_row, from_col, to_row, to_col)
#         return True

#     def __str__(self):
#         return "♔" if self.get_color() == "WHITE" else "♚"











# class King(Piece):
        
#         def __init__(self, color):
#             super().__init__(color)
#             self._initialize_movements()

#         def _initialize_movements(self):
#             """Inicializa las reglas de movimientos para el rey"""
#             self.movimientos = ReglasDeMovimientos()  # Mover la lógica común aquí

#         def valid_moves(self, from_row, from_col, to_row, to_col, board):
#             self.movimientos.king_movement(from_row, from_col, to_row, to_col)
#             return True

# class King(PieceWithMovement):
#         def valid_moves(self, from_row, from_col, to_row, to_col, board):
#             self.movimientos.king_movement(from_row, from_col, to_row, to_col)
#             return True

#         def __str__(self):
#             return "♔" if self.get_color() == "WHITE" else "♚"


# from piece import PieceWithMovement
# from movimientos import ReglasDeMovimientos

# class King(PieceWithMovement):
#     def __init__(self, color):
#         super().__init__(color)
#         self.movimientos = ReglasDeMovimientos()  # Inicializa las reglas de movimientos para el rey

#     def valid_moves(self, from_row, from_col, to_row, to_col, board):
#         return self.movimientos.king_movement(from_row, from_col, to_row, to_col)

#     def __str__(self):
#         return "♔" if self.get_color() == "WHITE" else "♚"

class King(PieceWithMovement):
    def __init__(self, color):
        super().__init__(color)
        self.movimientos = ReglasDeMovimientos()

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        try:
            self.movimientos.king_movement(from_row, from_col, to_row, to_col)
            return True  # Movimiento válido
        except Exception:  # Puedes ser más específico en las excepciones que atrapas
            return False  # Movimiento no válido

    def __str__(self):
        return "♔" if self.get_color() == "WHITE" else "♚"