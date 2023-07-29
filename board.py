import piece
import tile


class Board():
    def __init__(self):
        self.tiles: list[list[tile.Tile]] = [[tile.Tile() for _ in range(8)] for _ in range(8)]

    def populate_board(self):
        for i in range(8):
            self.tiles[1][i].curr_piece = piece.Pawn(self.tiles[1][i], piece.Color.BLACK)
            self.tiles[6][i].curr_piece = piece.Pawn(self.tiles[6][i], piece.Color.WHITE)
        self.tiles[0][0].curr_piece = piece.Rook(self.tiles[0][0], piece.Color.BLACK)
        self.tiles[0][7].curr_piece = piece.Rook(self.tiles[0][7], piece.Color.BLACK)
        self.tiles[7][0].curr_piece = piece.Rook(self.tiles[7][0], piece.Color.WHITE)
        self.tiles[7][7].curr_piece = piece.Rook(self.tiles[7][7], piece.Color.WHITE)
        self.tiles[0][1].curr_piece = piece.Knight(self.tiles[0][1], piece.Color.BLACK)
        self.tiles[0][6].curr_piece = piece.Knight(self.tiles[0][6], piece.Color.BLACK)
        self.tiles[7][1].curr_piece = piece.Knight(self.tiles[7][1], piece.Color.WHITE)
        self.tiles[7][6].curr_piece = piece.Knight(self.tiles[7][6], piece.Color.WHITE)
        self.tiles[0][2].curr_piece = piece.Bishop(self.tiles[0][2], piece.Color.BLACK)
        self.tiles[0][5].curr_piece = piece.Bishop(self.tiles[0][5], piece.Color.BLACK)
        self.tiles[7][2].curr_piece = piece.Bishop(self.tiles[7][2], piece.Color.WHITE)
        self.tiles[7][5].curr_piece = piece.Bishop(self.tiles[7][5], piece.Color.WHITE)
        self.tiles[0][3].curr_piece = piece.Queen(self.tiles[0][3], piece.Color.BLACK)
        self.tiles[7][3].curr_piece = piece.Queen(self.tiles[7][3], piece.Color.WHITE)
        self.tiles[0][4].curr_piece = piece.King(self.tiles[0][4], piece.Color.BLACK)
        self.tiles[7][4].curr_piece = piece.King(self.tiles[7][4], piece.Color.WHITE)

    def print_board(self):
        for i in range(8):
            for j in range(8):
                if self.tiles[i][j].curr_piece is None:
                    print('*', end=' ')
                else:
                    print(str(self.tiles[i][j].curr_piece), end=' ')
            print()
