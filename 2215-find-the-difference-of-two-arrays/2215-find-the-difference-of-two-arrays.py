class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1, res2 = [], []
        for n in nums1:
            if n not in nums2 and n not in res1:
                res1.append(n)
        for n in nums2:
            if n not in nums1 and n not in res2:
                res2.append(n)
        res = [res1, res2]
        return res
