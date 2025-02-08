from graph import Graph
from copy import deepcopy
from collections import deque

class FlowNetwork:
    def __init__(self, graphObject):
        self.graph = deepcopy(graphObject)
        self.source = self.getSource()
        self.sink = self.getSink()

    # Better implementation would be to check if the indegree of the vertex also
    # .getInDegree() is implemented in the graph.py
    def getSource(self):
        for vertex in self.graph.getEdges():
            if len(self.graph.getEdges()[vertex]) > 0:
                return vertex

    # Highest node with some indegree
    def getSink(self):
        for i in range(len(self.graph.getEdges()), 0, -1):
            if self.graph.getInDegree(i) != 0:
                return i

    def makeResidualGraph(self):
        # initialize residual graph with the same number of vertices
        residualGraph = Graph(self.graph.getVerticesnum())

        # Add edges and capacity as weights to the residual graph
        for (u, v), capacity in self.graph.weights.items():
            residualGraph.addEdge(u, v, capacity)
            if (v, u) not in self.graph.weights:
                residualGraph.addEdge(v, u, 0)
        return residualGraph

    def bfs(self, residualGraph, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            vertex = queue.popleft()
            for neighbor in residualGraph.getEdges()[vertex]:
                if neighbor not in visited and residualGraph.weights[(vertex, neighbor)] > 0:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = vertex
                    if neighbor == sink:
                        return True
        return False

    def FordFulkerson(self):
        residualGraph = self.makeResidualGraph()
        parent = {}
        maxFlow = 0

        while self.bfs(residualGraph, self.source, self.sink, parent):
            pathFlow = float("inf")
            sink = self.sink
            while sink != self.source:
                pathFlow = min(pathFlow, residualGraph.weights[(parent[sink], sink)])
                sink = parent[sink]

            maxFlow += pathFlow
            v = self.sink
            while v != self.source:
                u = parent[v]
                residualGraph.weights[(u, v)] -= pathFlow
                residualGraph.weights[(v, u)] += pathFlow
                v = parent[v]

        return maxFlow, residualGraph

    def findMinCut(self):
        maxFlow, residualGraph = self.FordFulkerson()
        visited = set()
        queue = deque([self.source])
        visited.add(self.source)

        while queue:
            vertex = queue.popleft()
            for neighbor in residualGraph.getEdges()[vertex]:
                if neighbor not in visited and residualGraph.weights[(vertex, neighbor)] > 0:
                    visited.add(neighbor)
                    queue.append(neighbor)

        minCutEdges = []
        for u in visited:
            for v in self.graph.getEdges()[u]:
                if v not in visited and (u, v) in self.graph.weights:
                    minCutEdges.append((u, v))

        return minCutEdges

    def print(self):
        print(f"Source node: {self.source}")
        print(f"Sink node: {self.sink}")


