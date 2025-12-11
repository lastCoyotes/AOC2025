from collections import defaultdict
import numpy as np

class Graph:
    def __init__(self):
        self.edges = defaultdict(set)
    def add_edge(self, u, v):
        self.edges[u].add(v)
    def get_node_index(self):
        nodes = set()
        for k, v in self.edges.items():
            nodes.add(k)
            nodes.update(v)
        nodes = list(nodes)
        nodes.sort()
        return {node: i for i, node in enumerate(nodes)}
    def get_adj_matrix(self):
        node_index = self.get_node_index()
        n = len(node_index)
        mat = np.zeros((n, n))
        for u, s in self.edges.items():
            for v in s:
                i = node_index[u]
                j = node_index[v]
                mat[i][j] = 1
        return mat
    def get_num_paths(self, u, v):
        node_index = self.get_node_index()
        i = node_index[u]
        j = node_index[v]
        n = len(node_index)
        A = self.get_adj_matrix()
        total = 0
        Ak = A.copy()
        for k in range(n):
            total += int(Ak[i][j])
            Ak @= A
        return total

graph = Graph()
with open('input/11.txt', 'r') as f:
    for line in f.readlines():
        tokens = line.strip().split()
        left = tokens[0][:-1]
        for right in tokens[1:]:
            graph.add_edge(left, right)

print(graph.get_num_paths('you', 'out'))

svr_to_dac = graph.get_num_paths('svr', 'dac')
svr_to_fft = graph.get_num_paths('svr', 'fft')

dac_to_fft = graph.get_num_paths('dac', 'fft')
fft_to_dac = graph.get_num_paths('fft', 'dac')

dac_to_out = graph.get_num_paths('dac', 'out')
fft_to_out = graph.get_num_paths('fft', 'out')

print(svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out)