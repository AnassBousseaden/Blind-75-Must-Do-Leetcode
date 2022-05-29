import heapq


class Solution:
    # first naive solution O(nlog(n))
    def topKFrequent0(self, nums: list[int], k: int) -> list[int]:
        l = []
        Hash = dict()
        for x in nums:
            if x not in Hash:
                Hash[x] = 0
            Hash[x] += 1
        for x in nums:
            if x in Hash:
                l.append((x, Hash[x]))
                del Hash[x]
        l.sort(key=lambda x: -x[1])
        return [l[i][0] for i in range(k)]
    # second solution
    # O(n) complexity but in practive slower

    def topKFrequent1(self, nums: list[int], k: int) -> list[int]:
        l = []
        Hash = dict()
        for x in nums:
            if x not in Hash:
                Hash[x] = 0
            Hash[x] += 1
        for x in nums:
            if x in Hash:
                l.append((-Hash[x], x))
                del Hash[x]
        # use of a maxheap to get the most frequence elements
        heapq.heapify(l)
        return [heapq.heappop(l)[1] for _ in range(k)]


test = Solution()
nums = [1, 1, 1, 2, 2, 3]

print(test.topKFrequent1(nums, 2))
