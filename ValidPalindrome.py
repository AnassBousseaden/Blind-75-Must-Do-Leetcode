class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        while (i < j and i < n and j >= 0):
            c_i, c_j = s[i], s[j]
            if not c_i.isalnum():
                i += 1
                continue
            if not c_j.isalnum():
                j -= 1
                continue
            if c_i.lower() != c_j.lower():
                return False
            i += 1
            j -= 1
        return True


Test = Solution()

s = " "

print(Test.isPalindrome((s)))
print('P'.isalnum())
