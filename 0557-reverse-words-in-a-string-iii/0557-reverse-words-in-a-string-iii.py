class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_words = []
        for i in words:
            rev_words.append(i[::-1])
        return " ".join(rev_words)