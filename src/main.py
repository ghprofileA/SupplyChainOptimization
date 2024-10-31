import pandas as pd
import networkx as nx
from graph_builder import build_graph
from floyd_warshall import floyd_warshall
import matplotlib.pyplot as plt

def main():
    # Prompt user for CSV file input
    csv_file = input("Enter the path to the CSV file (e.g., data/filename.csv): ").strip()
    
    try:
        # Read the selected CSV file
        edges = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"File '{csv_file}' not found. Please check the path and try again.")
        return
    except pd.errors.EmptyDataError:
        print(f"File '{csv_file}' is empty. Please provide a valid CSV file.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return
    
    # Prompt for source and target nodes
    source = input("Enter the source node : ").strip()
    target = input("Enter the target node : ").strip()
    
    # Build the graph
    G = build_graph(edges, directed=True)
    
    # Print Nodes and Edges for Verification
    print("\n--- Graph Nodes ---")
    print(list(G.nodes()))
    
    print("\n--- Graph Edges ---")
    print(list(G.edges(data=True)))
    
    # Check if nodes exist
    if source not in G.nodes:
        print(f"Source node '{source}' does not exist in the graph.")
        return
    if target not in G.nodes:
        print(f"Target node '{target}' does not exist in the graph.")
        return
    
    # Draw the graph
    pos = nx.spring_layout(G, seed=42)  # Fixed seed for consistent layout
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=12,
        font_color='black',
        font_weight='bold',
        edge_color='gray'
    )
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Supply Chain Network")
    plt.show()
    
    # Apply Floyd-Warshall algorithm
    distance, nodes = floyd_warshall(G)
    
    # Retrieve the distance
    path_cost = distance[nodes.index(source)][nodes.index(target)]
    
    if path_cost != float('inf'):
        # Reconstruct the path using NetworkX's shortest_path function
        path = nx.shortest_path(G, source=source, target=target, weight='weight')
        print(f"\nShortest path from {source} to {target}: {' -> '.join(path)}")
        print(f"Total Weight: {path_cost}\n")
        
        # Highlight the shortest path
        path_edges = list(zip(path, path[1:]))
        plt.figure(figsize=(10, 8))
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color='lightblue',
            node_size=2000,
            font_size=12,
            font_color='black',
            font_weight='bold',
            edge_color='gray'
        )
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            edge_color='red',
            width=2
        )
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=path,
            node_color='orange'
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title(f"Shortest Path: {' -> '.join(path)}")
        plt.show()
    else:
        print(f"\nNo path exists from {source} to {target}.\n")

if __name__ == "__main__":
    main()
