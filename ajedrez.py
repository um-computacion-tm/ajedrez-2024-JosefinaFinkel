
from chess import Chess
from excepciones import InvalidMove, InvalidTurn, InvalidCoordinates, NoPieceAtPosition, InvalidMoveDestination

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # Mostramos el tablero y el turno
        print(chess)
        print(f"Turno: {chess.get_turn()}")

        # Solicitamos las coordenadas del usuario
        from_row = int(input('Desde fila: '))
        from_col = int(input('Desde columna: '))
        to_row = int(input('Hasta fila: '))
        to_col = int(input('Hasta columna: '))

        # Realizamos el movimiento
        chess.move(from_row, from_col, to_row, to_col)

    except (InvalidMove, InvalidTurn, InvalidCoordinates, NoPieceAtPosition, InvalidMoveDestination) as e:
        print(f"Error: {e}")
    except ValueError:
        print("Por favor, ingrese coordenadas válidas (números enteros).")


# Test para ajedrez.py
def test_play_valid_move(self, mock_input):
        """Prueba que un movimiento válido se realice correctamente en ajedrez.py"""
        chess = Chess()
        play(chess)  # Simula una jugada en el juego
        self.assertEqual(chess.get_board().__positions__[1][0], chess.get_board().__positions__[0][0])  # Verifica que el peón se haya movido

    
def test_play_invalid_coordinates(self, mock_input):
        """Prueba que se manejen correctamente las coordenadas inválidas en ajedrez.py"""
        chess = Chess()
        with self.assertRaises(InvalidCoordinates):
            play(chess)  # Intentar mover con coordenadas fuera de rango




if __name__ == '__main__':
    main()

