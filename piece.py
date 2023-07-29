from enum import Enum


class Color(Enum):
    BLACK = 0
    WHITE = 1


class Piece:
    def __init__(self, position, color=Color.WHITE):
        self.color: Color = color
        self.position = position

    def move(self, new_position):
        self.position = new_position
        if self.position.curr_piece is not None:
            self.position.remove_piece()


class Pawn(Piece):
    def __init__(self, position, color=Color.WHITE):
        super().__init__(position, color)
        self.name = 'P'

    def __str__(self):
        return self.name 


class Rook(Piece):
    def __init__(self, position, color=Color.WHITE):
        super().__init__(position, color)
        self.name = 'R'

    def __str__(self):
        return self.name 


class Knight(Piece):
    def __init__(self, position, color=Color.WHITE):
        super().__init__(position, color)
        self.name = 'N'

    def __str__(self):
        return self.name 


class Bishop(Piece):
    def __init__(self, position, color=Color.WHITE):
        super().__init__(position, color)
        self.name = 'B'

    def __str__(self):
        return self.name 


class Queen(Piece):
    def __init__(self, position, color=Color.WHITE):
        super().__init__(position, color)
        self.name = 'Q'

    def __str__(self):
        return self.name 


class King(Piece):
    def __init__(self, position, color=Color.WHITE):
        super().__init__(position, color)
        self.name = 'K'

    def __str__(self):
        return self.name 


import tile
