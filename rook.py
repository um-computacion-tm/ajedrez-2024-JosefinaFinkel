

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
        # Verificar que la posición inicial y final son válidas
        if not board.valid_position(from_row, from_col) or not board.valid_position(to_row, to_col):
            raise InvalidMoveVerticalHorizontal("Posición inválida")

        # Validar que el movimiento es estrictamente vertical o horizontal
        if not (from_row == to_row or from_col == to_col):
            raise InvalidMoveVerticalHorizontal("El movimiento solo puede ser en vertical o horizontal")
        
        # Aquí puedes agregar más validaciones como si el camino está despejado
        return True




    