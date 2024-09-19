from chess import Chess

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

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()


