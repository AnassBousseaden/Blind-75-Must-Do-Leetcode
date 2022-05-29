class Solution:
    # first solution bad
    def pacificAtlantic1(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        marked = [[False]*n for _ in range(m)]
        savedResult = [[[False, False] for _ in range(n)] for _ in range(m)]
        ATLANTIC, PACIFIC = 0, 1
        result = []

        def aux(i, j):
            savedResult[i][j][ATLANTIC] = (savedResult[i][j][ATLANTIC] or
                                           i == m-1 or j == n-1)
            savedResult[i][j][PACIFIC] = (
                savedResult[i][j][PACIFIC] or i == 0 or j == 0)
            marked[i][j] = True
            for dir_i, dir_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i+dir_i < 0 or i+dir_i >= m or j+dir_j < 0 or j+dir_j >= n or (heights[i+dir_i][j+dir_j] > heights[i][j]):
                    continue
                # if not marked then go in
                if marked[i+dir_i][j+dir_j] == False:
                    aux(i+dir_i, j+dir_j)
                savedResult[i][j][ATLANTIC] = (
                    savedResult[i+dir_i][j+dir_j][ATLANTIC] or savedResult[i][j][ATLANTIC])
                savedResult[i][j][PACIFIC] = (
                    savedResult[i+dir_i][j+dir_j][PACIFIC] or savedResult[i][j][PACIFIC])
            for dir_i, dir_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i+dir_i < 0 or i+dir_i >= m or j+dir_j < 0 or j+dir_j >= n or (heights[i+dir_i][j+dir_j] > heights[i][j]):
                    continue
                if heights[i+dir_i][j+dir_j] == heights[i][j]:
                    savedResult[i+dir_i][j+dir_j][ATLANTIC] = savedResult[i +
                                                                          dir_i][j+dir_j][ATLANTIC] or savedResult[i][j][ATLANTIC]
                    savedResult[i+dir_i][j+dir_j][PACIFIC] = savedResult[i +
                                                                         dir_i][j+dir_j][PACIFIC] or savedResult[i][j][PACIFIC]
            if savedResult[i][j][PACIFIC] and savedResult[i][j][ATLANTIC]:
                result.append([i, j])
        for i in range(m):
            for j in range(n):
                if marked[i][j] != True:
                    aux(i, j)
        return result

    def pacificAtlantic2(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        marked = [[False] * n for _ in range(m)]
        savedResult = [[False] * n for _ in range(m)]
        result = []

        def aux2(i, j, marked, savedResult):
            marked[i][j] = True
            for dir_i, dir_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i+dir_i < 0 or i+dir_i >= m or j+dir_j < 0 or j+dir_j >= n or (heights[i+dir_i][j+dir_j] < heights[i][j]) or marked[i+dir_i][j+dir_j] == True:
                    continue
                savedResult[i+dir_i][j+dir_j] = savedResult[i +
                                                            dir_i][j+dir_j] or savedResult[i][j]
                aux2(i+dir_i, j+dir_j, marked, savedResult)
        # case pacific
        i = 0
        for j in range(n):
            savedResult[i][j] = True
            marked[i][j] = True
            aux2(i, j, marked, savedResult)
        j = 0
        for i in range(m):
            savedResult[i][j] = True
            marked[i][j] = True
            aux2(i, j, marked, savedResult)
        marked2 = [[False] * n for _ in range(m)]
        savedResult2 = [[False] * n for _ in range(m)]
        i = m-1
        for j in range(n):
            savedResult2[i][j] = True
            marked2[i][j] = True
            aux2(i, j, marked2, savedResult2)
        j = n-1
        for i in range(m):
            savedResult2[i][j] = True
            marked2[i][j] = True
            aux2(i, j, marked2, savedResult2)
        for i in range(m):
            for j in range(n):
                if savedResult[i][j] and savedResult2[i][j]:
                    result.append([i, j])
        return result


test = Solution()

heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(test.pacificAtlantic2(heights))
