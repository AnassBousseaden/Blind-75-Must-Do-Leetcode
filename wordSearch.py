class Solution:
    def dfs(self, m, n, i, j, board, visited, word):
        if word == "" or (board[i][j] == word[0] and len(word) == 1):
            return True
        if board[i][j] != word[0]:
            return False
        visited[i][j] = True
        print(i, j, board[i][j], visited)
        for dir in [-1, 1]:
            if 0 <= i+dir and i+dir < m and not visited[i+dir][j] and self.dfs(m, n, i+dir, j, board, visited, word[1:]):
                return True
            if 0 <= j+dir and j+dir < n and not visited[i][j+dir] and self.dfs(m, n, i, j+dir, board, visited, word[1:]):
                return True
        visited[i][j] = False
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(m, n, i, j, board, visited, word):
                    return True
        return False


test = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(test.exist(board, word))
