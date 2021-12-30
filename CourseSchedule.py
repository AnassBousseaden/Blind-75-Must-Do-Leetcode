
class Solution:
    def DFS(self, vertex: int, visited: list[bool], stack: list[bool], Adj: list[list[int]]) -> bool:
        visited[vertex] = True
        stack[vertex] = True
        for neighbor in Adj[vertex]:
            if stack[neighbor] and visited[neighbor]:
                return True
            if not visited[neighbor] and self.DFS(neighbor, visited, stack, Adj):
                return True
        stack[vertex] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # construire les listes d'adjascence
        Adj = [[] for _ in range(numCourses)]
        for l in prerequisites:
            Adj[l[1]].append(l[0])
        print(Adj)
        # faire un parcourt en profondeur en marquant les sommets
        visited = [False for _ in range(numCourses)]
        stack = [False for _ in range(numCourses)]
        for vertex in range(numCourses):
            if not visited[vertex] and self.DFS(vertex, visited, stack, Adj):
                return False
        return True


test = Solution()

t = [[0, 1], [2, 0], [1, 2]]

print(test.canFinish(3, t))
