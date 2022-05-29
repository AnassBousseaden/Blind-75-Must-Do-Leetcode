class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return ((n * (n+1)) >> 1) - sum(nums)


test = Solution()

nums = [3, 0, 1]


print(test.missingNumber(nums))
