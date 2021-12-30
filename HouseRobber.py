class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        table = dict()
        table[n-1] = nums[n-1]
        table[n-2] = max(nums[n-1], nums[n-2])
        for j in range(n-3, -1, -1):
            table[j] = max(nums[j] + table[j+2], table[j+1])
        return table[0]


test = Solution()

nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238,
        168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]

print(test.rob(nums))
