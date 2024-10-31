import networkx as nx
import pandas as pd

def build_graph(edges: pd.DataFrame, directed: bool = True) -> nx.Graph:
    """
    Builds a graph from a DataFrame containing edges.

    Parameters:
    - edges (pd.DataFrame): DataFrame with columns ['Source', 'Target', 'Weight']
    - directed (bool): Whether the graph is directed

    Returns:
    - G (nx.Graph): The constructed graph
    """
    G = nx.DiGraph() if directed else nx.Graph()

    for _, row in edges.iterrows():
        G.add_edge(row['Source'], row['Target'], weight=row['Weight'])

    return G
