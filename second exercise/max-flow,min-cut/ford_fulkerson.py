from graph import Graph
from copy import deepcopy
from collections import deque

class FlowNetwork:
    def __init__(self, graphObject):
        self.graph = deepcopy(graphObject)
        self.source = self.getSource()
        self.sink = self.getSink()

    # Better implementation would be to check the indegree of the vertex also
    # .getInDegree() is implemented in the graph.py
    def getSource(self):
        # minimum vertex with some outdegree
        for vertex in self.graph.getEdges():
            if len(self.graph.getEdges()[vertex]) > 0:
                return vertex

    # Better implementation would be to check the outdegree of the vertex also
    # .getOutDegree() is implemented in the graph.py
    def getSink(self):
        # Highest node with some indegree
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
                # reverse edge with 0 capacity if it doesn't exist
                residualGraph.addEdge(v, u, 0)
        return residualGraph

    # bfs to augment the path
    def bfs(self, residualGraph, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            vertex = queue.popleft()
            for neighbor in residualGraph.getEdges()[vertex]:
                # if the neighbor is not visited and 
                # there is a positive weight(i.e. flow is possible)
                if neighbor not in visited and residualGraph.weights[(vertex, neighbor)] > 0:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = vertex  # store the parent of the neighbor
                    if neighbor == sink:
                        return True  # if path is found
        return False  # if path is not found

    def FordFulkerson(self):
        residualGraph = self.makeResidualGraph()
        parent = {}
        maxFlow = 0

        while self.bfs(residualGraph, self.source, self.sink, parent):
            pathFlow = float("inf")
            sink = self.sink
            # walk back from sink to source in the augmented path
            while sink != self.source:
                # find the minimum flow in the path
                pathFlow = min(pathFlow, residualGraph.weights[(parent[sink], sink)])
                sink = parent[sink]

            # update the maximum flow
            maxFlow += pathFlow

            # update the residual graph
            v = self.sink
            # walk back from sink to source in the augmented path
            while v != self.source:
                u = parent[v]
                # subtract the flow from the forward edge
                residualGraph.weights[(u, v)] -= pathFlow
                # add the flow to the reverse edge
                # which can be used to cancel bad flow decisions
                residualGraph.weights[(v, u)] += pathFlow
                v = parent[v]

        return maxFlow, residualGraph

    def findMinCut(self):
        maxFlow, residualGraph = self.FordFulkerson()
        visited = set()
        queue = deque([self.source])
        visited.add(self.source)

        # bfs to find the vertices reachable from the source
        while queue:
            vertex = queue.popleft()
            for neighbor in residualGraph.getEdges()[vertex]:
                # only add the vertex that has positive residual capacity
                if neighbor not in visited and residualGraph.weights[(vertex, neighbor)] > 0:
                    visited.add(neighbor)
                    queue.append(neighbor)

        minCutEdges = []
        # go through the reachable vertices
        for u in visited:
            for v in self.graph.getEdges()[u]:
                # if there was an edge in the original graph but now it is not
                # reachable then it is a min cut edge (i.e. max capacity is used)
                if v not in visited and (u, v) in self.graph.weights:
                    minCutEdges.append((u, v))

        return minCutEdges

    def print(self):
        print(f"Source node: {self.source}")
        print(f"Sink node: {self.sink}")


