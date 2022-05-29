import heapq


class MedianFinder:
    def __init__(self):
        self.MaxHeap = []
        self.MinHeap = []

    def addNum(self, num: int) -> None:
        nMinHeap = len(self.MinHeap)
        nMaxHeap = len(self.MaxHeap)
        n = nMinHeap + nMaxHeap
        if n == 0:
            heapq.heappush(self.MaxHeap, -num)
            return
        if n == 1:
            topMaxHeap = -heapq.heappop(self.MaxHeap)
            heapq.heappush(self.MaxHeap, -min(topMaxHeap, num))
            heapq.heappush(self.MinHeap, max(topMaxHeap, num))
            return

        topMinHeap = self.MinHeap[0]
        if num < topMinHeap:
            heapq.heappush(self.MaxHeap, -num)

            nMaxHeap += 1
        if topMinHeap <= num:
            heapq.heappush(self.MinHeap, num)
            nMinHeap += 1
        # equilibrate the heaps

        if nMaxHeap < (nMinHeap):
            v = heapq.heappop(self.MinHeap)
            heapq.heappush(self.MaxHeap, -v)
            return
        if nMaxHeap > (nMinHeap+1):
            v = -heapq.heappop(self.MaxHeap)
            heapq.heappush(self.MinHeap, v)
            return

    def findMedian(self) -> float:
        if len(self.MaxHeap) == len(self.MinHeap):
            return (-self.MaxHeap[0]+self.MinHeap[0])/2
        return -self.MaxHeap[0]


test = MedianFinder()


for i in range(11):
    test.addNum(i)
print(test.MaxHeap, test.MinHeap)
