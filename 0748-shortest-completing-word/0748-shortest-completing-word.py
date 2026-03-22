class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l_chars = [char.lower() for char in licensePlate if char.isalpha()]
        l_count = Counter(l_chars)
        words.sort(key=len)
        for word in words:
            word_count = Counter(word)
            if all(word_count[char] >= l_count[char] for char in l_count):
                return word