
class Solution:
    def isAnagram(self, s: str, t: str)-> bool:
        
        if len(s) != len(t):
            return False
        tl = list(t)
        for c in s:
            if c in tl:
                tl.remove(c)
        return len(tl) == 0