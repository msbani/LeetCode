class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # num_set = set(nums)
        # longest = 0
        # for n in num_set:
        #     if n - 1 not in num_set:
        #         length = 1
        #         while n + length in num_set:
        #             length += 1
        #         longest = max(longest, length)
        # return longest

        nums = sorted(set(nums))
        longest = 1
        l = 0

        while len(nums) == 0:
            return 0

        for r in range(1, len(nums)):
            if nums[r] == nums[r-1]+1:
                longest = max(longest, r-l+1)
            else:
                l = r
        return longest
            


