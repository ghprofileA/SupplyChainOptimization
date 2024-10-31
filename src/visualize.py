import matplotlib.pyplot as plt
import plotly.graph_objects as go
import networkx as nx

def visualize_with_matplotlib(G, pos, path=None, node_types=None):
    """
    Visualize the graph using Matplotlib.
    """
    plt.figure(figsize=(10, 8))
    
    # Define node colors based on type
    if node_types:
        color_map = []
        for node in G.nodes():
            if node_types.get(node) == 'Warehouse':
                color_map.append('lightgreen')
            elif node_types.get(node) == 'Distribution Center':
                color_map.append('lightblue')
            else:
                color_map.append('lightcoral')
    else:
        color_map = 'lightblue'
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=color_map)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->', arrowsize=20, edge_color='gray')
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    
    # Highlight the shortest path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange', node_size=700)
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')
    
    # Add legend
    if node_types:
        import matplotlib.patches as mpatches
        green_patch = mpatches.Patch(color='lightgreen', label='Warehouse')
        blue_patch = mpatches.Patch(color='lightblue', label='Distribution Center')
        coral_patch = mpatches.Patch(color='lightcoral', label='Retail Outlet')
        plt.legend(handles=[green_patch, blue_patch, coral_patch])
    
    # Set title and remove axis
    plt.title('Supply Chain Network with Optimized Route', fontsize=15)
    plt.axis('off')
    plt.show()

def visualize_with_plotly(G, pos, path=None):
    """
    Visualize the graph using Plotly for interactivity.
    """
    # Edge traces
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines')
    
    # Node traces
    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition="bottom center",
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=20,
            color=[len(list(G.neighbors(n))) for n in G.nodes()],
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            )
        )
    )
    
    # Path traces
    path_edges = list(zip(path, path[1:])) if path else []
    path_x = []
    path_y = []
    for edge in path_edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        path_x += [x0, x1, None]
        path_y += [y0, y1, None]
    
    path_trace = go.Scatter(
        x=path_x, y=path_y,
        line=dict(width=4, color='red'),
        hoverinfo='none',
        mode='lines')
    
    # Combine all traces
    data = [edge_trace, path_trace, node_trace]
    
    # Define layout
    layout = go.Layout(
        title='Supply Chain Network with Optimized Route',
        titlefont_size=20,
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20,l=5,r=5,t=40),
        annotations=[ dict(
            text="",
            showarrow=False,
            xref="paper", yref="paper") ],
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
    
    # Create figure and display
    fig = go.Figure(data=data, layout=layout)
    fig.show()
