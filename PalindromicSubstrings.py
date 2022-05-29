from tkinter import S


class Solution:
    # first solution O(n²)
    def countSubstrings1(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            size = 0
            while i-size >= 0 and i+size < n and s[i-size] == s[i+size]:
                size += 1
                result += 1
            size = 0
            while i-size >= 0 and i+size+1 < n and s[i-size] == s[i+size+1]:
                size += 1
                result += 1
        return result
    # second solution trying to do O(n)

    def countSubstrings1(self, s: str) -> int:
        n = len(s)
        result = 0
        return result


s = "abc"
test = Solution()
print(test.countSubstrings1(s))
# print(test.countSubstrings1(s))
