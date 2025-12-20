class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] == '*':
                res.pop()
            elif s[i] != '*':
                res.append(s[i])
        return ''.join(res)
            