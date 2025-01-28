"""BFS can answere many questions about a graph. Let (V, E) be a graph, and we have two
vertices given, s and u. Let B ⊆ V be a set of vertices. What us the maximum number
of vertices of the set B that can appear on a shortest path from s to u?"""

from graph import Graph
from collections import deque, defaultdict

def BFS_ShortestPaths(graphObj, startVertex, endVertex):
    # Dictionary to store distances of all vertices
    distances = {vertex: float('inf') for vertex in graphObj.adjacencyList}
    distances[startVertex] = 0

    # Dictionary to store the parents of each vertex (for reconstructing paths)
    parents = defaultdict(list)

    # Queue for BFS (Breadth-First Search)
    queue = deque([startVertex])

    # Run until the queue is not empty
    while queue:
        currentVertex = queue.popleft()

        # Check neighbors of the current vertex
        for neighbor in graphObj.adjacencyList[currentVertex]:
            # If not reached before
            if distances[neighbor] == float('inf'):
                # Update the shortest distance
                distances[neighbor] = distances[currentVertex] + 1
                queue.append(neighbor) # Update the queue

            # Add all the vertices that lead to neigbour with the shortest path
            if distances[neighbor] == distances[currentVertex] + 1:
                parents[neighbor].append(currentVertex)

    # If the target is unreachable, return None 
    if distances[endVertex] == float('inf'):
        return None

    allPaths = [] # To store all possible shortest paths
    
    # To reconstruct the shortest paths available 
    def reconstructPaths(currentVertex, path):
        # If reached the starting vertex add it to the start of the path
        if currentVertex == startVertex:
            allPaths.append([startVertex] + path)
            return # End the function
        
        # Continue adding the parent to the path from the endVertex recursively
        for parent in parents[currentVertex]:
            reconstructPaths(parent, [currentVertex] + path)
    
    # Function call to reconstruct path starting from the end vertex
    reconstructPaths(endVertex, [])

    return allPaths



def maximalVertices(paths, verticesSet):
    """
    returns the maximal occurences of vertices in the shortest path
    that belongs to the given set
    """
    maximalVertex = 0

    # Iterate through all the shortest paths given
    for path in paths:
        count = 0
        # Iterate though all vertices in a path
        for i in path:
            if i in verticesSet:
                count += 1
        # Update maximalVertices if possible
        if count > maximalVertex:
            maximalVertex = count

    return maximalVertex


def readPairFile(filename):
    """ 
    reads the file containing the start and end vertex
    """
    pairs = []

    with open(filename, "r") as fileObj:
        for line in fileObj:
            if line:
                pairs = line.strip().split(" ")
                if len(pairs) != 2:
                    print("Invalid input in file!!! Enter a file with start and end vertex pair.")
                    return None
    return pairs


def readSetFile(filename, graph):
    """
    reads the file containing the set of vertices
    returns a set of those vertices
    """
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
    """
    reades file the contains all possible edges and adds them 
    to the graph object provided
    """
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
    # initialize a graph object
    graph = Graph()

    while True:
        edgeFileName = input("Enter the file name containing edges: ")

        try:
            readEdgeFile(edgeFileName, graph)
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

    while True:
        setFileName = input("Enter the file name containing set or leave empty for empty set: ")

        # if the file is empty, make an empty set
        if setFileName == "":
            verticesSet = []
            break

        else:
            try:
                verticesSet = readSetFile(setFileName, graph)
            except FileNotFoundError:
                print("File not found. Please enter a valid file name.")

            if verticesSet is not None:
                break
            else:
                return

    while True:
        pairVertex = input("Enter the file for the pair of vertices: ")

        try:
            pair = readPairFile(pairVertex)
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

        if pair is not None:
            break
        else:
            return
    
    shortestPaths = BFS_ShortestPaths(graph, int(pair[0]), int(pair[1]))

    if shortestPaths is None:
        print("Target vertex unreachable!!!")

    print(f"All possible shortest paths: {shortestPaths}")
    
    maxVertices = maximalVertices(shortestPaths, verticesSet)

    print(
        f"Maximum number of vertices in the set B that can appear on a shortest path from {
          pair[0]} to {pair[1]} is {maxVertices}"
    )


if __name__ == "__main__":
    main()
