class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            for dig in str(num):
                if int(dig)==0 or num % int(dig) != 0:
                    break
            else:
                res.append(num)
        return res