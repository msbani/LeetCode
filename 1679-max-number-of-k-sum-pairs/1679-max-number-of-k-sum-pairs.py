class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        pair = 0
        for n in nums:
            if d[k-n] > 0:
                pair += 1
                d[k-n] -= 1
            else:
                d[n] += 1
        return pair