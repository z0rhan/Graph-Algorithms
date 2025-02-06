from collections import defaultdict
# class to implement a graph

class Graph:

    def __init__(self, vertices=None):

        if vertices is not None:
            self.adjacencyList = {i: [] for i in range(1, vertices+1)}
        else:
            self.adjacencyList = defaultdict(list)

        self.weights = {}
        self.verticesNum = vertices

    def getVerticesnum(self):
        return self.vertices

    def getEdges(self):
        return self.adjacencyList

    # add edge to the graph
    def addEdge(self, from_vertex, to_vertex, weight=None):

        current_v_num = len(self.adjacencyList)
        self.verticesNum = from_vertex

        # add new edges if required
        if self.verticesNum > current_v_num:
            newVertices = {i: [] for i in range(current_v_num+1, self.verticesNum+1)}
            self.adjacencyList.update(newVertices)

        if to_vertex not in self.adjacencyList[from_vertex]:
            self.adjacencyList[from_vertex].append(to_vertex)

        if weight is not None:
            self.weights[(from_vertex, to_vertex)] = weight

        # update the number of vertices
        self.vertices = len(self.adjacencyList)

    # Read the file containing the data of the graph
    #
    # Without weights, the number after ":" represent the adjacent vertices of 1
    # 1: 2 3 4
    #
    # With weights, the number after "," represent the weight
    # associated for edge (1,2)
    # 1: (2,1) (3,2) (4,5)

    def readGraph(self, filename):

        with open(filename) as file_object:
            for line in file_object:
                if line.strip() == "":
                    print("Empty line here in file...")
                    continue

                splittedLine = line.strip().split(":")
                if len(splittedLine) != 2:
                    print("Error in format of file!!!")
                    return

                from_vertex = splittedLine[0]

                edges = splittedLine[1]

                splittedEdge = edges.strip().split(" ")

                for edge in splittedEdge:
                    try:
                        e, w = edge.split(',')
                        edgefinal = e.strip('(')
                        weight = w.strip(')')
                        self.addEdge(int(from_vertex), int(edgefinal), int(weight))

                    except:
                        self.addEdge(int(from_vertex), int(edge.strip()))



    def printEdges(self):

        print(f"Total nodes: {self.verticesNum} \n")

        print(f"Edges represented by adjacencyList:")

        for edge in self.adjacencyList:
            print(f"{edge} :{self.adjacencyList[edge]}")

        if len(self.weights) != 0:
            print(f"Weights associated with the edges:")
            for weight in self.weights:
                print(f"{weight} :{self.weights[weight]}")

