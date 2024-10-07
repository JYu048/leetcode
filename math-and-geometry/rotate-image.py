class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)

        # swap row and column
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse rows
        for i in range(n):
            matrix[i].reverse()
        



