class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        Sum = sum(nums)

        dp = [[0,0] for _ in range(len(nums))]

        dp[0][0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0]+nums[i], nums[i])
            dp[i][1] = min(dp[i-1][1]+nums[i], nums[i])
            res = max(res, dp[i][0], Sum - dp[i][1])
        return res