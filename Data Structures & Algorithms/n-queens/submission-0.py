class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posiDiag = set() # r+c
        negiDiag = set() # r-c

        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                b = ["".join(row) for row in board]
                res.append(b[:])
            
            for c in range(n):
                if c in cols or (r+c) in posiDiag or (r-c) in negiDiag:
                    continue
                cols.add(c)
                posiDiag.add(r+c)
                negiDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                cols.remove(c)
                posiDiag.remove(r+c)
                negiDiag.remove(r-c)
                board[r][c] = '.'
        backtrack(0)
        return res
