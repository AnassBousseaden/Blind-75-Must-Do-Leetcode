from typing import Optional


class Solution:

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # on ajoute tout les mots dans notre trie
        Node = dict()
        for word in words:
            currentNode = Node
            for w in word:
                if not w in currentNode:
                    currentNode[w] = dict()
                currentNode = currentNode[w]
            currentNode['$'] = word
        m = len(board)
        n = len(board[0])
        result = []

        def dfs(i, j, currentNode: dict):
            currentLetter = board[i][j]
            if not (currentLetter in currentNode):
                return
            board[i][j] = '#'
            childrenNode = currentNode[currentLetter]
            candidate = childrenNode.pop('$', False)
            if candidate != False:
                result.append(candidate)
            for i_dir, j_dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= i+i_dir and i+i_dir < m and 0 <= j+j_dir and j+j_dir < n and (board[i+i_dir][j+j_dir] != '#'):
                    dfs(i+i_dir, j+j_dir, childrenNode)
            board[i][j] = currentLetter
            # Détruire les feuilles vide au fur et à mesure, optimisation qui améliore
            # le temps d'exécution mais qui n'améliore pas la complexité asymptotiquement
            if childrenNode == {}:
                currentNode.pop(currentLetter)

        for i in range(m):
            for j in range(n):
                if board[i][j] in Node:
                    dfs(i, j, Node)
        return (result)


test = Solution()

board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

print(test.findWords(board, words))
