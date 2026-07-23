class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {(i, j): set() for i in range(3) for j in range(3)}

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                if val == '.':
                    continue
                
                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                if val in boxes[(i // 3, j // 3)]:
                    return False
                boxes[(i // 3, j // 3)].add(val)

        return True