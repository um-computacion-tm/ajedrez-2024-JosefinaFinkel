# from piece import Piece

# class Board:
#     def __init__(self):
#         self.__positions__ = [] # Inicializa el tablero vacío
#         for _ in range(8):
#             col = [] # Crea una columna vacía
#             for _ in range(8):
#                 col.append(None) # Agrega 8 espacios vacíos (None) a la columna
#             self.__positions__.append(col) # Agrega la columna al tablero 

#         # Coloca las torres en sus posiciones iniciales
#         self.__positions__[0][0] = Piece("BLACK", self) # Black
#         self.__positions__[0][7] = Piece("BLACK", self) # Black
#         self.__positions__[7][7] = Piece("WHITE", self) # White
#         self.__positions__[7][0] = Piece("WHITE", self) # White
    

#     def __str__(self):
#         board_str = ""
#         for row in self.__positions__:
#             for cell in row:
#                 if cell is not None:
#                     board_str += str(cell)
#                 else:
#                     board_str += " "
#             board_str += "\n"
#         return board_str

#     def get_piece(self, row, col):
#         return self.__positions__[row][col] #dentro de los corchetes, deberia ir los numeros del 1 al 7
        

# #esto es el tablero 8x8, cada posición tiene un valor de None, o un número de 1 a 8.
# #columna (col): {none, none, none, none, none, none, none, none}
# #posición {col, col, col, col, col, col, col, col}
# #fila (row): {none, none, none, none, none, none, none, none}

# import unittest
# from board import Board
# from piece import Piece

# class TestBoard(unittest.TestCase):
#     def setUp(self):
#         self.board = Board()

#     def test_empty_positions(self):
#         """ Verifica que todas las posiciones iniciales están vacías (None), excepto las posiciones de las torres. """
#         for row in range(8):
#             for col in range(8):
#                 if (row == 0 and col in [0, 7]) or (row == 7 and col in [0, 7]):
#                     continue  # Estas posiciones deben tener torres
#                 self.assertIsNone(self.board.get_piece(row, col), f"Position ({row}, {col}) should be empty")

#     def test_initial_rook_positions(self):
#         """ Verifica que las torres están en las posiciones correctas. """
#         self.assertIsInstance(self.board.get_piece(0, 0), Piece)
#         self.assertIsInstance(self.board.get_piece(0, 7), Piece)
#         self.assertIsInstance(self.board.get_piece(7, 0), Piece)
#         self.assertIsInstance(self.board.get_piece(7, 7), Piece)

        
#         # Verifica que las torres tienen el color correcto
#         self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
#         self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
#         self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
#         self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")

# if __name__ == '__main__':
#     unittest.main()

#     import unittest
# from board import Board


# class TestBoard(unittest.TestCase):
#     def test_str_board(self):
#         board = Board()
#         self.assertEqual(
#             str(board),
#             (
#                 "♖      ♖\n"
#                 "        \n"
#                 "        \n"
#                 "        \n"
#                 "        \n"
#                 "        \n"
#                 "        \n"
#                 "♜      ♜\n"
#             )
#         )
#         from rook import Rook  # Se asume que hay una clase Rook
# from piece import Piece  # Clase base para las piezas

# class Board:
#     def __init__(self):
#         self.__positions__ = []  # Inicializa el tablero vacío
#         for _ in range(8):
#             col = []  # Crea una columna vacía
#             for _ in range(8):
#                 col.append(None)  # Agrega 8 espacios vacíos (None) a la columna
#             self.__positions__.append(col)  # Agrega la columna al tablero

#         # Coloca las torres (Rooks) en sus posiciones iniciales
#         self.__positions__[0][0] = Rook("BLACK", self)
#         self.__positions__[0][7] = Rook("BLACK", self)
#         self.__positions__[7][0] = Rook("WHITE", self)
#         self.__positions__[7][7] = Rook("WHITE", self)

#     def __str__(self):
#         board_str = ""
#         for row in self.__positions__:
#             for cell in row:
#                 if cell is not None:
#                     board_str += str(cell) + " "
#                 else:
#                     board_str += ". "  # Representa un espacio vacío con un punto
#             board_str += "\n"
#         return board_str

#     def get_piece(self, row, col):
#         if 0 <= row < 8 and 0 <= col < 8:
#             return self.__positions__[row][col]
#         else:
#             raise ValueError(f"Invalid position ({row}, {col}) on the board")

# # Esto verifica la correcta colocación de las piezas y el estado inicial del tablero

# import unittest
# from board import Board
# from rook import Rook

# class TestBoard(unittest.TestCase):
#     def setUp(self):
#         self.board = Board()

#     def test_empty_positions(self):
#         """ Verifica que todas las posiciones iniciales están vacías (None), excepto las posiciones de las torres. """
#         for row in range(8):
#             for col in range(8):
#                 if (row == 0 and col in [0, 7]) or (row == 7 and col in [0, 7]):
#                     continue  # Estas posiciones deben tener torres
#                 self.assertIsNone(self.board.get_piece(row, col), f"Position ({row}, {col}) should be empty")

#     def test_initial_rook_positions(self):
#         """ Verifica que las torres están en las posiciones correctas. """
#         self.assertIsInstance(self.board.get_piece(0, 0), Rook)
#         self.assertIsInstance(self.board.get_piece(0, 7), Rook)
#         self.assertIsInstance(self.board.get_piece(7, 0), Rook)
#         self.assertIsInstance(self.board.get_piece(7, 7), Rook)

#         # Verifica que las torres tienen el color correcto
#         self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
#         self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
#         self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
#         self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")

# if __name__ == '__main__':
#     unittest.main()

from piece import Piece
from rook import Rook
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King
from pawn import Pawn

class Board:
    def __init__(self):
        """Inicializa el tablero vacío y coloca las piezas en sus posiciones iniciales."""
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self._initialize_pieces()

    def _initialize_pieces(self):
        """Coloca todas las piezas en sus posiciones iniciales."""
        # Torres
        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)
        self.__positions__[7][0] = Rook("WHITE", self)
        self.__positions__[7][7] = Rook("WHITE", self)

        # Caballos
        self.__positions__[0][1] = Knight("BLACK", self)
        self.__positions__[0][6] = Knight("BLACK", self)
        self.__positions__[7][1] = Knight("WHITE", self)
        self.__positions__[7][6] = Knight("WHITE", self)

        # Alfiles
        self.__positions__[0][2] = Bishop("BLACK", self)
        self.__positions__[0][5] = Bishop("BLACK", self)
        self.__positions__[7][2] = Bishop("WHITE", self)
        self.__positions__[7][5] = Bishop("WHITE", self)

        # Reyes y Reinas
        self.__positions__[0][3] = Queen("BLACK", self)
        self.__positions__[0][4] = King("BLACK", self)
        self.__positions__[7][3] = Queen("WHITE", self)
        self.__positions__[7][4] = King("WHITE", self)

        # Peones
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)
            self.__positions__[6][col] = Pawn("WHITE", self)

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

    def get_piece(self, row, col):
        """Devuelve la pieza en una posición determinada."""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col]
        else:
            raise ValueError(f"Posición inválida: ({row}, {col})")

    def move_piece(self, from_row, from_col, to_row, to_col):
        """Mueve una pieza de una posición a otra si el movimiento es válido."""
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError(f"No hay ninguna pieza en la posición: ({from_row}, {from_col})")

        # Verificar si el movimiento es válido
        if piece.is_valid_move(to_row, to_col):
            self.__positions__[to_row][to_col] = piece
            self.__positions__[from_row][from_col] = None
            piece.update_position(to_row, to_col)
        else:
            raise ValueError("Movimiento no válido.")

    def is_position_empty(self, row, col):
        """Verifica si una posición está vacía."""
        return self.get_piece(row, col) is None
