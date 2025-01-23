"""BFS can answere many questions about a graph. Let (V, E) be a graph, and we have two
vertices given, s and u. Let B ⊆ V be a set of vertices. What us the maximum number
of vertices of the set B that can appear on a shortest path from s to u?"""

from graph import Graph
from collections import deque
import sys

# function to conduct BFS
def BFS(graphObject, startVertex, endVertex, verticesSet):
    queue = deque([startVertex])  # queue to store the vertices
    visited = set()  # set to store the visited vertices
    if startVertex in verticesSet:
        verticesCount = {startVertex: 1}
    else:
        verticesCount = {startVertex: 0}

    print(verticesCount)

    # run until the queue is empty
    while queue:
        # remove the current vertex from the queue
        currentVertex = queue.popleft()
        # add the vertex to the visited set
        visited.add(currentVertex)

        # visit the neighbours of the current vertex
        for neighbour in graphObject.getEdges()[currentVertex]:
            # add the neighbour to the queue if not visited
            if neighbour in verticesSet and neighbour not in visited:
                visited.add(neighbour)
                # update the distance
                verticesCount[neighbour] = verticesCount[currentVertex] + 1
                if neighbour == endVertex:
                    break
                queue.append(neighbour)

            if neighbour not in verticesSet and neighbour == endVertex:
                verticesCount[neighbour] = verticesCount[currentVertex]

    return verticesCount.get(endVertex, None)

def readPairFile(filename):
    pairs = []

    with open(filename, "r") as fileObj:
        for line in fileObj:
            if line:
                pairs = line.strip().split(' ')
                if len(pairs) != 2:
                    print("Invalid input in file")
                    return None
    return pairs

def readSetFile(filename, graph):
    setVertices = set()

    with open(filename, "r") as fileObj:
        for line in fileObj:
            vertices = line.strip().split(' ')
            for vertex in vertices:
                if int(vertex) > graph.getVerticesnum():
                    print(f"Vertex {vertex} is not in the graph")
                    return None
                setVertices.add(int(vertex))

    return setVertices

def readEdgeFile(filename, graph):

    with open(filename, "r") as fileObj:

        for line in fileObj:
            if line:
                line = line.strip().split(':')
                if len(line) != 2:
                    continue
                fromVertex = line[0].strip()
                toVertices = line[1].strip().split(' ')

                for vertex in toVertices:
                    graph.addEdge(int(fromVertex), int(vertex))


def main():

    graph = Graph(0)

    while True:
        edgeFileName = input("Enter the file name containing edges: ")
        try:
            readEdgeFile(edgeFileName, graph)
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

    while True:
        setFileName = input("Enter the file name containing set: ")

        verticesSet = readSetFile(setFileName, graph)

        if verticesSet is not None:
            break

    while True:
        pairVertex = input("Enter the file for the pair of vertices: ")

        pair = readPairFile(pairVertex)

        if pair is not None:
            break

    distance = BFS(graph, int(pair[0]), int(pair[1]), verticesSet)
    graph.printEdges()
    print(verticesSet)

    if distance is None:
        print(f"No path between {pair[0]} and {pair[1]}")
    else:
        print(f"Maximal vertices on the shortest path between {pair[0]} and {pair[1]} is {distance}")

if __name__ == "__main__":
    main()
