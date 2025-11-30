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

# Another simple solution.
        # max_candies = max(candies)

        # return [c + extraCandies >= max_candies for c in candies]