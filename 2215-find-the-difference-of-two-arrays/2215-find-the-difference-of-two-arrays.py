class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        res1, res2 = set(), set()

        for n in nums1:
            if n not in nums2:
                res1.add(n)

        for n in nums2:
            if n not in nums1:
                res2.add(n)
        
        return [list(res1), list(res2)]

# My Solution with O(m*n) TIme complexity
        # res1, res2 = [], []
        # for n in nums1:
        #     if n not in nums2 and n not in res1:
        #         res1.append(n)
        # for n in nums2:
        #     if n not in nums1 and n not in res2:
        #         res2.append(n)
        # return [res1, res2]

