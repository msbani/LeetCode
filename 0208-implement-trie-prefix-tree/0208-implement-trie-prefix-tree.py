class TrieNode:
    def __init__(self, character = None):
        self.character = character
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children.update({char:TrieNode(char)})
            current = current.children.get(char)
        current.is_end_of_word = True 

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            try:
                current = current.children[char]
            except KeyError:
                return False
        if current.is_end_of_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            try:
                current = current.children[char]
            except KeyError:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)