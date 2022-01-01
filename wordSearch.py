class Solution:

    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        k = len(word)

        def dfs(i: int, j: int, t: int):
            currentLetter = board[i][j]
            if (t == k-1):
                return currentLetter == word[t]
            if currentLetter != word[t]:
                return False
            board[i][j] = '#'
            for dir in [-1, 1]:
                if 0 <= i+dir and i+dir < m and board[i+dir][j] != '#' and dfs(i+dir, j, t+1):
                    return True
                if 0 <= j+dir and j+dir < n and board[i][j+dir] != '#' and dfs(i, j+dir, t+1):
                    return True
            board[i][j] = currentLetter
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


test = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(test.exist(board, word))
