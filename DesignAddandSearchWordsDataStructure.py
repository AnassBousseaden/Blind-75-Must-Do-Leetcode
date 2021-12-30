from typing import Optional


class WordDictionary:

    def __init__(self):
        self.Node = dict()

    def addWord(self, word: str) -> None:
        currentNode = self.Node
        for w in word:
            if not w in currentNode:
                currentNode[w] = dict()
            currentNode = currentNode[w]
        currentNode['\n'] = None

    def search(self, word: str, currentNode: Optional[dict] = None) -> bool:
        currentNode = self.Node if currentNode is None else currentNode
        for i, w in enumerate(word):
            if w == '.':
                # parcourt en profondeur de l'arbre
                rest = word[i+1:]
                for k in currentNode:
                    if k == '\n':
                        continue
                    tmpNode = currentNode[k]
                    if self.search(rest, tmpNode):
                        return True
                return False
            if not w in currentNode:
                return False
            currentNode = currentNode[w]
        return '\n' in currentNode


# Your WordDictionary object will be instantiated and called as such:
word = "hello"
word2 = "......"
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word2)

print(param_2)
