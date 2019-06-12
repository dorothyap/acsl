# Name: Dorothy Philip
# 2018-2019 Contest #3
# Problem : ACSL Stretch Junior Division
# Language: Python 3.7.2

class Board(object):
    def __init__(self, rows, cols, blocked):
        self._rowCount = rows
        self._columnCount = cols
        self._cell = [[False for j in range(self._columnCount)] for i in range(self._rowCount)]
        for x in blocked :
            x = x -1
            r = int(x / cols)
            c = x % cols
            self._cell[r][c] = True
        self._pieces = []
        self._positions = []

    def getPath(self) :
        return ''.join(self._pieces)

    def cellsForPiece(self, row, col, piece) :
        if piece == 'A' :
            return [(row, col), (row, col + 1), (row, col + 2)]
        elif piece == 'B' :
            return [(row, col), (row+1, col), (row+1, col+1)]
        elif piece == 'C' :
            return [(row, col), (row, col+1), (row+1, col+1), (row+2, col+1)]
        return

    def fillCellsForPiece(self, row, col, piece, value) :
        if piece == 'A' :
            self._cell[row][col] = value
            self._cell[row][col + 1] = value
            self._cell[row] [col + 2] = value
        elif piece == 'B' :
            self._cell[row][col] = value
            self._cell[row + 1][col] = value
            self._cell[row + 1] [col + 1] = value
        elif piece == 'C' :
            self._cell[row][col] = value
            self._cell[row][col + 1] = value
            self._cell[row + 1] [col + 1] = value
            self._cell[row + 2] [col + 1] = value

    def nextCellAfterPiece(Self, row, col, piece) :
        if piece == 'A' :
            return (row, col + 3)
        elif piece == 'B' :
            return (row + 1, col + 2)
        elif piece == 'C' :
            return (row + 2, col + 2)

    def canPlacePiece(self, row, col, piece) :
        options = self.cellsForPiece(row, col, piece)
        for (r, c) in options :
            if r < 0 or r >= self._rowCount :
                return False
            if c < 0 or c >= self._columnCount :
                return False
            if (self._cell[r][c] == True) :
                return False
            if piece == 'B' and c == 0 :
                return False
            if piece == 'C' and c == self._columnCount - 1 :
                return False
        return True

    def nextPiece(self, piece):
        if piece == 'A' :
            return 'B' 
        elif piece == 'B' :
            return 'C'
        elif piece == 'C' :
            return 'A' 

    def nextPositionAfterPlacement(self, r, c, piece) :
        position = None
        if self.canPlacePiece(r, c, piece) :
            self._pieces.append(piece)
            self._positions.append((r, c,))
            self.fillCellsForPiece(r, c, piece, True)
            position = self.nextCellAfterPiece(r, c, piece)
        return position
    
    def undoLastMove(self, piece) :
        (r, c) = self._positions.pop()
        self.fillCellsForPiece(r, c, piece, False)
        return

    def place(self, r, c, piece, count) :
        if (c >= self._columnCount) :
            return
        if count >= 3 :
            l = len(self._pieces)
            if (l==0) :
                return
            piece = self._pieces.pop()
            self.undoLastMove(piece)
            count = 0
        elif self.canPlacePiece(r, c, piece) :
            self._pieces.append(piece)
            self._positions.append((r, c))
            self.fillCellsForPiece(r, c, piece, True)
            (r, c) = self.nextCellAfterPiece(r, c, piece)
            count = 0
        else :
            count = count + 1
        self.place(r, c, self.nextPiece(piece), count)

    def placeAll(self, start) :
        start = start - 1
        r = int(start / self._columnCount)
        c = start % self._columnCount
        self.place(r, c, 'A', 0)
        return self._pieces

boards = []
for i in range(5) :
    data = input().split()
    r = int(data[0])
    c = int(data[1])
    s = int(data[2])
    n = int(data[3])
    blocked = []
    j = 4
    for i in range(n) :
        blocked.append(int (data[j]))
        j = j +  1
    board = Board(r, c, blocked)
    board.placeAll(s)
    boards.append(board)

for b in boards :
    print(b.getPath())
        
            
    


