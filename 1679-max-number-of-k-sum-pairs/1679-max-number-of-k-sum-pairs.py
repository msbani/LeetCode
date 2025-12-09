class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # d = defaultdict(int)
        # pair = 0
        # for n in nums:
        #     if d[k-n] > 0:
        #         pair += 1
        #         d[k-n] -= 1
        #     else:
        #         d[n] += 1
        # return pair

# Another solution with sorting
        nums.sort()
        i, j = 0, len(nums)-1
        pair = 0

        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                pair += 1
                i += 1
                j -= 1
            elif total < k:
                i += 1
            else:
                j -= 1
        return pair
