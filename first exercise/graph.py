# class to implement a graph

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencyList= [[] for i in range(vertices)]
        self.weights = {}

    def getVerticesnum(self):
        return self.vertices

    def getEdges(self):
        return self.adjacencyList

    # add edge to the graph
    def addEdge(self, from_vertex, to_vertex, weight=None):

        currentVertices = self.vertices
        self.vertices = max(self.vertices, from_vertex+1, to_vertex+1)

        self.adjacencyList.extend([[] for i in range(self.vertices - currentVertices)])

        if to_vertex not in self.adjacencyList[from_vertex]:
            self.adjacencyList[from_vertex].append(to_vertex)
            self.adjacencyList[to_vertex].append(from_vertex)

        else:
            print("Edge already exists")

        if weight is not None:
            self.weights[(from_vertex, to_vertex)] = weight

        print("Edge added from vertex", from_vertex, "to vertex", to_vertex)

    # print all the edges in the graph
    def printEdges(self):

        edgesList = []
        for i in range(self.vertices):
            if len(self.adjacencyList[i]) != 0:
                edgesList.append([i, self.adjacencyList[i]])

        print(f"Actual list:\n{self.adjacencyList}")
        print("Edges with starting vertex and its adjacent list:")
        for i in edgesList:
            print(i)
