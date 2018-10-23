from math import inf
from PriorityQueue import PriorityQueue


class PriorityQueueArray(PriorityQueue):
    # O(n)
    def __findSmallestNodeIndex__(self):
        smallestDistance = inf
        smallestDistanceNodeIndex = None

        for i in range(self.nodes):
            if self.nodes[i].distance < smallestDistance:
                smallestDistance = self.nodes[i].distance
                smallestDistanceNodeIndex = i

        return smallestDistanceNodeIndex

    def __init__(self, nodes):
        self.nodes = nodes

    # O = O of findSmallestNode + O(1) of popping item from list.
    def deleteMin(self):
        return self.nodes.pop(self.__findSmallestNodeIndex__())

    # O(1)
    def reorder(self):
        pass

    # O(1)
    def empty(self):
        return len(self.nodes) == 0