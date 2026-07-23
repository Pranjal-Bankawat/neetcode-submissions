class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        def makeRotten(r, c):
            nonlocal fresh
            if(r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 1):
                grid[r][c] = 2
                q.append([r, c])
                fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                makeRotten(r + 1, c)
                makeRotten(r - 1, c)
                makeRotten(r, c + 1)
                makeRotten(r, c - 1)
            time += 1
        return time if fresh == 0 else -1