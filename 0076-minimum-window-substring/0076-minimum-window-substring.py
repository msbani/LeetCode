
class Solution:
    def minWindow(self, s:str, t:str)-> str:
        d = defaultdict(int)
        for char in t:
            d[char] += 1
        formed, total = 0, len(d)
        l = r = 0
        len_ans = float('inf')
        subl, subr = 0, 0
        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    formed += 1
            while l <= r and formed == total:
                curr_len = r-l+1
                if curr_len < len_ans:
                    len_ans = curr_len
                    subl, subr = l, r+1
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1
                l += 1
            r += 1
        return "" if len_ans == float('inf') else s[subl:subr]


# Neetcode Solution    
       
        # if t == "": return ""

        # countT, window = {}, {}

        # for c in t:
        #     countT[c] = 1 + countT.get(c, 0)
        
        # have, need = 0, len(countT)
        # res, resLen = [-1, -1], float("inf")
        # l = 0
        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)
            
        #     if c in countT and window[c] == countT[c]:
        #         have += 1

        #     while have == need:
        #         # update the result
        #         if (r - l + 1) < resLen:
        #             res = [l, r]
        #             resLen = (r-l+1)
        #         # pop from the left of our window
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l += 1
        # l, r = res
        # return s[l:r+1] if resLen != float("inf") else ""