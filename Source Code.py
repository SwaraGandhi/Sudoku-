class Solution(object):
    def isValidSudoku(self, board):
        # Check rows
        for row in board:
            visited = set()
            for val in row:
                if val != '.':
                    if val in visited: return False
                    visited.add(val)

        # Check cols
        for j in xrange(9):
            visited = set()
            for i in xrange(9):
                val = board[i][j]
                if val != '.':
                    if val in visited: return False
                    visited.add(val)
    
        # Check grids
        for rowStart in xrange(0, 7, 3):
            for colStart in xrange(0, 7, 3):
                visited = set()
                for i in xrange(rowStart, rowStart+3):
                    for j in xrange(colStart, colStart+3):
                        val = board[i][j]
                        if val != '.':
                            if val in visited: return False
                            visited.add(val)

        return True
