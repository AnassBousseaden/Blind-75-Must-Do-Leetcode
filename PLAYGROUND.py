from collections import defaultdict
import heapq


newHeap = []

heapq.heappush(newHeap, (1, 2))
heapq.heappush(newHeap, (57, 1))
heapq.heappush(newHeap, (4, 5))
heapq.heappop(newHeap)

H = defaultdict(lambda: 0)

H['a'] += 1
print(H['a'])


E = set()


E.add("here")
E.add("here")
print(E)

c = 'a'
s = "hello"

print(s+c)

print(newHeap)
