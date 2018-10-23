from math import inf
from PriorityQueue import PriorityQueue

class PriorityQueueHeap(PriorityQueue):
    def __rePositionNode__(self, nodeToMove):
        pass

    def __init__(self, nodes, childCount=2):
        # initialize variables
        self.rootNode = None
        self.unfilledNode = None
        self.childCount = childCount

        # insert nodes
        for node in nodes:
            self.insertNode(node)

    def empty(self):
        return self.rootNode is None

    def deleteMin(self):
        #TODO: if unfilled node has no children, keep going up tree until current node is no longer the leftmost node. Then go to previous child of parent and keep going right until you reach a node with no children. Set unfilled_node = parent of this node.
        if len(self.unfilledNode.children) == 0:
            while (self.unfilledNode != self.rootNode) and (self.unfilledNode.heapParent.children.index(self.unfilledNode) == 0):
                self.unfilledNode = self.unfilledNode.heapParent

            if self.rootNode != self.unfilledNode:
                currentIndex = self.unfilledNode.heapParent.children.index(self.unfilledNode)
                self.unfilledNode = self.unfilledNode.heapParent.children[currentIndex]

            while len(self.unfilledNode.children) > 0:
                self.unfilledNode = self.unfilledNode.children[self.childCount - 1]

            self.unfilledNode = self.unfilledNode.heapParent

        #TODO: Pop top of tree and move rightmost child of unfilled_node to take its place


        #TODO: Scan children for smallest child. If smallest child is smaller than the current node, bubble the child up. Scan new children and repeat process until no children are smaller.

    def reorder(self, changedNode):
        self.bubbleUp(changedNode)

    def insertNode(self, nodeToAdd):
        #TODO: insert node as child of unfilled node
        if self.rootNode is None:
            self.rootNode = nodeToAdd
            nodeToAdd.heapParent = None
            self.unfilledNode = nodeToAdd
        else:
            self.unfilledNode.append(nodeToAdd)
            nodeToAdd.heapParent = self.unfilledNode

        nodeToAdd.children = []

        #TODO: check if child needs to be bubbled up
        self.bubbleUp(nodeToAdd)

        #TODO: check if unfilled node is now filled. If yes, keep going up tree until the current node is no longer the rightmost node. Then go to next child of parent and keep going left until end of children. Then set unfilled node = (parent?). If root is reached, go all the way left until no more children. Then set unfilled node = this node
        if len(self.unfilledNode.children) == self.childCount:
            rightMostIndex = self.childCount - 1
            while (self.unfilledNode != self.rootNode) and (self.unfilledNode.heapParent.children.index(self.unfilledNode) == rightMostIndex):
                self.unfilledNode = self.unfilledNode.heapParent

            if self.unfilledNode != self.rootNode:
                currentIndex = self.unfilledNode.heapParent.children.index(self.unfilledNode)
                self.unfilledNode = self.unfilledNode.heapParent.children[currentIndex + 1]

            while len(self.unfilledNode.children) > 0:
                self.unfilledNode = self.unfilledNode.children[0]

    def bubbleUp(self, nodeToMove):
        #TODO: while parent is greater than node to move, swap parent and child node values, being sure to delete child's self-reference and moving the unfilled node pointer and root node pointers if necessary
        while nodeToMove.heapParent is not None and nodeToMove.heapParent.distance > nodeToMove.distance:
            parent = nodeToMove.heapParent
            parentParent = parent.heapParent
            parentChildren = parent.children
            nodeChildren = nodeToMove.children

            nodeToMove.heapParent = parentParent
            nodeToMove.children = parentChildren
            nodeToMove.children.remove(nodeToMove)

            parent.children = nodeChildren
            parent.heapParent = nodeToMove

            if self.unfilledNode == nodeToMove:
                self.unfilledNode = parent
            elif self.unfilledNode == parent:
                self.unfilledNode = nodeToMove

            if self.rootNode == nodeToMove:
                self.rootNode = parent
            elif self.rootNode == parent:
                self.rootNode = nodeToMove

