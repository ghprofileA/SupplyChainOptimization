import numpy as np
import networkx as nx

def floyd_warshall(graph: nx.Graph):
    """
    - graph (nx.Graph): The graph on which to perform the algorithm
    - distance (np.ndarray): Matrix of shortest path distances
    - nodes (list): List of nodes in the graph
    """
    nodes = list(graph.nodes)
    distance = np.full((len(nodes), len(nodes)), np.inf)

    # Initialize the distance matrix
    for i, node in enumerate(nodes):
        distance[i][i] = 0
    for u, v, data in graph.edges(data=True):
        distance[nodes.index(u)][nodes.index(v)] = data['weight']

    # Floyd-Warshall algorithm
    for k in range(len(nodes)):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance, nodes
