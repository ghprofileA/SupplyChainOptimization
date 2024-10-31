# tests/test_floyd_warshall.py

import unittest
from src.graph_builder import build_graph
from src.floyd_warshall import compute_shortest_paths, reconstruct_path

class TestFloydWarshall(unittest.TestCase):
    def setUp(self):
        # Define a simple graph
        edges = [
            ('A', 'B', 1),
            ('A', 'C', 4),
            ('B', 'C', 2),
            ('B', 'D', 5),
            ('C', 'D', 1)
        ]
        self.G = build_graph(edges, directed=True)
        self.shortest_path_lengths, self.predecessors, self.distances = compute_shortest_paths(self.G)
    
    def test_shortest_path_A_D(self):
        path = reconstruct_path(self.predecessors, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
        self.assertEqual(self.shortest_path_lengths['A']['D'], 4)
    
    def test_no_path(self):
        # Add a disconnected node
        self.G.add_node('E')
        self.shortest_path_lengths, self.predecessors, self.distances = compute_shortest_paths(self.G)
        path = reconstruct_path(self.predecessors, 'A', 'E')
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()
