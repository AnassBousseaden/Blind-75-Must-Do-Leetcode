class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        maxLength = 0

        for i in range(n):
            if(i > maxLength):
                break
            maxLength = max(i+nums[i], maxLength)
        return maxLength >= (n-1)


Test = Solution()
L = [3, 2, 1, 0, 4]

print(Test.canJump(L))
