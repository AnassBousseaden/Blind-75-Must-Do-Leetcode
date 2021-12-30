
class Solution:
    # faire un parcout dans un graphe
    def dfs(self, m: int, n: int, i: int, j: int, grid: list[list[str]], visited: list[list[bool]]):
        if not (i >= 0 and i < m) or not (j >= 0 and j < n):
            return
        visited[i][j] = True
        for dir in [-1, 1]:
            if 0 <= i+dir and i+dir < m and not visited[i+dir][j] and grid[i+dir][j] == "1":
                self.dfs(m, n, i+dir, j, grid, visited)
            if 0 <= j+dir and j+dir < n and not visited[i][j+dir] and grid[i][j+dir] == "1":
                self.dfs(m, n, i, j+dir, grid, visited)

    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    result += 1
                    self.dfs(m, n, i, j, grid, visited)

        return result


test = Solution()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(test.numIslands(grid1))
print(test.numIslands(grid2))
