

class Trie:
    def __init__(self):
        self.Node = dict()

    def insert(self, word: str) -> None:
        currentNode = self.Node
        for w in word:
            if not w in currentNode:
                currentNode[w] = dict()
            currentNode = currentNode[w]
        currentNode['\n'] = None

    def search(self, word: str) -> bool:
        currentNode = self.Node
        for w in word:
            if not w in currentNode:
                return False
            currentNode = currentNode[w]
        return '\n' in currentNode

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.Node
        for w in prefix:
            if not w in currentNode:
                return False
            currentNode = currentNode[w]
        return True


# Your Trie object will be instantiated and called as such:
word = "hello"
prefix = "hel"
obj = Trie()
obj.insert(word)
print(obj.Node)
print(obj.search(prefix))
print(obj.startsWith(prefix))
