
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