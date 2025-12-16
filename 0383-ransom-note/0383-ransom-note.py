
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str)->bool:
        d = defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            if c not in d or d[c] <= 0:
                return False
            d[c] -= 1
        return True