

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        table = [1]*n
        result = 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    table[i] = max(table[i], table[j]+1)
                    result = max(result, table[i])
            print(f"{i}:{table}")

        return result


test = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(test.lengthOfLIS(nums))
