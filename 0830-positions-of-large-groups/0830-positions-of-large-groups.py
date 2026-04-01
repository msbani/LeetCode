class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        count = 1
        first = 0
        second = 1
        while second < len(s):
            if s[first] != s[second]:
                if count >= 3:
                    res.append([first, second-1])
                first = second
                second += 1
                count = 1
            else:
                second += 1
                count += 1
        if count >= 3:
            res.append([first, second-1])    
        return res
