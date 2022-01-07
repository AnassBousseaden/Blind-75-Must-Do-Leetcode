class Solution:
    def rob2(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        table = dict()
        table[n-1] = nums[n-1]
        table[n-2] = max(nums[n-1], nums[n-2])
        for j in range(n-3, -1, -1):
            table[j] = max(nums[j] + table[j+2], table[j+1])
        return table[0]

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n >= 4:
            print(nums[2:-1], nums[1: -2])
            return max(nums[0] + self.rob2(nums[2:-1]), nums[-1]+self.rob2(nums[1: -2]), self.rob2(nums[1:-1]))
        return max(nums)


test = Solution()
nums = [2, 7, 7, 7, 4]

print(test.rob(nums))
