class Tree:
    def __init__(self, edges):
        self.parents = dict()
        self.init(edges)

    def init(self, edges):

        for parent, vertex in edges:
            self.parents[vertex] = parent

    def is_ancestor(self, v, u):
        """
        This function is checking whether u is ancestor of v or no
        """
        while v is not None:
            v = self.parents[v]
            if v == u:
                return True
        return False


def check_dfs(graph_edges, traverse_edges):
    """
    This function is checking DFS is correct
    """
    tree = Tree(traverse_edges)
    for u, v in graph_edges:

        if not tree.is_ancestor(u, v) and not tree.is_ancestor(v, u):
            return False
    return True
