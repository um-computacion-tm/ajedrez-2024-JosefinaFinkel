class InvalidInput(Exception):
    """Excepción para entradas inválidas en la CLI."""
    pass

class InvalidMove(Exception):
    """Clase base para movimientos inválidos."""
    pass

class InvalidMoveNoPiece(InvalidMove):
    """Movimiento inválido debido a la ausencia de una pieza en la posición inicial."""
    pass

class InvalidMoveSameColor(InvalidMove):
    """Movimiento inválido debido a que la pieza de destino es del mismo color."""
    pass

class InvalidMovePieceFromOtherColor(InvalidMove):
    """Movimiento inválido debido a que la pieza de destino es de otro color."""
    pass

class InvalidMoveNotInBoard(InvalidMove):
    """Movimiento inválido porque la posición de destino está fuera del tablero."""
    pass

class InvalidMovePathOcuppied(InvalidMove):
    """Movimiento inválido porque el camino hacia la posición de destino está ocupado."""
    pass

class InvalidMoveVertical(InvalidMove):
    """Movimiento inválido porque no es vertical."""
    pass

class InvalidMoveHorizontal(InvalidMove):
    """Movimiento inválido porque no es horizontal."""
    pass

class InvalidMoveVerticalHorizontal(InvalidMove):
    """Movimiento inválido porque no es ni vertical ni horizontal."""
    pass

class InvalidMoveDiagonal(InvalidMove):
    """Movimiento inválido porque no es diagonal."""
    pass

class InvalidMoveNotAllowed(InvalidMove):
    """Movimiento inválido porque no está permitido para la pieza."""
    pass

class InvalidMoveKnight(InvalidMove):
    """Movimiento inválido para un caballo."""
    pass

class InvalidMovePawn(InvalidMove):
    """Movimiento inválido para un peón."""
    pass

class InvalidMoveKing(InvalidMove):
    """Movimiento inválido para un rey."""
    pass

class InvalidMoveQueen(InvalidMove):
    """Movimiento inválido para una reina."""
    pass