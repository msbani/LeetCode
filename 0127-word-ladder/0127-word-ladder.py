from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([[beginWord,1]])
        while queue:
            currentWord, steps = queue.popleft()
            word = list(currentWord)
            for i in range(len(word)):
                originalChar = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == originalChar:
                        continue
                    word[i] = ch
                    newWord = "".join(word)

                    if newWord == endWord:
                        return steps + 1
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append([newWord, steps + 1])

                word[i] = originalChar

        return 0