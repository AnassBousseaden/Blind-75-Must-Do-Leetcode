

class Solution:
    def coinChange1(self, coins: list[int], amount: int) -> int:
        table = [amount+1]*(amount+1)
        table[0] = 0  # we need 0 coin to make 0
        for targetValue in range(amount+1):
            for coinValue in coins:
                if coinValue <= targetValue:
                    table[targetValue] = min(
                        table[targetValue-coinValue]+1, table[targetValue])
        return table[amount] if table[amount] != None else -1

    def coinChange2(self, coins: list[int], amount: int) -> int:
        stack = [0]
        depth = 0
        table = [False] * (amount+1)
        table[0] = True
        while not not stack:
            depth += 1
            stack_tmp = []
            for value in stack:
                for coin in coins:
                    newValue = value + coin
                    # print(newValue)
                    if newValue == amount:
                        return depth
                    if newValue >= amount:
                        continue
                    if table[newValue] == False:
                        table[newValue] = True
                        stack_tmp.append(newValue)
            # print(stack_tmp)
            stack = stack_tmp
        # print(table)
        return -1

    def coinChange(self, coins: list[int], amount: int) -> int:
        self.result = amount

        def DFS(nodeValue, depth):
            if nodeValue > amount:
                return
            if nodeValue == amount:
                self.result = min(self.result, depth)
            for coin in coins:
                DFS(nodeValue+coin, depth+1)
        DFS(0, 0)
        return self.result


test = Solution()
coins = [3, 7, 405, 436]

amount = 8839

print(test.coinChange1(coins, amount))
