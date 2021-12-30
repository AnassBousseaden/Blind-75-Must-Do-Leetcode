class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervalToAdd = newInterval
        result = []
        added = False
        for interval in intervals:
            if(added == False and interval[0] > intervalToAdd[1]):
                added = True
                result.append(intervalToAdd)

            if not (interval[1] < intervalToAdd[0] or intervalToAdd[1] < interval[0]):
                intervalToAdd = [
                    min(interval[0], intervalToAdd[0]), max(intervalToAdd[1], interval[1])]
            else:
                result.append(interval)
        if (added == False):
            result.append(intervalToAdd)
        return result


test = Solution()
L = [[1, 3], [6, 9]]
I = [2, 5]

print(test.insert(L, I))
