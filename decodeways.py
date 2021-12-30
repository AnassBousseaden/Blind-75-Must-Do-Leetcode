from typing import Dict


class Solution:
    def numDecodings(self, s: str,  table=dict()) -> int:
        if len(s) == 1 and int(s[0]) == 0:
            return 0
        if len(s) <= 1:
            return 1
        if s in table:
            return table[s]
        first, second = int(s[0]), int(s[1])
        if first == 0:
            table[s] = 0
            return table[s]
        v = first*10+second
        if v <= 26 and 1 <= v:
            table[s] = self.numDecodings(
                s[1:], table)+self.numDecodings(s[2:], table)
            return table[s]
        table[s] = self.numDecodings(s[1:], table)
        return table[s]


test = Solution()

s = "152145"


print(test.numDecodings(s))
