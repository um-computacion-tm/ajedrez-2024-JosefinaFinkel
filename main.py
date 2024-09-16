def suma(a,b):
    return a + b

if __name__ == '__main__':
    print(suma(1,2))

# from chess import Chess

# def main():
#     chess = Chess()  # Corregido: usar Chess() en lugar de chess()
#     while True:
#         play(chess)

# def play(chess):
#     try:
#         print(chess.get_board())  # Mostrar el estado del tablero usando el nuevo método
#         print("Turno:", chess.get_turn())  # Mostrar el turno actual usando el nuevo método
#         from_row = int(input('Desde fila: '))
#         from_col = int(input('Desde columna: '))
#         to_row = int(input('Hasta fila: '))
#         to_col = int(input('Hasta columna: '))

#         chess.move(from_row, from_col, to_row, to_col)

#     except Exception as e:
#         print("Error:", e)

# if __name__ == '__main__':
#     main()
