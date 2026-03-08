class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = sum(nums)
        b = sum(set(nums))

        s = n * (n+1)//2
        return (a - b, s - b)
        
        """dup, missing = -1, -1
        for i in range(1, len(nums)+1):
            count = nums.count(i)
            if count ==2:
                dup = i
            elif count ==0:
                missing = i
        return [dup, missing]"""