
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.H = dict()

    def cloneGraph(self, node: 'Node') -> 'Node':
        val = node.val
        if val in self.H:
            return self.H[val]
        cloneRootNode = Node(val)
        self.H[val] = cloneRootNode
        for neighborNode in node.neighbors:
            cloneRootNode.neighbors.append(self.cloneGraph(neighborNode))
        return cloneRootNode

    def cloneGraphIterative(self, node: 'Node') -> 'Node':
        stackGraph = [node]
        H = dict()
        H[node.val] = Node(node.val)
        while not not stackGraph:
            currentNodeGraph = stackGraph.pop()
            for neighborNode in currentNodeGraph.neighbors:
                if neighborNode.val not in H:
                    H[neighborNode.val] = Node(neighborNode.val)
                    stackGraph.append(neighborNode)
                cloneNeighborNode = H[neighborNode.val]
                H[currentNodeGraph.val].neighbors.append(cloneNeighborNode)
        return H[node.val]


test = Solution()

N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N1.neighbors = [N2, N3]
N2.neighbors = [N1, N3]
N3.neighbors = [N1, N2]

G = N1

cloneG = test.cloneGraphIterative(G)

print(
    f"here is the first value : {cloneG.neighbors[0].val} and the neighbors : {cloneG.neighbors[0].neighbors}")

print(f"G @ : {G} ; G_clone @ : {cloneG}")
