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
from excepciones import InvalidMove, InvalidTurn, NoPieceAtPosition, InvalidCoordinates, InvalidMoveDestination, InvalidMoveDiagonal, InvalidMoveVerticalHorizontal

# Clase de pruebas para el juego de ajedrez
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

    # Tests para movimientos de piezas
    def test_valid_rook_movement(self):
        """Prueba los movimientos válidos de la torre"""
        rook = Rook("WHITE")
        board = Board()
        self.assertTrue(rook.valid_moves(0, 0, 0, 5, board))  # Movimiento horizontal

    def test_invalid_rook_movement(self):
        """Prueba los movimientos inválidos de la torre"""
        rook = Rook("WHITE")
        board = Board()
        with self.assertRaises(InvalidMoveVerticalHorizontal):
            rook.valid_moves(0, 0, 2, 2, board)  # Movimiento inválido (no es en línea recta)

    # def test_valid_bishop_movement(self):
    #     """Prueba los movimientos válidos del alfil"""
    #     bishop = Bishop("WHITE")
    #     board = Board()
    #     self.assertTrue(bishop.valid_moves(0, 0, 2, 2, board))  # Movimiento diagonal

    # def test_invalid_bishop_movement(self):
    #     """Prueba los movimientos inválidos del alfil"""
    #     bishop = Bishop("WHITE")
    #     board = Board()
    #     with self.assertRaises(InvalidMoveDiagonal):
    #         bishop.valid_moves(0, 0, 0, 2, board)  # Movimiento inválido (no es diagonal)

    def test_valid_bishop_movement(self):
        """Prueba los movimientos válidos del alfil"""
        bishop = Bishop("WHITE")
        board = Board()

    # Limpiar el camino del alfil (por ejemplo, vaciar posiciones intermedias)
        board.__positions__[1][1] = None  # Limpia el peón u otra pieza en (1,1)

        # Ahora prueba el movimiento diagonal del alfil
        self.assertTrue(bishop.valid_moves(0, 0, 2, 2, board))  # Movimiento diagonal

    def test_invalid_bishop_movement(self):
        """Prueba los movimientos inválidos del alfil"""
        bishop = Bishop("WHITE")
        board = Board()
        with self.assertRaises(InvalidMoveDiagonal):
            bishop.valid_moves(0, 0, 0, 2, board)  # Movimiento inválido


    # Tests para las excepciones
    def test_no_piece_at_position(self):
        """Prueba que lance excepción cuando no hay pieza en una posición"""
        with self.assertRaises(NoPieceAtPosition):
            self.chess.move(0, 0, 0, 1)  # No hay pieza en esta posición
    
    def test_no_piece_at_position(self):
        """Prueba que lance excepción cuando no hay pieza en una posición"""
        with self.assertRaises(NoPieceAtPosition):
            self.chess.move(2, 2, 2, 3)  # No hay pieza en esta posición

    
    def test_invalid_turn(self):
        """Prueba el manejo de turnos inválidos"""
        with self.assertRaises(InvalidTurn):
            self.chess.move(6, 0, 5, 0)  # Intentar mover una pieza negra en el turno blanco

if __name__ == '__main__':
    unittest.main()

