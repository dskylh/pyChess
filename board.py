from enum import Enum

from piece import Piece


class Board():
    def __init__(self):
        self.tiles: list[list[Tile]] = []

    def populate_board(self):



class Tile():
    def __init__(self):
        self.piece: Piece


class Color(Enum):
    BLACK = 0
    WHITE = 1