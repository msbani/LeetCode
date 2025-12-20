class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c == '*':
                res and res.pop()       # res and is written to make sure the list in non empty
            else:
                res.append(c)
        return ''.join(res)
            