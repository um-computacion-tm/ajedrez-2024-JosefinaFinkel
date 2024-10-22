

from piece import Piece
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMoveDiagonal, InvalidMoveVerticalHorizontal, InvalidMovePathOcuppied

class Queen(Piece):
    
    def __init__(self, color):
        super().__init__(color)
        self.movimientos = ReglasDeMovimientos()

    def valid_moves(self, from_row, from_col, to_row, to_col, board):
        try:
            # Verificar movimiento diagonal
            self.movimientos.movimiento_lineal(from_row, from_col, to_row, to_col)
        except InvalidMoveDiagonal:
            # Si no es diagonal, verifica movimiento vertical u horizontal
            if not (from_row == to_row or from_col == to_col):
                raise InvalidMoveVerticalHorizontal("El movimiento solo puede ser en diagonal, vertical u horizontal")
        
        # Verificar si el camino está despejado
        if not board.is_path_clear(from_row, from_col, to_row, to_col):
            raise InvalidMovePathOcuppied("El camino no está despejado")
        
        return True

    def __str__(self):
        return "♕" if self.get_color() == "WHITE" else "♛"
