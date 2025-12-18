class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        return (counts1.keys()==counts2.keys() and sorted(counts1.values()) == sorted(counts2.values()))

# Without using Counter
        # count1 = {}
        # count2 = {}
        # for c in word1:
        #     count1[c] = count1.get(c, 0) + 1
        # for c in word2:
        #     count2[c] = count2.get(c, 0) + 1
        # return (count1.keys()==count2.keys() and sorted(count1.values()) == sorted(count2.values()))