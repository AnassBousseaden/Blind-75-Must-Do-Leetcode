class Solution:
    def reverseBits(self, n: int) -> int:
        return n | (1 << 31) + 1


test = Solution()
