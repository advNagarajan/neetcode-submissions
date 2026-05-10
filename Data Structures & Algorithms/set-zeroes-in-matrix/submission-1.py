class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        mark = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mark.append((i,j))

        for i, j in mark:
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
            for row in range(len(matrix)):
                matrix[row][j] = 0


