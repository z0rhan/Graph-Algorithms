"""BFS can answere many questions about a graph. Let (V, E) be a graph, and we have two
vertices given, s and u. Let B ⊆ V be a set of vertices. What us the maximum number
of vertices of the set B that can appear on a shortest path from s to u?"""

from graph import Graph
from collections import deque, defaultdict

def BFS_shortest_paths(graphObj, startVertex, endVertex):
    distances = {vertex: float('inf') for vertex in graphObj.adjacencyList}
    distances[startVertex] = 0

    # Dictionary to store the predecessors of each vertex (for reconstructing paths)
    parents = defaultdict(list)

    # Queue for BFS (Breadth-First Search)
    queue = deque([startVertex])

    while queue:
        current_vertex = queue.popleft()

        # Check neighbors of the current vertex
        for neighbor in graphObj.adjacencyList[current_vertex]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_vertex] + 1
                queue.append(neighbor)

            # If we find a shorter path, update the predecessor list
            if distances[neighbor] == distances[current_vertex] + 1:
                parents[neighbor].append(current_vertex)

    # If the target is unreachable, return an empty list
    if distances[endVertex] == float('inf'):
        return []

    all_paths = []

    def reconstruct_paths(current_vertex, path):
        if current_vertex == startVertex:
            all_paths.append([startVertex] + path[::-1])
            return
        for parent in parents[current_vertex]:
            reconstruct_paths(parent, path + [current_vertex])

    reconstruct_paths(endVertex, [])

    return all_paths



def maximalVertices(paths, verticesSet):
    maximalVertex = 0
    print(paths)

    for path in paths:
        count = 0
        for i in path:
            if i in verticesSet:
                count += 1
        if count > maximalVertex:
            maximalVertex = count

    return maximalVertex


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

    graph = Graph()

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
        else:
            return

    while True:
        pairVertex = input("Enter the file for the pair of vertices: ")

        pair = readPairFile(pairVertex)

        if pair is not None:
            break
        else:
            return

    shortestPaths = BFS_shortest_paths(graph, int(pair[0]), int(pair[1]))
    maxVertices = maximalVertices(shortestPaths, verticesSet)

    print(
        f"Maximum number of vertices in the set B that can appear on a shortest path from {
          pair[0]} to {pair[1]} is {maxVertices}"
    )


if __name__ == "__main__":
    main()
