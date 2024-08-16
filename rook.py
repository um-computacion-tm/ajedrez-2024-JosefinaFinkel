class Piece:
     def __init__(self, color):
            self.__color__ = color


class Rook(Piece):
  def __init__(self, color):
       super().__init__(color)


class Pawn(Piece):
   def __init__(self, color):
       super().__init__(color)

        
class Bishop(Piece):
 ... 
       
class Knight(Piece):
  ...
        
class Queen(Piece):
   ...  
        
class King(Piece):
   ...


