


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

    # Métodos para probar coordenadas inválidas
    def _test_raises_exception(self, exception_type, start, end):
        """Prueba que lance la excepción especificada al mover una pieza."""
        with self.assertRaises(exception_type):
            self.chess.move(start[0], start[1], end[0], end[1])

    def test_invalid_coordinates_out_of_bounds(self):
        """Prueba el manejo de coordenadas fuera de rango"""
        self._test_raises_exception(InvalidCoordinates, (8, 0), (9, 0))

    def test_invalid_coordinates_other_case(self):
        """Prueba otro caso de coordenadas inválidas"""
        self._test_raises_exception(InvalidCoordinates, (-1, 0), (0, 0))  # Movimiento fuera del rango del tablero

    # Métodos para probar movimientos de piezas
    def _test_valid_piece_movement(self, piece_class, start_position, end_position):
        """Prueba los movimientos válidos de una pieza"""
        piece = piece_class("WHITE")
        board = Board()

        # Limpiar el camino de la pieza en la posición inicial
        board.__positions__[start_position[0]][start_position[1]] = piece

        # Verifica que el movimiento es válido
        self.assertTrue(piece.valid_moves(start_position[0], start_position[1], end_position[0], end_position[1], board))

    def test_valid_rook_movement(self):
        """Prueba los movimientos válidos de la torre"""
        rook = Rook("WHITE")
        board = Board()

        # Limpia el camino de la torre en la fila 0
        for col in range(1, 5):  # Limpiar las posiciones de (0,1) a (0,4)
            board.__positions__[0][col] = None  # Asegúrate de que estas posiciones estén vacías
        board.__positions__[0][0] = rook  # Coloca la torre en la posición inicial

        # Ahora prueba el movimiento horizontal de la torre
        self.assertTrue(rook.valid_moves(0, 0, 0, 5, board))  # Movimiento horizontal

    def test_valid_bishop_movement(self):
        """Prueba los movimientos válidos del alfil"""
        bishop = Bishop("WHITE")
        board = Board()

        # Limpia la posición de (1, 1) para que el movimiento diagonal sea válido
        board.__positions__[1][1] = None  # Asegúrate de que no haya ninguna pieza bloqueando el camino
        board.__positions__[0][0] = bishop  # Coloca el alfil en la posición inicial

        self.assertTrue(bishop.valid_moves(0, 0, 2, 2, board))  # Movimiento diagonal válido

    def test_valid_king_movement(self):
        """Prueba los movimientos válidos del rey"""
        self._test_valid_piece_movement(King, (0, 4), (1, 5))  # Ejemplo de posiciones

    def test_valid_knight_movement(self):
        """Prueba los movimientos válidos del caballo"""
        self._test_valid_piece_movement(Knight, (0, 1), (2, 0))  # Ejemplo de posiciones

    # Métodos para manejar excepciones de piezas
    def test_no_piece_at_position_1(self):
        """Prueba que lance excepción cuando no hay pieza en una posición"""
        self.chess.get_board().__positions__[0][0] = None  # Asegúrate de que la posición esté vacía
        self._test_raises_exception(NoPieceAtPosition, (0, 0), (0, 1))

    def test_no_piece_at_position_2(self):
        """Prueba que lance excepción cuando no hay pieza en otra posición"""
        self._test_raises_exception(NoPieceAtPosition, (2, 2), (2, 3))

    # Nuevos tests para peones
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
