class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * cols

        dp[0] = grid[0][0]
        for col in range(1, cols):
            dp[col] = dp[col-1]+grid[0][col]

        for row in range(1, rows):
            dp[0] += grid[row][0]
            for col in range(1, cols):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[-1]