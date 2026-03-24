class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r1, r2 = 0, 1
        while r2 < len(matrix):
            c1, c2 = 0, 1
            while c2 < len(matrix[0]):
                if matrix[r1][c1] != matrix[r2][c2]:
                    return False
                c1 += 1
                c2 += 1
            r1 += 1
            r2 += 1
        return True