from board import Color, Tile


class Piece():
    def __init__(self, position: Tile, color=Color.WHITE):
        self.color: Color = color
        self.position: Tile = position

    def move(self, new_position: Tile):
        self.position = new_position


class Pawn(Piece):
    def __init__(self, position: Tile, color=Color.WHITE):
        super().__init__(position, color)
        self.name = 'P'




    def __str__(self):
        return self.name + str(self.position)
