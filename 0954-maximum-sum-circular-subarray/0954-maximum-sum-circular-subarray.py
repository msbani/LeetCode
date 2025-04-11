class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = nums[0]
        maxSum = nums[0]
        curMax = nums[0]
        minSum = nums[0]
        curMin = nums[0]

        for i in range(1, n):
            num = nums[i]
            total += num
            curMax = max(num, curMax + num)
            maxSum = max(maxSum, curMax)
            curMin = min(num, curMin + num)
            minSum = min(minSum, curMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)