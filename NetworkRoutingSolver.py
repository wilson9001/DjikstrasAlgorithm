#!/usr/bin/python3

from math import inf
from CS312Graph import *
import time
from PriorityQueue import PriorityQueue
from PriorityQueueArray import PriorityQueueArray
from PriorityQueueBinaryHeap import PriorityQueueBinaryHeap

def makeQueue(nodes, use_heap=False):
    if use_heap:
        return PriorityQueueBinaryHeap(nodes)
    else:
        return PriorityQueueArray(nodes)


class NetworkRoutingSolver:
    def __init__( self):
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath(self, destIndex):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        node = self.network.nodes[self.source]
        edges_left = 3
        while edges_left > 0:
            edge = node.neighbors[2]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            total_length += edge.length
            node = edge.dest
            edges_left -= 1
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths(self, srcIndex, use_heap=False):
        self.source = srcIndex
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        graph = self.network.graph
        nodes = graph.nodes

        # O(n)
        # Initialize node tracking
        for node in nodes:
            node.distance = inf
            node.parent = None

        nodes[srcIndex].distance = 0

        queue = makeQueue

        while len(queue) != 0:
            source_node = queue.deleteMin()

            for edge in source_node.neighbors:
                destination_node = edge.dest
                if destination_node.distance > (source_node.distance + edge.length):
                    destination_node.setDistance(destination_node.distance + edge.length)
                    destination_node.setPreviousNode(source_node)
                    queue.reorder(destination_node)

        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        t2 = time.time()
        return t2 - t1

