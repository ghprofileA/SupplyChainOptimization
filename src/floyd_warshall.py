import numpy as np
import networkx as nx

def floyd_warshall(graph: nx.Graph, blocked_paths=[]):
    nodes = list(graph.nodes)
    distance = np.full((len(nodes), len(nodes)), np.inf)

    # Initialize distance matrix with edge weights
    for i, node in enumerate(nodes):
        distance[i][i] = 0  # Distance to itself is 0
    for u, v, data in graph.edges(data=True):
        if (u, v) not in blocked_paths:
            distance[nodes.index(u)][nodes.index(v)] = data['weight']
    
    # Floyd-Warshall algorithm with blocked paths
    for k in range(len(nodes)):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    
    return distance, nodes
"""
    - graph (nx.Graph): The graph on which to perform the algorithm
    - distance (np.ndarray): Matrix of shortest path distances
    - nodes (list): List of nodes in the graph
    """