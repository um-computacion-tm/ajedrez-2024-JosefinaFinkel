

from excepciones import *

class ReglasDeMovimientos:

    def __init__(self):
        pass 

    def vertical_move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es vertical."""
        if from_col != to_col:
            raise InvalidMoveVertical("El movimiento no es vertical")
        return 1 if to_row > from_row else -1

    def horizontal_move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es horizontal."""
        if from_row != to_row:
            raise InvalidMoveHorizontal("El movimiento no es horizontal")
        return 1 if to_col > from_col else -1

    def vertical_horizontal_move(self, from_row, from_col, to_row, to_col): 
        """Combina movimientos verticales y horizontales, o lanza una excepción si no es ninguno de los dos."""
        if from_row != to_row and from_col != to_col:
            raise InvalidMoveVerticalHorizontal("El movimiento solo puede ser en vertical o horizontal")
        if from_row != to_row:
            return self.vertical_move(from_row, from_col, to_row, to_col)
        else:
            return self.horizontal_move(from_row, from_col, to_row, to_col)
    
    def row_difference_move(self, from_row, to_row):
        """Calcula la diferencia entre filas usando valor absoluto."""
        return abs(to_row - from_row)
        
    def col_difference_move(self, from_col, to_col):
        """Calcula la diferencia entre columnas usando valor absoluto."""
        return abs(to_col - from_col)
        
    def diagonal_move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es diagonal, lanza una excepción si no lo es."""
        row_diff = self.row_difference_move(from_row, to_row)
        col_diff = self.col_difference_move(from_col, to_col)
        if row_diff != col_diff:
            raise InvalidMoveDiagonal("El movimiento solo puede ser en diagonal")
        direction_row = 1 if to_row > from_row else -1
        direction_col = 1 if to_col > from_col else -1
        return direction_row, direction_col

    def knight_movement(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es válido para un caballo (L)."""
        row_diff = self.row_difference_move(from_row, to_row)
        col_diff = self.col_difference_move(from_col, to_col)
        if not (row_diff == 2 and col_diff == 1) and not (row_diff == 1 and col_diff == 2):
            raise InvalidMoveKnight("El movimiento del caballo no es válido")
    
    def king_movement(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es válido para un rey (una casilla en cualquier dirección)."""
        row_diff = self.row_difference_move(from_row, to_row)
        col_diff = self.col_difference_move(from_col, to_col)
        if row_diff > 1 or col_diff > 1:
            raise InvalidMoveKing("El rey solo puede moverse una casilla en cualquier dirección")

    def queen_movement(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento es válido para una reina (combinación de movimientos verticales, horizontales y diagonales)."""
        
        try:
            # Verifica el movimiento diagonal
            self.diagonal_move(from_row, from_col, to_row, to_col)
            return True
        except InvalidMoveDiagonal:
            pass  # Si no es diagonal, continúa verificando otros movimientos

        try:
            # Verifica el movimiento vertical u horizontal
            self.vertical_horizontal_move(from_row, from_col, to_row, to_col)
            return True
        except InvalidMoveVerticalHorizontal:
            pass  # Si no es vertical ni horizontal, continúa con la verificación

        raise InvalidMoveQueen("La reina solo puede moverse en línea recta o en diagonal")


    # def pawn_movement(self, from_row, from_col, to_row, to_col):
    #     # Lógica para el movimiento del peón, como solo avanzar en la misma columna
    #     if from_col != to_col:
    #         raise InvalidMovePawn("El peón solo puede avanzar en la misma columna")
        
    #     # Movimiento de una casilla hacia adelante
    #     if abs(from_row - to_row) == 1:
    #         return True

    #     # Movimiento inicial de dos casillas hacia adelante desde la posición de inicio
    #     if abs(from_row - to_row) == 2 and (from_row == 1 or from_row == 6):
    #         return True

    #     raise InvalidMovePawn("El movimiento del peón no es válido.")

    
    def pawn_movement(self, from_row, from_col, to_row, to_col, color):
        if color == "WHITE":
            if from_row == 1:  # Primer movimiento
                if to_row == from_row + 2 and to_col == from_col:
                    return True  # Movimiento de dos casillas
            if to_row == from_row + 1 and to_col == from_col:
                return True  # Movimiento de una casilla

        if color == "BLACK":
            if from_row == 6:  # Primer movimiento
                if to_row == from_row - 2 and to_col == from_col:
                    return True  # Movimiento de dos casillas
            if to_row == from_row - 1 and to_col == from_col:
                return True  # Movimiento de una casilla

        # Si llega aquí, el movimiento es inválido
        raise InvalidMovePawn("Movimiento inválido para el peón")

