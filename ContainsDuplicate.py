class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        S = set()
        for val in nums:
            if val in S:
                return True
            S.add(val)
        return False


test = Solution()

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(test.containsDuplicate(nums))
