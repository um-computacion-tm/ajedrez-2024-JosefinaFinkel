# import unittest
# from rook import Rook
# from knight import Knight
# from bishop import Bishop
# from queen import Queen
# from king import King
# from pawn import Pawn
# from board import Board
# from chess import Chess
# from movimientos import ReglasDeMovimientos
# from excepciones import InvalidMove, InvalidTurn, NoPieceAtPosition, InvalidCoordinates, InvalidMoveDestination, InvalidMoveDiagonal, InvalidMoveVerticalHorizontal
# from chess import Chess
# from excepciones import InvalidMovePawn, InvalidTurn
# # Clase de pruebas para el juego de ajedrez
# class TestChessGame(unittest.TestCase):
    
#     def setUp(self):
#         """Inicializa una partida de ajedrez nueva para cada test"""
#         self.chess = Chess()

#     # Tests para la clase Chess
#     def test_turn_initial(self):
#         """Verifica que el turno inicial sea de las blancas"""
#         self.assertEqual(self.chess.get_turn(), "WHITE")
    
#     def test_change_turn(self):
#         """Verifica el cambio de turno"""
#         self.chess.change_turn()
#         self.assertEqual(self.chess.get_turn(), "BLACK")

#     def test_invalid_coordinates(self):
#         """Prueba el manejo de coordenadas fuera de rango"""
#         with self.assertRaises(InvalidCoordinates):
#             self.chess.move(8, 0, 9, 0)  # Movimiento fuera del rango del tablero


#     def test_valid_rook_movement(self):
#         """Prueba los movimientos válidos de la torre"""
#         rook = Rook("WHITE")
#         board = Board()

#         # Limpiar el camino de la torre en la fila 0
#         for col in range(1, 5):  # Limpiar las posiciones de (0,1) a (0,4)
#             board.__positions__[0][col] = None

#         # Ahora prueba el movimiento horizontal de la torre
#         self.assertTrue(rook.valid_moves(0, 0, 0, 5, board))  # Movimiento horizontal

#     def test_invalid_rook_movement(self):
#         """Prueba los movimientos inválidos de la torre"""
#         rook = Rook("WHITE")
#         board = Board()

#         # El movimiento inválido no necesita cambios, ya que es diagonal y siempre inválido para la torre
#         with self.assertRaises(InvalidMoveVerticalHorizontal):
#             rook.valid_moves(0, 0, 2, 2, board)  # Movimiento inválido (no es en línea recta)


#     def test_valid_bishop_movement(self):
#         """Prueba los movimientos válidos del alfil"""
#         bishop = Bishop("WHITE")
#         board = Board()

#     # Limpiar el camino del alfil (por ejemplo, vaciar posiciones intermedias)
#         board.__positions__[1][1] = None  # Limpia el peón u otra pieza en (1,1)

#         # Ahora prueba el movimiento diagonal del alfil
#         self.assertTrue(bishop.valid_moves(0, 0, 2, 2, board))  # Movimiento diagonal

#     def test_invalid_bishop_movement(self):
#         """Prueba los movimientos inválidos del alfil"""
#         bishop = Bishop("WHITE")
#         board = Board()
#         with self.assertRaises(InvalidMoveDiagonal):
#             bishop.valid_moves(0, 0, 0, 2, board)  # Movimiento inválido


#     # Tests para las excepciones
#     def test_no_piece_at_position(self):
#         """Prueba que lance excepción cuando no hay pieza en una posición"""
#         with self.assertRaises(NoPieceAtPosition):
#             self.chess.move(0, 0, 0, 1)  # No hay pieza en esta posición
    
#     def test_no_piece_at_position(self):
#         """Prueba que lance excepción cuando no hay pieza en una posición"""
#         with self.assertRaises(NoPieceAtPosition):
#             self.chess.move(2, 2, 2, 3)  # No hay pieza en esta posición

# #nuevos 

#     def test_valid_pawn_movement_white(self):
#         """Prueba movimientos válidos de peones blancos"""
#         self.chess.move(1, 0, 3, 0)  # Primer movimiento de dos casillas
#         self.chess.move(6, 0, 4, 0)  # Mover peón negro dos casillas
#         self.chess.move(3, 0, 4, 0)  # Movimiento de una casilla hacia adelante

#     def test_invalid_pawn_movement_white(self):
#         """Prueba movimientos inválidos de peones blancos"""
#         with self.assertRaises(InvalidMovePawn):
#             self.chess.move(1, 0, 4, 0)  # Intentar mover tres casillas
        
#         with self.assertRaises(InvalidMovePawn):
#             self.chess.move(1, 0, 2, 1)  # Intentar mover en diagonal sin captura

#     def test_invalid_turn(self):
#         """Prueba el manejo de turnos inválidos"""
#         self.chess.move(1, 0, 3, 0)  # Peón blanco avanza
#         self.assertEqual(self.chess.get_turn(), "BLACK")  # Verifica que el turno cambió
#         with self.assertRaises(InvalidTurn):
#             self.chess.move(1, 1, 3, 1)  # Intentar mover peón blanco en el turno negro


# if __name__ == '__main__':
#     unittest.main()


import unittest
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
from board import Board
from chess import Chess
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMove, InvalidTurn, NoPieceAtPosition, InvalidCoordinates, InvalidMovePawn, InvalidTurn, InvalidMoveDiagonal, InvalidMoveVerticalHorizontal

class TestChessGame(unittest.TestCase):
    
    def setUp(self):
        """Inicializa una partida de ajedrez nueva para cada test"""
        self.chess = Chess()

    # Tests para la clase Chess
    def test_turn_initial(self):
        """Verifica que el turno inicial sea de las blancas"""
        self.assertEqual(self.chess.get_turn(), "WHITE")
    
    def test_change_turn(self):
        """Verifica el cambio de turno"""
        self.chess.change_turn()
        self.assertEqual(self.chess.get_turn(), "BLACK")

    def test_invalid_coordinates(self):
        """Prueba el manejo de coordenadas fuera de rango"""
        with self.assertRaises(InvalidCoordinates):
            self.chess.move(8, 0, 9, 0)  # Movimiento fuera del rango del tablero

    def test_valid_rook_movement(self):
        """Prueba los movimientos válidos de la torre"""
        rook = Rook("WHITE")
        board = Board()

        # Limpiar el camino de la torre en la fila 0
        for col in range(1, 5):  # Limpiar las posiciones de (0,1) a (0,4)
            board.__positions__[0][col] = None

        # Ahora prueba el movimiento horizontal de la torre
        self.assertTrue(rook.valid_moves(0, 0, 0, 5, board))  # Movimiento horizontal

    def test_invalid_rook_movement(self):
        """Prueba los movimientos inválidos de la torre"""
        rook = Rook("WHITE")
        board = Board()

        # Como se intenta mover a una posición no válida
        with self.assertRaises(InvalidMoveVerticalHorizontal):
            rook.valid_moves(0, 0, 1, 1, board)  # Movimiento diagonal inválido


    def test_valid_bishop_movement(self):
        """Prueba los movimientos válidos del alfil"""
        bishop = Bishop("WHITE")
        board = Board()

        # Limpiar el camino del alfil (por ejemplo, vaciar posiciones intermedias)
        board.__positions__[1][1] = None  # Limpia el peón u otra pieza en (1,1)

        # Ahora prueba el movimiento diagonal del alfil
        self.assertTrue(bishop.valid_moves(0, 0, 2, 2, board))  # Movimiento diagonal válido

    def test_invalid_bishop_movement(self):
        """Prueba los movimientos inválidos del alfil"""
        bishop = Bishop("WHITE")
        board = Board()

        # Suponiendo que hay piezas en el camino que bloquean el movimiento
        board.__positions__[1][1] = Pawn("BLACK")  # Ocupando (1,1)

        with self.assertRaises(InvalidMoveDiagonal):
            bishop.valid_moves(0, 0, 2, 2, board)  # Movimiento diagonal que está bloqueado

    # Tests para las excepciones
    def test_no_piece_at_position(self):
        """Prueba que lance excepción cuando no hay pieza en una posición"""
        with self.assertRaises(NoPieceAtPosition):
            self.chess.move(0, 0, 0, 1)  # No hay pieza en esta posición
    
        with self.assertRaises(NoPieceAtPosition):
            self.chess.move(2, 2, 2, 3)  # No hay pieza en esta posición

    # Nuevos tests

    def test_valid_pawn_movement_white(self):
        """Prueba movimientos válidos de peones blancos"""
        self.chess.move(1, 0, 3, 0)  # Primer movimiento de dos casillas
        self.chess.move(6, 0, 4, 0)  # Mover peón negro dos casillas
        self.chess.move(3, 0, 4, 0)  # Movimiento de una casilla hacia adelante

    def test_invalid_pawn_movement_white(self):
        """Prueba movimientos inválidos de peones blancos"""
        with self.assertRaises(InvalidMovePawn):
            self.chess.move(1, 0, 4, 0)  # Intentar mover tres casillas
        
        with self.assertRaises(InvalidMovePawn):
            self.chess.move(1, 0, 2, 1)  # Intentar mover en diagonal sin captura

    def test_invalid_turn(self):
        """Prueba el manejo de turnos inválidos"""
        self.chess.move(1, 0, 3, 0)  # Peón blanco avanza
        self.assertEqual(self.chess.get_turn(), "BLACK")  # Verifica que el turno cambió
        with self.assertRaises(InvalidTurn):
            self.chess.move(1, 1, 3, 1)  # Intentar mover peón blanco en el turno negro


if __name__ == '__main__':
    unittest.main()
