import pandas as pd
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
import PIL
import io


def buffer_plot_and_get(fig):
    """
    matplotlib figure to PIL image
    :param fig: matplotlib figure
    :return: PIL image
    """
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return PIL.Image.open(buf)


def edge_list(graph):
    """

    :param graph: graph in format {vertex_1 : [neigh_1, neigh_2, ...], vertex_2 : [...]}
    :return: list of edges [(v1, v2), ...]
    """
    edges = [None for vertex in graph for _ in graph[vertex]]
    index = 0
    for v in graph:
        for u in graph[v]:
            edges[index] = (v, u)
            index += 1
    return edges


def color_map_iterator(nx_graph, traverse, edge_traverse):
    """
    Returns coloring iterator for each frame of animation.
    Returns iterator which produce list of colors for nodes and edges in every iteration.
    Order of edges and nodes in list depends on order of them in nx_graph

    :param nx_graph: networkx graph
    :param traverse: vertices in traverse order
    :param edge_traverse: edges in traverse order
    :return: iterator
    """
    colors = pd.DataFrame(np.zeros_like(nx_graph.nodes(), dtype='int'), index=nx_graph.nodes(), columns=['color'])
    index = pd.MultiIndex.from_tuples(nx_graph.edges())
    edge_colors = pd.DataFrame(np.zeros(len(nx_graph.edges()), dtype='int')
                               , index=index, columns=['color'])

    def get_colors():
        nc = np.array(['teal', 'aqua'])
        ec = np.array(['rosybrown', 'gold'])

        return np.choose(colors['color'], nc), np.choose(edge_colors['color'], ec)

    def color_update():

        yield get_colors()
        yield get_colors()

        for node, edge in zip(traverse, edge_traverse):
            if edge in edge_colors.index:
                edge_colors.loc[edge]['color'] = 1
            if edge[::-1] in edge_colors.index:
                edge_colors.loc[edge[::-1]]['color'] = 1

            yield get_colors()

            colors.loc[node]['color'] = 1
            yield get_colors()

        yield get_colors()
        yield get_colors()

    return color_update()


def generate_gif(graph, edge_traverse, file_name="graph_traverse"):

    """
    This function generates GIF image of graph traverse

    :param graph: graph in format {vertex_1 : [neigh_1, neigh_2, ...], vertex_2 : [...]}
    :param edge_traverse: edges in order of traverse [(v1, v2), ...]
    :param file_name: name of output file with gif image
    """

    edges = edge_list(graph)
    traverse = [edge[1] for edge in edge_traverse]
    G = nx.Graph(edge_list(graph))

    fig = plt.figure()
    axes = fig.add_subplot()
    axes.axis('off')
    pos = nx.spring_layout(G)

    images = []
    for color_map, edges_cmap in color_map_iterator(G, traverse, edge_traverse):
        nx.draw(G, with_labels=True, font_weight='bold', ax=axes,
                node_color=color_map, edge_color=edges_cmap, pos=pos)
        img = buffer_plot_and_get(fig)
        images.append(img)
        axes.clear()
        axes.axis('off')

    images[0].save(file_name + '.gif',
                   save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)
