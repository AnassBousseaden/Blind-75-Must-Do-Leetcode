from typing import overload


class Solution:
    def isValidWindow(self, s: str, H_t: dict, keys: set) -> bool:
        H_s = dict.fromkeys(keys, 0)
        for char in s:
            if H_s.get(char) == None:
                continue
            H_s[char] += 1
        for k in keys:
            if H_s[k] < H_t[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        bestWindow = ""
        bestlength = n+1
        i, j = 0, 0
        # create the Dic associated with t
        keys = set(t)
        H = dict.fromkeys(keys, 0)
        for k in keys:
            H[k] = t.count(k)

        while i < n or j < n:
            if i == j:
                j = j+1
            else:
                tmp = s[i:j]
                print(i, j, tmp)
                if self.isValidWindow(tmp, H, keys):
                    if bestlength > j-i:
                        bestWindow = tmp
                        bestlength = j-i
                    i = i + 1
                else:
                    if j < n:
                        j = j+1
                    else:
                        i = i+1
        return bestWindow


test = Solution()

s = "ADOBECODEBANC"
t = "ABC"

print(test.minWindow(s, t))
