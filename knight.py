



from movimientos import ReglasDeMovimientos


# class Knight(PieceWithMovement):
#     def __init__(self, color):
#         super().__init__(color)
#         self.movimientos = ReglasDeMovimientos()

#     def valid_moves(self, from_row, from_col, to_row, to_col, board):
#         try:
#             self.movimientos.knight_movement(from_row, from_col, to_row, to_col)
#             return True  # Movimiento válido
#         except Exception:  # Puedes ser más específico en las excepciones que atrapas
#             return False  # Movimiento no válido

#     def __str__(self):
#         return "♘" if self.get_color() == "WHITE" else "♞"

from piece import PieceWithMovement

class Knight(PieceWithMovement):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        try:
            self.movimientos.knight_movement(from_row, from_col, to_row, to_col)
            return True  # Movimiento válido
        except Exception:  # Puedes ser más específico en las excepciones que atrapas
            return False  # Movimiento no válido

    def __str__(self):
        return "♘" if self.get_color() == "WHITE" else "♞"
