

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        q = [1] * (n+2)
        p = [1] * (n+2)
        for j in range(1, n+1):
            q[j] = nums[j-1] * q[j-1]
            p[j] = nums[n-j] * p[j-1]
        print(q, p)
        result = [1]*n
        for i in range(n):
            result[i] = q[i]*p[n-i-1]
        return result


test = Solution()

t = [1, 2, 3, 4]

print(test.productExceptSelf(t))
