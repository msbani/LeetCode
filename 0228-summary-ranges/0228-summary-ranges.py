class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, end = 0,0
        result = []
        for i in range(len(nums)):
            if i != len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                end += 1
            else:
                if start != end:
                    result.append(str(nums[start])+'->'+ str(nums[end]))
                else:
                    result.append(str(nums[start]))
                end += 1
                start = end
        return result
