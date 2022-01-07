

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        htable = defaultdict(int)
        for c in s:
            htable[c] = htable[c]+1
        for c in t:
            htable[c] = htable[c]-1
        for val in htable:
            if htable[val] != 0:
                return False
        return True


test = Solution()

s = "anagram"
t = "nagarjm"

print(test.isAnagram(s, t))
