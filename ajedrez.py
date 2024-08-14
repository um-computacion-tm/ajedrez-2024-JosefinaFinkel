from chess import Chess 
#aca importamos la clase chess

def main():
    chess = chess()
    while True:
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        from_row = int(input('From row: '))
        from_col = int(input('From col: '))
        to_row = int(input('To row: '))
        to_col = int(input('To col: '))

        chess.move(from_row, from_col, to_row, to_col)

    except Exception as e: #podemos aclarar las excepciones que queramos poner: "no es una posición válida", "no es tu turno", etc.
        print("error")

if __name__ == '__main__':
    main()
#