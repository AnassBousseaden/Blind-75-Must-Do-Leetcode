from collections import defaultdict
import collections


class Solution:
    # first solution O(n²) too slow
    def characterReplacement1(self, s: str, k: int) -> int:
        n = len(s)
        result = k
        for i in range(n):
            Hash = defaultdict(lambda: 0)
            currentMaxValue = 0
            for j in range(i, n):
                Hash[s[j]] += 1
                currentMaxValue = max(currentMaxValue, Hash[s[j]])
                subStringLen = j-i+1
                nbDiffCharSubString = j-i+1-currentMaxValue
                if nbDiffCharSubString > k:
                    break
                result = max(result, subStringLen)
        return result
    # second solution

    def characterReplacement2(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        Hash = defaultdict(int)
        maxf = 0
        for j in range(n):
            Hash[s[j]] += 1
            maxf = max(maxf, Hash[s[j]])  # new candidate
            if j-i+1 > k+maxf:
                Hash[s[i]] -= 1
                i += 1
        return min(maxf+k, len(s))

    def characterReplacement(self, s, k):
        maxf = i = 0
        count = collections.Counter()
        for j in range(len(s)):
            # print(f"string : {s[i:j+1]} and the most common : {maxf}")
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            if j - i + 1 > maxf + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i


s = "EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"
k = 13
test = Solution()
print(test.characterReplacement2(s, k))
print(test.characterReplacement(s, k))
