from piece import Piece

class Board:
    def __init__(self):
        self.__positions__ = [] # Inicializa el tablero vacío
        for _ in range(8):
            col = [] # Crea una columna vacía
            for _ in range(8):
                col.append(None) # Agrega 8 espacios vacíos (None) a la columna
            self.__positions__.append(col) # Agrega la columna al tablero 

        # Coloca las torres en sus posiciones iniciales
        self.__positions__[0][0] = Piece("BLACK", self) # Black
        self.__positions__[0][7] = Piece("BLACK", self) # Black
        self.__positions__[7][7] = Piece("WHITE", self) # White
        self.__positions__[7][0] = Piece("WHITE", self) # White
    

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__[row][col] #dentro de los corchetes, deberia ir los numeros del 1 al 7
        

#esto es el tablero 8x8, cada posición tiene un valor de None, o un número de 1 a 8.
#columna (col): {none, none, none, none, none, none, none, none}
#posición {col, col, col, col, col, col, col, col}
#fila (row): {none, none, none, none, none, none, none, none}

import unittest
from board import Board
from piece import Piece

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_empty_positions(self):
        """ Verifica que todas las posiciones iniciales están vacías (None), excepto las posiciones de las torres. """
        for row in range(8):
            for col in range(8):
                if (row == 0 and col in [0, 7]) or (row == 7 and col in [0, 7]):
                    continue  # Estas posiciones deben tener torres
                self.assertIsNone(self.board.get_piece(row, col), f"Position ({row}, {col}) should be empty")

    def test_initial_rook_positions(self):
        """ Verifica que las torres están en las posiciones correctas. """
        self.assertIsInstance(self.board.get_piece(0, 0), Piece)
        self.assertIsInstance(self.board.get_piece(0, 7), Piece)
        self.assertIsInstance(self.board.get_piece(7, 0), Piece)
        self.assertIsInstance(self.board.get_piece(7, 7), Piece)

        
        # Verifica que las torres tienen el color correcto
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
        self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
        self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")

if __name__ == '__main__':
    unittest.main()

    import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖      ♖\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♜      ♜\n"
            )
        )