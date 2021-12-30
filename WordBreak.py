class Solution:
    def f(self, s: str, setWords: set, dicWords: dict) -> bool:
        if not s:
            return True
        if s in dicWords:
            return dicWords[s]
        for w in setWords:
            if s.startswith(w) and self.f(s[len(w):], setWords, dicWords):
                dicWords[s] = True
                return True
        dicWords[s] = False
        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        setWords = set(wordDict)
        dicWords = dict()
        result = self.f(s, setWords, dicWords)
        print(dicWords)
        return result


test = Solution()


s = "applepenapple"
wordDict = ["apple", "pen"]
w = wordDict[0]


print(s[len(w):])

print(test.wordBreak(s, wordDict))
