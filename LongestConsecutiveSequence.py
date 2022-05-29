class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        S = set(nums)
        n = len(nums)
        best_score = 0
        for val in nums:
            score = 1
            left_values = val-1
            right_values = val+1
            while left_values in S:
                score += 1
                S.remove(left_values)
                left_values -= 1
            while right_values in S:
                score += 1
                S.remove(right_values)
                right_values += 1
            best_score = max(best_score, score)
        return best_score


test = Solution()


t = [100, 4, 200, 1, 3, 2]

print(test.longestConsecutive(t))
