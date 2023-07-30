from enum import Enum


class Squares(Enum):
    a1, b1, c1, d1, e1, f1, g1, h1 = 0, 1, 2, 3, 4, 5, 6, 7
    a2, b2, c2, d2, e2, f2, g2, h2 = 8, 9, 10, 11, 12, 13, 14, 15
    a3, b3, c3, d3, e3, f3, g3, h3 = 16, 17, 18, 19, 20, 21, 22, 23
    a4, b4, c4, d4, e4, f4, g4, h4 = 24, 25, 26, 27, 28, 29, 30, 31
    a5, b5, c5, d5, e5, f5, g5, h5 = 32, 33, 34, 35, 36, 37, 38, 39
    a6, b6, c6, d6, e6, f6, g6, h6 = 40, 41, 42, 43, 44, 45, 46, 47
    a7, b7, c7, d7, e7, f7, g7, h7 = 48, 49, 50, 51, 52, 53, 54, 55
    a8, b8, c8, d8, e8, f8, g8, h8 = 56, 57, 58, 59, 60, 61, 62, 63


class Colors(Enum):
    BLACK = 0
    WHITE = 1


class Pieces(Enum):
    PAWN = 0
    ROOK = 1
    NKNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5


bitboards = {
    (Pieces.PAWN,
     Colors.BLACK): 1 << Squares.a7.value | 1 << Squares.b7.value | 1 << Squares.c7.value | 1 << Squares.d7.value
                    | 1 << Squares.e7.value | 1 << Squares.f7.value
                    | 1 << Squares.g7.value | 1 << Squares.h7.value,
    (Pieces.ROOK, Colors.BLACK): 1 << Squares.a8.value | 1 << Squares.h8.value,
    (Pieces.NKNIGHT, Colors.BLACK): 1 << Squares.b8.value | 1 << Squares.g8.value,
    (Pieces.BISHOP, Colors.BLACK): 1 << Squares.c8.value | 1 << Squares.f8.value,
    (Pieces.QUEEN, Colors.BLACK): 1 << Squares.d8.value,
    (Pieces.KING, Colors.BLACK): 1 << Squares.e8.value,

    (Pieces.PAWN,
     Colors.WHITE): 1 << Squares.a2.value | 1 << Squares.b2.value | 1 << Squares.c2.value | 1 << Squares.d2.value
                    | 1 << Squares.e2.value | 1 << Squares.f2.value | 1 << Squares.g2.value | 1 << Squares.h2.value,
    (Pieces.ROOK, Colors.WHITE): 1 << Squares.a1.value | 1 << Squares.h1.value,
    (Pieces.NKNIGHT, Colors.WHITE): 1 << Squares.b1.value | 1 << Squares.g1.value,
    (Pieces.BISHOP, Colors.WHITE): 1 << Squares.c1.value | 1 << Squares.f1.value,
    (Pieces.QUEEN, Colors.WHITE): 1 << Squares.d1.value,
    (Pieces.KING, Colors.WHITE): 1 << Squares.e1.value,
}


# Example usage:
def print_board():
    for row in range(7, -1, -1):
        for col in range(8):
            square = Squares(8 * row + col)
            piece_found = False
            for (piece_type, piece_color), bitboard in bitboards.items():
                if bitboard & (1 << square.value):
                    piece_found = True
                    if piece_color == Colors.WHITE:
                        print(f"{piece_type.name[0]}", end="")
                    else:
                        print(f"{piece_type.name[0].lower()}", end="")
                    break
            if not piece_found:
                print(".", end="")
        print()


def move_piece(start_square, end_square):
    for (piece_type, piece_color), bitboard in bitboards.items():
        if bitboard & (1 << start_square.value):
            bitboards[(piece_type, piece_color)] ^= (1 << start_square.value)
            bitboards[(piece_type, piece_color)] |= (1 << end_square.value)
            break

while True:
    print_board()
    start_square = input("start square: ")
    end_square = input("end square: ")
    if start_square == "q":
        break
    move_piece(Squares[start_square], Squares[end_square])


