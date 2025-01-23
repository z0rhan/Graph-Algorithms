"""BFS can answere many questions about a graph. Let (V, E) be a graph, and we have two
vertices given, s and u. Let B ⊆ V be a set of vertices. What us the maximum number
of vertices of the set B that can appear on a shortest path from s to u?"""

from graph import Graph
from collections import deque

def BFS(graphObject, startVertex, endVertex):
    queue = deque([startVertex])
    visited = set()
    distance = {startVertex: 0}

    while queue:
        currentVertex = queue.popleft()
        visited.add(currentVertex)

        if currentVertex == endVertex:
            return distance[currentVertex]

        for neighbour in graphObject.getEdges()[currentVertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                distance[neighbour] = distance[currentVertex] + 1
                queue.append(neighbour)

    return distance[endVertex]

def getSet():
    verticesSet = set()
    vertices = input("Enter the vertices in the set separated by commas(x,y,z,...): ")
    verticesList = vertices.split(',')

    for vertex in verticesList:
        if not vertex.isdigit():
            print("Invalid input")
            return None

    for vertex in verticesList:
        verticesSet.add(int(vertex))


def addEdges(graphObject):
    while True: 
        edge = input("Enter the edges in the form {u,v}: ")

        splittedEdge = edge.split(',')

        if len(splittedEdge) != 2:
            print("Invalid input")
            continue

        startVertex = splittedEdge[0]
        endVertex = splittedEdge[1]

        if not startVertex.isdigit() or not endVertex.isdigit():
            print("Invalid input")
            continue

        graphObject.addEdge(int(startVertex), int(endVertex))


def main():
    numOfVertices = int(input("Enter the number of vertices: "))
    graph = Graph(numOfVertices)

    while True:
        command = input("Enter [A]dd to add edges, [F]ind to find the max vertices or [Q]uit to quit: ")
        if command == "A":
            addEdges(graph)

        elif command == "F":
            startVertex = int(input("Enter the start vertex: "))
            endVertex = int(input("Enter the end vertex: "))
            print(BFS(graph, startVertex, endVertex))

        elif command == "Q":
            break

        else:
            print("Invalid command")

    graph.getEdges()

if __name__ == "__main__":
    main()
