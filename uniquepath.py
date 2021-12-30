class Solution:
    def swap(v1: int, v2: int):
        tmp = v1
        v1 = v2
        v2 = tmp

    def uniquePaths(self, m: int, n: int, table=[], isInitialized=False) -> int:
        if not isInitialized:
            table = [None]*n
            print(table)
            for i in range(n):
                table[i] = [None]*m
        if m == 1 or n == 1:
            return 1

        if table[n-1][(m-1)-1] == None:
            table[n-1][(m-1)-1] = Solution.uniquePaths(self,
                                                       m-1, n, table, isInitialized=True)
        if table[(n-1)-1][(m-1)] == None:
            table[(n-1)-1][(m-1)] = Solution.uniquePaths(self,
                                                         m, n-1, table, isInitialized=True)

        if not isInitialized:
            print(table)
        return table[(n-1)-1][(m-1)] + table[n-1][(m-1)-1]


Test = Solution()

print(Test.uniquePaths(3, 6))
