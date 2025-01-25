# class to implement a graph
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.weights = {}
        self.vertices = len(self.adjacencyList)

    def getVerticesnum(self):
        return self.vertices

    def getEdges(self):
        return self.adjacencyList

    # add edge to the graph
    def addEdge(self, from_vertex, to_vertex, weight=None):
        if to_vertex not in self.adjacencyList[from_vertex]:
            self.adjacencyList[from_vertex].append(to_vertex)

        if weight is not None:
            self.weights[(from_vertex,to_vertex)] = weight

        self.vertices = len(self.adjacencyList)

    def printEdges(self):
        print(f"Total nodes: {self.vertices}")
        print(self.adjacencyList)
