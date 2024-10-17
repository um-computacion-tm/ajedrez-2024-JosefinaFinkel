
# from piece import Piece
# from movimientos import ReglasDeMovimientos
# from board import Board

# class Pawn(Piece):
    
#     def __init__(self, color):
#         super().__init__(color)  # Llama al constructor de la clase Piece.
#         self.__movimientos_pawn__ = ReglasDeMovimientos()  # Instancia de las reglas de movimientos.

#     def valid_moves(self, from_row, from_col, to_row, to_col, board):
#         # Valida el movimiento del peón utilizando el método de movimiento de la clase ReglasDeMovimientos.
#         self.__movimientos_pawn__.pawn_movement(from_row, from_col, to_row, to_col)
#         return True

#     def __str__(self):
#         # Devuelve el símbolo del peón según su color.
#         return "♙" if self.get_color() == "WHITE" else "♟"

from piece import Piece
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMoveNotInBoard, InvalidMoveSameColor

class Pawn(Piece):
    
    def __init__(self, color):
        super().__init__(color)  # Llama al constructor de la clase Piece.
        self.__movimientos_pawn__ = ReglasDeMovimientos()  # Instancia de las reglas de movimientos.

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        from board import Board
        # 1. Verifica si la posición de destino está dentro del tablero
        if not board.valid_position(to_row, to_col):
            raise InvalidMoveNotInBoard("La posición de destino no es válida")
        
        # 2. Verifica si la casilla de destino está ocupada por una pieza del mismo color
        destination_piece = board.get_piece(to_row, to_col)
        if destination_piece and destination_piece.get_color() == self.get_color():
            raise InvalidMoveSameColor("No se puede mover a una posición ocupada por una pieza del mismo color")

        # 3. Valida el movimiento del peón utilizando las reglas de movimientos
        self.__movimientos_pawn__.pawn_movement(from_row, from_col, to_row, to_col)
        
        return True

    def __str__(self):
        # Devuelve el símbolo del peón según su color.
        return "♙" if self.get_color() == "WHITE" else "♟"
