import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from floyd_warshall import floyd_warshall
from graph_builder import build_graph

def visualize_floyd_warshall_matrix(distance, nodes):
    # Format and display the matrix with pandas for readability
    df = pd.DataFrame(distance, index=nodes, columns=nodes)
    df.replace(float('inf'), '∞', inplace=True)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)

    print("\nShortest Path Matrix with Blocked Paths:\n")
    print(df)
    
def main():
    edges = []
    
    # Taking edges input
    while True:
        source = input("Enter source node (or type 'done' to finish): ").strip()
        if source.lower() == 'done':
            break
        target = input("Enter target node: ").strip()
        weight = int(input("Enter weight: ").strip())
        edges.append((source, target, weight))
    
    # Creating DataFrame and saving to CSV
    edges_df = pd.DataFrame(edges, columns=['Source', 'Target', 'Weight'])
    edges_df.to_csv("data/user_graph.csv", index=False)
    
    # Prompt for blocked paths
    blocked_paths = []
    while True:
        blocked = input("Enter a blocked path in format 'source,target' (or type 'done' to finish): ").strip()
        if blocked.lower() == 'done':
            break
        source, target = blocked.split(',')
        blocked_paths.append((source.strip(), target.strip()))
    
    # Build graph
    G = build_graph(edges_df, directed=True)
    
    # Update adjacency matrix to reflect blocked paths
    distance, nodes = floyd_warshall(G, blocked_paths)
    
    # Display the shortest path matrix
    print("\nShortest Path Matrix with Blocked Paths:")
    print_matrix(distance, nodes)
    
    # Example: Calculate alternative path between specific nodes
    source_node = input("Enter source node for alternative path: ").strip()
    target_node = input("Enter target node for alternative path: ").strip()
    
    try:
        path_cost = distance[nodes.index(source_node)][nodes.index(target_node)]
        if path_cost == float('inf'):
            print(f"\nNo alternative path exists from {source_node} to {target_node}.")
        else:
            path = nx.shortest_path(G, source=source_node, target=target_node, weight='weight')
            print(f"\nAlternative path from {source_node} to {target_node}: {' -> '.join(path)}")
            print(f"Total Cost: {path_cost}")
    except ValueError:
        print("Source or target node does not exist in the graph.")

def print_matrix(matrix, nodes):
    print("       " + "   ".join(nodes))
    for i, row in enumerate(matrix):
        print("\t",f"{nodes[i]:<7}", end=" ")
        for val in row:
            if val == float('inf'):
                print("∞", end="   ")
            else:
                print(f"{val:.1f}", end="   ")
        print()


if __name__ == "__main__":
    main()
