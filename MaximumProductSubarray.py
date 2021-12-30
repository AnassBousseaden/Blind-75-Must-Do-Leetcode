class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        table = dict()
        maxResult = -11
        for i, val in enumerate(nums):
            tab = dict()
            for j in range(0, i+1):
                if i == j:
                    tab[(i, j)] = val
                    maxResult = max(maxResult, val)
                else:
                    tmp = val * table[(i-1, j)]
                    tab[(i, j)] = tmp
                    maxResult = max(maxResult, tmp)
            table = tab
        return maxResult


test = Solution()

nums = [2, 3, -2, 4]


print(test.maxProduct(nums))
