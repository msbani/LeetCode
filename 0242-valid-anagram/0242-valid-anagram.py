
class Solution:
    def isAnagram(self, s: str, t: str)-> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

# One liner
        # return Counter(s) == Counter(t)
# One liner
        # return sorted(s) == sorted(t)
# My solution
        # if len(s) != len(t):
        #     return False
        # tl = list(t)
        # for c in s:
        #     if c in tl:
        #         tl.remove(c)
        # return len(tl) == 0