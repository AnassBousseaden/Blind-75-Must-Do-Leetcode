class Solution:
    def maxProductFirstTry(self, nums: list[int]) -> int:
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

    def maxProduct(self, nums: list[int]) -> int:
        maxValueAtIndex_i = nums[0]  # this is -inf
        maxValue = nums[0]  # this is -inf
        minValueAtIndex_i = nums[0]  # this is +inf
        for i, val in enumerate(nums[1:]):
            tmp_maxValueAtIndex_i = max(
                minValueAtIndex_i * val, maxValueAtIndex_i*val, val)
            tmp_minValueAtIndex_i = min(
                minValueAtIndex_i * val, maxValueAtIndex_i*val, val)
            minValueAtIndex_i = tmp_minValueAtIndex_i
            maxValueAtIndex_i = tmp_maxValueAtIndex_i
            maxValue = max(maxValueAtIndex_i, maxValue)
        return maxValue


test = Solution()

nums = [-4, -3, -2]
print(nums[1:])

print(test.maxProduct(nums))
