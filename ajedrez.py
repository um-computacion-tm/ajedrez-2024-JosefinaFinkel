"""
from chess import Chess
from excepciones import InvalidMoveError, NotYourTurnError, OutOfBoundsError, PieceOccupiedError

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # Mostramos el tablero y el turno
        print(chess)
        print(f"Turn: {chess.get_turn()}")

        # Solicitamos las coordenadas del usuario
        from_row = int(input('From row: '))
        from_col = int(input('From col: '))
        to_row = int(input('To row: '))
        to_col = int(input('To col: '))

        # Realizamos el movimiento
        chess.move(from_row, from_col, to_row, to_col)

    except (InvalidMoveError, NotYourTurnError, OutOfBoundsError, PieceOccupiedError) as e:
        print(f"Error: {e}")
    except ValueError:
        print("Por favor, ingrese coordenadas válidas (números enteros).")

if __name__ == '__main__':
    main() """

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


if __name__ == '__main__':
    main()

