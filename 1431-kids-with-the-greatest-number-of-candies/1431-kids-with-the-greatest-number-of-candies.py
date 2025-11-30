class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)

        for n in candies:
            if n + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res