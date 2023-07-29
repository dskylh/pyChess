class Tile:
    def __init__(self, curr_piece=None):
        self.curr_piece = curr_piece

    def remove_piece(self):
        self.curr_piece = None
