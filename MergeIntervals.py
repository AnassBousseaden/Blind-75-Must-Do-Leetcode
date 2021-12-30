class Solution:
    def mergeTwo(interval1: list[int], interval2: list[int]) -> list[int]:
        if(interval1[1] <= interval2[0]):
            return [interval1[0], interval2[1]]
        if(interval2[1] <= interval1[0]):
            return [interval2[0], interval1[1]]

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda k: k[0])
        result = []
        for interval in intervals:
            if(not result or result[-1][1] < interval[0]):
                result.append(interval)
            if(result[-1][1] >= interval[0]):
                result[-1][0] = min(interval[0], result[-1][0])
                result[-1][1] = max(interval[1], result[-1][1])
        return result


test = Solution()
L = [[2, 3], [2, 2], [4, 5],  [2, 10]]

print(test.merge(L))
