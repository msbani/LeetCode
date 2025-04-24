class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        numRows = len(matrix)
        numCols = len(matrix[0])
        dpTable = [[0] * (numCols + 1) for _ in range(numRows + 1)]
        maxSide = 0

        for row in range(1, numRows + 1):
            for col in range(1, numCols + 1):
                if matrix[row - 1][col - 1] == "1":
                    top = dpTable[row - 1][col]
                    left = dpTable[row][col - 1]
                    topLeft = dpTable[row - 1][col - 1]
                    dpTable[row][col] = 1 + min(top, left, topLeft)
                    maxSide = max(maxSide, dpTable[row][col])

        return maxSide * maxSide