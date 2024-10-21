


# from board import Board
# from movimientos import ReglasDeMovimientos
# from execpciones import *

# class Chess:
#     def __init__(self):
#         self.__board__ = Board()
#         self.__turn__ = "white"
#         self.__movimientos__ = ReglasDeMovimientos()

#     def move(self, from_row, from_col, to_row, to_col):
#         # Validar que las coordenadas estén dentro del rango del tablero
#         if not (0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7):
#             raise InvalidCoordinates("Coordenadas fuera del rango del tablero")

#         # Obtener la pieza de la posición de origen
#         piece = self.__board__.get_piece(from_row, from_col)

#         # Validar que haya una pieza en la posición inicial
#         if piece is None:
#             raise NoPieceAtPosition("No hay una pieza en las coordenadas de origen")

#         # Validar si la pieza pertenece al jugador que tiene el turno
#         if (piece.get_color() == "white" and self.__turn__ != "white") or (piece.get_color() == "black" and self.__turn__ != "black"):
#             raise InvalidTurn("No es el turno de la pieza seleccionada")

#         # Validar si el movimiento es válido según las reglas de la pieza
#         try:
#             piece.valid_moves(from_row, from_col, to_row, to_col)
#         except InvalidMove as e:
#             raise e  # Capturar y propagar la excepción si el movimiento no es válido

#         # Obtener la pieza en la posición de destino
#         destination_piece = self.__board__.get_piece(to_row, to_col)

#         # Verificar que la posición de destino no tenga una pieza del mismo color
#         if destination_piece and destination_piece.get_color() == piece.get_color():
#             raise InvalidMoveDestination("No se puede mover a una posición ocupada por una pieza del mismo color")

#         # Mover la pieza en el tablero
#         self.__board__.move_piece(from_row, from_col, to_row, to_col)

#         # Cambiar turno después del movimiento
#         self.change_turn()

#     def change_turn(self):
#         self.__turn__ = "black" if self.__turn__ == "white" else "white"



from board import Board
from movimientos import ReglasDeMovimientos
from excepciones import InvalidMove, InvalidTurn, NoPieceAtPosition, InvalidCoordinates, InvalidMoveDestination

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__movimientos__ = ReglasDeMovimientos()

    def move(self, from_row, from_col, to_row, to_col):
        """Realiza un movimiento de una pieza si es válido"""
        
        # Validar que las coordenadas estén dentro del rango del tablero
        if not self.__board__.valid_position(from_row, from_col) or not self.__board__.valid_position(to_row, to_col):
            raise InvalidCoordinates("Coordenadas fuera del rango del tablero")

        # Obtener la pieza de la posición de origen
        piece = self.__board__.get_piece(from_row, from_col)

        # Validar que haya una pieza en la posición inicial
        if piece is None:
            raise NoPieceAtPosition("No hay una pieza en las coordenadas de origen")

        # Depuración
        print(f"Turno actual: {self.get_turn()}, Color de la pieza: {piece.get_color()}")  

        # Validar si la pieza pertenece al jugador que tiene el turno
        if piece.get_color() != self.get_turn():
            raise InvalidTurn(f"No es el turno de {self.get_turn()}")

        # Validar si el movimiento es válido según las reglas de la pieza
        if not piece.valid_moves(from_row, from_col, to_row, to_col, self.__board__):
            raise InvalidMove("Movimiento inválido según las reglas de la pieza")

        # Verificar que la posición de destino no tenga una pieza del mismo color
        destination_piece = self.__board__.get_piece(to_row, to_col)
        if destination_piece and destination_piece.get_color() == piece.get_color():
            raise InvalidMoveDestination("No se puede mover a una posición ocupada por una pieza del mismo color")

        # Mover la pieza en el tablero
        self.__board__.move_piece(from_row, from_col, to_row, to_col)

        # Cambiar turno solo si el movimiento fue exitoso
        self.change_turn()

    def change_turn(self):
        """Cambia el turno del jugador"""
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def get_turn(self):
        """Devuelve el color del jugador que tiene el turno actual"""
        return self.__turn__

    def __str__(self):
        """Devuelve una representación en cadena del estado del tablero"""
        return str(self.__board__)
    
    def get_board(self):
        """Devuelve el tablero"""
        return self.__board__