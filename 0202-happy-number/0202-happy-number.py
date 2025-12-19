class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = str(n)
            total = 0
            for i in n:
                total += int(i) * int(i)
            if total == 1:
                return True
            else:
                n = total
        return False