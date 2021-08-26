import unittest
from unittests.check_dfs_tree import check_dfs
from unittests.graphs import graph1, graph2
from viz import dfs
from viz import draw


class TestDfs(unittest.TestCase):

    def test_traverse_1(self):
        traverse_edges = [x for x in dfs.DFS(1, graph1)]
        self.assertTrue(check_dfs(draw.edge_list(graph1), traverse_edges))

    def test_traverse_2(self):
        traverse_edges = [x for x in dfs.DFS(1, graph2)]
        self.assertTrue(check_dfs(draw.edge_list(graph2), traverse_edges))
