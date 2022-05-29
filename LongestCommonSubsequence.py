
class Solution:
    # first solution (bad) O(n²)
    def longestCommonSubsequence(self, w1: str, w2: str) -> int:
        n1, n2 = len(w1), len(w2)
        dp = [[0] * n2 for _ in range(n1)]
        result = 0
        for i in range(n1):
            for j in range(n2):
                if w1[i] == w2[j]:
                    if j > 0 and i > 0:
                        dp[i][j] = dp[i-1][j-1]+1
                    if dp[i][j] < 1:
                        dp[i][j] = 1
                else:
                    if i > 0:
                        dp[i][j] = dp[i-1][j]
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])
            print(dp[i])
        return max(dp[n1-1])

    def longestCommonSubsequence2(self, w1: str, w2: str) -> int:
        n1, n2 = len(w1), len(w2)
        dp = [0] * (n2)
        prevdp = [0] * n2
        for i in range(n1):
            # switch roles of pointers
            tmp = prevdp
            prevdp = dp
            dp = tmp
            for j in range(n2):
                if w1[i] == w2[j]:
                    if j > 0:
                        dp[j] = prevdp[j-1]+1
                    else:
                        dp[j] = 1
                else:
                    dp[j] = prevdp[j]
                    if j > 0:
                        dp[j] = max(dp[j], dp[j-1])
        return max(dp)
    # more readable solution (made with the help of the leetcode forum)

    def longestCommonSubsequence3(self, w1: str, w2: str) -> int:
        n1, n2 = len(w1), len(w2)
        dp = [0] * (n2+1)
        nextdp = [0] * (n2+1)
        for i in range(n1):
            # switch roles of pointers
            for j in range(n2):
                if w1[i] == w2[j]:
                    nextdp[j+1] = dp[j]+1
                else:
                    nextdp[j+1] = max(dp[j+1], nextdp[j])
            tmp = nextdp
            nextdp = dp
            dp = tmp
        return dp[n2]


text1 = "abcba"
text2 = "abcbcba"
test = Solution()
print(test.longestCommonSubsequence(text1, text2))
print(test.longestCommonSubsequence2(text1, text2))
print(test.longestCommonSubsequence3(text1, text2))
