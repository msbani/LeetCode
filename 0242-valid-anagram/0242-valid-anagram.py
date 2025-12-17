
class Solution:
    def isAnagram(self, s: str, t: str)-> bool:
        tl = list(t)
        if len(s) != len(tl):
            return False
        for c in s:
            if c in tl:
                tl.remove(c)
        return len(tl) == 0