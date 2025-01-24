"""BFS can answere many questions about a graph. Let (V, E) be a graph, and we have two
vertices given, s and u. Let B ⊆ V be a set of vertices. What us the maximum number
of vertices of the set B that can appear on a shortest path from s to u?"""

from graph import Graph
from collections import deque, defaultdict
import sys


def BFS_shortest_paths(graphObj, startVertex, endVertex):

def maximalVertices(paths, verticesSet):
    count = 0
    maximalVertex = 0
    for path in paths:
        for i in path:
            count += i
        if count > maximalVertex:
            maximalVertex = count

    return maximalVertex


# function to conduct BFS


def readPairFile(filename):
    pairs = []

    with open(filename, "r") as fileObj:
        for line in fileObj:
            if line:
                pairs = line.strip().split(" ")
                if len(pairs) != 2:
                    print("Invalid input in file")
                    return None
    return pairs


def readSetFile(filename, graph):
    setVertices = set()

    with open(filename, "r") as fileObj:
        for line in fileObj:
            vertices = line.strip().split(" ")
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
                line = line.strip().split(":")
                if len(line) != 2:
                    continue
                fromVertex = line[0].strip()
                toVertices = line[1].strip().split(" ")

                for vertex in toVertices:
                    graph.addEdge(int(fromVertex), int(vertex))


def main():

    graph = Graph(0)

    while True:
        # edgeFileName = input("Enter the file name containing edges: ")
        try:
            readEdgeFile("testgraph_1", graph)
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

    while True:
        # setFileName = input("Enter the file name containing set: ")

        verticesSet = readSetFile("testset_1", graph)

        if verticesSet is not None:
            break

    while True:
        # pairVertex = input("Enter the file for the pair of vertices: ")

        pair = readPairFile("testpair_1")

        if pair is not None:
            break

    shortestPahts = BFS_shortest_paths(graph, int(pair[0]), int(pair[1]))
    maxVertices = maximalVertices(shortestPahts, verticesSet)

    print(
        f"Maximal vertices on the shortest path between {
          pair[0]} and {pair[1]} is {maxVertices}"
    )


if __name__ == "__main__":
    main()
