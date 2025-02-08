# I want to mention that the weight implemented in the graph.py is
# used to represent the capacity of the graph in this case

from graph import Graph
from ford_fulkerson import FlowNetwork

def main():
    graph = Graph()
    while True:
        try:
            network_file = input("Enter the name of the file with the network graph: ")
            graph.readGraph(network_file)
            break
        except FileNotFoundError:
            print("Give a valid file name!!!")

    network = FlowNetwork(graph)
    maxFlow, _ = network.FordFulkerson()
    minCut = network.findMinCut()

    print("The maximum flow is: ", maxFlow)
    print("The minimum cut edges are: ", minCut)

if __name__ == "__main__":
    main()
