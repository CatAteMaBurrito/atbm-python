userBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
def isValidChessBoard(board):
    # This part of the program checks that there is -
    # 1. Exactly one king of each color
    # 2. Each player can have at most 16 pieces
    # 3. At most 8 pawns
    # 4. Piece names begin with 'w' or 'b'
    whitePawns = 0
    whitePieces = 0
    blackPawns = 0
    blackPieces = 0
    whiteKingCount = 0
    blackKingCount = 0
    for value in board.values():
        if ('pawn' not in value and 'knight' not in value and 'bishop' not in value and 'rook' not in value and 'queen' not in value and 'king' not in value):
            return False

        if (value[0] == 'w'):
            whitePieces += 1
            if ('pawn' in value):
                whitePawns += 1
            if ('king' in value):
                whiteKingCount += 1
        elif (value[0] == 'b'):
            blackPieces += 1
            if ('pawn' in value):
                blackPawns += 1
            if ('king' in value):
                blackKingCount += 1
        else:
            return False
    if (whitePawns > 8 or blackPawns > 8):
        return False
    if (whitePieces > 16 or blackPieces > 16):
        return False
    if (whiteKingCount != 1 or blackKingCount != 1):
        return False
    
    # This part checks for valid places and piece names are valid
    for key in board.keys():
        if (int(key[0]) > 8 or int(key[0]) < 1):
            return False
        elif (key[1] > 'h' or key[1] < 'a'):
            return False

    return True
print(isValidChessBoard(userBoard))