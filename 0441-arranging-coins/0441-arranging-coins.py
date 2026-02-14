class Solution:
    def arrangeCoins(self, n: int) -> int:
        c_rows = 0
        r = 1
        while n > 0:
            if n >= r:
                c_rows += 1
            else:
                return c_rows
            n -= r
            r += 1
        return c_rows
            