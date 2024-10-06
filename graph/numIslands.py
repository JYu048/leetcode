from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(r, c):
            queue = deque([(r,c)])
            grid[r][c] = "0"
            
            while queue:
                (r, c) = queue.popleft()
                for i, j in [(0, 1), (0, -1), (-1, 0), (1,0)]:
                    new_r, new_c = r + i, j + c
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == "1":
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = "0"
        
        m, n = len(grid), len(grid[0]) 
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1": 
                    bfs(i, j)
                    res += 1
        
        return res
