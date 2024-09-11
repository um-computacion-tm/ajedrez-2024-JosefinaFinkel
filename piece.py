

class Piece:
     def __init__(self, color, board):
            self.__color__ = color
            self.__board__ = board

def __str__(self):
   if self.__color__ == 'white':
       return self.white_str()
   else:
       return self.black_str()
   
def can_move(self, start_pos, end_pos, board):
    # verificar si la pieza puede moverse de start_pos a end_pos
    pass

   
class Rook(Piece):
 ...

  
class Pawn(Piece):
    ...

        
class Bishop(Piece):
   ...
       
class Knight(Piece):
   ...
        
class Queen(Piece):
   ...  
        
class King(Piece):
   ...


