
class Solution:
    def lengthOfLastWord(self, s:str)->int:
        i = len(s) - 1
        length = 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

# Another solution using built in functions
        # words = s.strip().split()
        # if not words:
        #     return 0
        # return len(words[-1])
