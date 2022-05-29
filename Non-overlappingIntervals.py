from collections import defaultdict


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # recherche l'indice qui est bon retourne None ou end tel que end < start et end maximale
        def search(value, intervals):
            result = None
            start, end = 0, len(intervals)-1
            while start <= end:
                middle = (start+end)//2
                if intervals[middle][1] <= value:
                    start = middle + 1
                    result = intervals[middle][1]
                else:
                    end = middle - 1
            return result
        intervals.sort(key=lambda x: x[1])  # sorted with start as value
        currentMax = 1
        table = defaultdict(int)
        for start, end in intervals:
            prevBorn = search(start, intervals)
            # print(start, prevBorn)
            table[end] = max(table[prevBorn]+1, table[end], currentMax)
            currentMax = max(currentMax, table[end])
        return len(intervals)-currentMax


test = Solution()

intervals = [[1, 2], [2, 3], [3, 4], [1, 3], [-52, 31], [82, 97],
             [-65, -11], [-62, -49], [95, 99], [58, 95], [-40, -26]]
# [[1,2],[1,2],[1,2]]
# [[1,2],[2,3]]

print(test.eraseOverlapIntervals(intervals))
