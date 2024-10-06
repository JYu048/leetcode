class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        def bfs(r, c):
            queue = collections.deque([(r,c)])
            grid[r][c] = 0
            area = 1

            while queue:
                x, y = queue.popleft()

                for i, j in [(0, 1), (0, -1), (1,0), (-1,0)]:
                    new_x, new_y = x + i, y + j

                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 0
                        area += 1
            
            return area
        
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    area = bfs(i, j)
                    res = max(area, res)
        
        return res

