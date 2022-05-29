

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        productLeft, productRight = 1, 1
        for i in range(n):
            result[i] *= productLeft
            result[n-1-i] *= productRight
            productLeft = productLeft*nums[i]
            productRight = productRight*nums[n-1-i]
        return result


test = Solution()

t = [1, 2, 3, 4]

print(test.productExceptSelf(t))
