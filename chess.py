
from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "white"

    def move(
        self,
        from_row, 
        from_col, 
        to_row,
        to_col):
        ...
        #validar coordenadas  
        piece = self.board.get_piece(from_row, from_col)
        self.change_turn()

        self.change_turn()
    def change_turn(self):
        if self.__turn__ == "white":
            self.__turn__ = "black"
        else:
            self.__turn__ = "white"
            

from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "white"

    def move(
        self,
        from_row, 
        from_col, 
        to_row,
        to_col):
        # Validar que las coordenadas estén dentro del rango del tablero
        if not (0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7):
            raise ValueError("Coordenadas fuera del rango del tablero")

        # Obtener la pieza de la posición de origen
        piece = self.__board__.get_piece(from_row, from_col)

        # Validar que haya una pieza en la posición inicial
        if piece is None:
            raise ValueError("No hay una pieza en las coordenadas de origen")

        # Validar si la pieza pertenece al jugador que tiene el turno
        if (piece.color == "white" and self.__turn__ != "white") or (piece.color == "black" and self.__turn__ != "black"):
            raise ValueError("No es el turno de la pieza seleccionada")

        # Validar si el movimiento es válido según las reglas de la pieza
        if not piece.is_valid_move(to_row, to_col):
            raise ValueError("Movimiento no válido para esta pieza")

        # Mover la pieza en el tablero
        self.__board__.move_piece(from_row, from_col, to_row, to_col)

        # Cambiar turno después del movimiento
        self.change_turn()

    def change_turn(self):
        if self.__turn__ == "white":
            self.__turn__ = "black"
        else:
            self.__turn__ = "white"
