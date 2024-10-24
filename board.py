
from piece import Piece
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
from excepciones import InvalidCoordinates, NoPieceAtPosition, InvalidMove
from movimientos import ReglasDeMovimientos

class Board:
    def __init__(self):
        """Inicializa el tablero vacío y coloca las piezas en sus posiciones iniciales."""
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__initialize_pieces__()
    

    def __initialize_pieces__(self):
        """Coloca todas las piezas en sus posiciones iniciales."""

        self.__positions__[0][0] = Rook("WHITE")  # Cambiado a WHITE
        self.__positions__[0][7] = Rook("WHITE")  # Cambiado a WHITE
        self.__positions__[7][0] = Rook("BLACK")  # Cambiado a BLACK
        self.__positions__[7][7] = Rook("BLACK")  # Cambiado a BLACK

        # Caballos
        self.__positions__[0][1] = Knight("WHITE")  # Cambiado a WHITE
        self.__positions__[0][6] = Knight("WHITE")  # Cambiado a WHITE
        self.__positions__[7][1] = Knight("BLACK")  # Cambiado a BLACK
        self.__positions__[7][6] = Knight("BLACK")  # Cambiado a BLACK

        # Alfiles
        self.__positions__[0][2] = Bishop("WHITE")  # Cambiado a WHITE
        self.__positions__[0][5] = Bishop("WHITE")  # Cambiado a WHITE
        self.__positions__[7][2] = Bishop("BLACK")  # Cambiado a BLACK
        self.__positions__[7][5] = Bishop("BLACK")  # Cambiado a BLACK

        # Reyes y Reinas
        self.__positions__[0][3] = Queen("WHITE")  # Cambiado a WHITE
        self.__positions__[0][4] = King("WHITE")  # Cambiado a WHITE
        self.__positions__[7][3] = Queen("BLACK")  # Cambiado a BLACK
        self.__positions__[7][4] = King("BLACK")  # Cambiado a BLACK

        # Peones
        for col in range(8):
            self.__positions__[1][col] = Pawn("WHITE")  # Cambiado a WHITE
            self.__positions__[6][col] = Pawn("BLACK")  # Cambiado a BLACK
           

    def __str__(self):
        """Devuelve una representación en cadena del tablero."""
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "
                else:
                    board_str += ". "
            board_str += "\n"
        return board_str

    def valid_position(self, row, col):
        """Verifica si la posición está dentro del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece(self, row, col):
        """Devuelve la pieza en una posición determinada o None si está vacía."""
        if not self.valid_position(row, col):
            return None  # Cambiar a retornar None en lugar de lanzar una excepción
        return self.__positions__[row][col]

    def move_piece(self, from_row, from_col, to_row, to_col):
        """Mueve una pieza de una posición a otra si el movimiento es válido."""
        if not self.valid_position(from_row, from_col) or not self.valid_position(to_row, to_col):
            raise InvalidCoordinates("Una o ambas coordenadas están fuera del rango del tablero")

        # Obtener la pieza de origen
        piece = self.get_piece(from_row, from_col)

        # Verificar si el movimiento es válido según las reglas de la pieza
        if not piece.valid_moves(from_row, from_col, to_row, to_col, self):
            raise InvalidMove("El movimiento no es válido para esta pieza")

        # Verificar si la posición de destino está vacía o contiene una pieza del oponente
        destination_piece = self.get_piece(to_row, to_col)
        if destination_piece is not None and destination_piece.get_color() == piece.get_color():
            raise InvalidMove("No se puede mover a una posición ocupada por una pieza del mismo color")

        # Realizar el movimiento
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None

    def is_position_empty(self, row, col):
        """Verifica si una posición está vacía."""
        return self.__positions__[row][col] is None

    def is_path_clear(self, from_row, from_col, to_row, to_col):
        """Verifica si el camino entre dos posiciones está libre de piezas."""
        row_step = 1 if to_row > from_row else -1 if to_row < from_row else 0
        col_step = 1 if to_col > from_col else -1 if to_col < from_col else 0
        
        current_row, current_col = from_row + row_step, from_col + col_step
        
        while current_row != to_row or current_col != to_col:
            if not self.is_position_empty(current_row, current_col):
                return False
            current_row += row_step
            current_col += col_step

        return True
   


