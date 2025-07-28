class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        counts1 = Counter(nums1)
        for num in nums2:
            if counts1.get(num,0) > 0:
                result.append(num)
                counts1[num] -= 1
        return result