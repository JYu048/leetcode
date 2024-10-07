from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Loop in 4 directions: right, down, left, up.
        Change direction upon encountering a visited node or reaching the matrix boundary.
        """

        # Directions: right, down, left, up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_ptr = 0
        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        res = []

        # Mark the starting element as visited and append it to the result
        res.append(matrix[r][c])
        matrix[r][c] = "visited"

        while len(res) < m * n:
            x, y = dirs[dir_ptr]
            new_r, new_c = r + x, c + y

            # Check if the new position is within bounds and not visited
            if 0 <= new_r < m and 0 <= new_c < n and matrix[new_r][new_c] != "visited":
                r, c = new_r, new_c
                res.append(matrix[r][c])
                matrix[r][c] = "visited"
            else:
                # Change direction
                dir_ptr = (dir_ptr + 1) % 4

        return res

