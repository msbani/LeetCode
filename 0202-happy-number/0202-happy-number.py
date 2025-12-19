class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = self.calc(n)
            if n in seen:
                return False
            seen.add(n)
        return True

    def calc(self, n):
        curr = 0
        while n > 0:
            digit = n % 10
            curr += digit * digit
            n //= 10
        return curr
# My Solution
        # seen = set()
        # while n not in seen:
        #     seen.add(n)
        #     n = str(n)
        #     total = 0
        #     for i in n:
        #         total += int(i) * int(i)
        #     if total == 1:
        #         return True
        #     else:
        #         n = total
        # return False