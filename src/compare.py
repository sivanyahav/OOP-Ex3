import json
import networkx as nx
from networkx.readwrite import json_graph
from time import time

from GraphAlgo import GraphAlgo


class compare_nx:
    @staticmethod
    def load_from_json(filename: str):
        gr = nx.DiGraph()
        try:
            with open(filename, "r") as f:
                dict_graph = json.load(f)
                for dic in dict_graph["Nodes"]:
                    gr.add_node(dic["id"])
                for dic in dict_graph["Edges"]:
                    gr.add_edge(dic["src"], dic["dest"], weight=dic["w"])
        except IOError as e:
            print(e)
        return gr


if __name__ == '__main__':
    """---------------shortest_path(src=1, dest=2) compare---------------"""

    print("test 1- S_P")
    g = compare_nx.load_from_json('../data/G_10_80_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_10_80_0.json')

    start = time()
    f = nx.shortest_path(g, 1, 2, weight='weight')
    print(f'shortest_path-nx: {time() - start}')
    print("nx: ", f)

    start = time()
    algo.shortest_path(1, 2)
    print(f'shortest_path-Python: {time() - start}')
    print("algo: ", algo.shortest_path(1, 2))

    print("test 2- S_P")

    g = compare_nx.load_from_json('../data/G_100_800_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_100_800_0.json')

    start = time()
    f = nx.shortest_path(g, 1, 2, weight='weight')
    print(f'shortest_path-nx: {time() - start}')
    print("nx: ", f)

    start = time()
    algo.shortest_path(1, 2)
    print(f'shortest_path-Python: {time() - start}')
    print("algo: ", algo.shortest_path(1, 2))

    print("test 3- S_P")
    g = compare_nx.load_from_json('../data/G_1000_8000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_1000_8000_0.json')

    start = time()
    f = nx.shortest_path(g, 1, 2, weight='weight')
    print(f'shortest_path-nx: {time() - start}')
    print("nx: ", f)

    start = time()
    algo.shortest_path(1, 2)
    print(f'shortest_path-Python: {time() - start}')
    print("algo: ", algo.shortest_path(1, 2))

    print("test 4- S_P")
    g = compare_nx.load_from_json('../data/G_10000_80000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_10000_80000_0.json')

    start = time()
    f = nx.shortest_path(g, 1, 2, weight='weight')
    print(f'shortest_path-nx: {time() - start}')
    print("nx: ", f)

    start = time()
    algo.shortest_path(1, 2)
    print(f'shortest_path-Python: {time() - start}')
    print("algo: ", algo.shortest_path(1, 2))

    print("test 5- S_P")
    g = compare_nx.load_from_json('../data/G_20000_160000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_20000_160000_0.json')

    start = time()
    f = nx.shortest_path(g, 1, 2, weight='weight')
    print(f'shortest_path-nx: {time() - start}')
    print("nx: ", f)

    start = time()
    algo.shortest_path(1, 2)
    print(f'shortest_path-Python: {time() - start}')
    print("algo: ", algo.shortest_path(1, 2))

    print("test 6- S_P")
    g = compare_nx.load_from_json('../data/G_30000_240000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_30000_240000_0.json')

    start = time()
    f = nx.shortest_path(g, 1, 2, weight='weight')
    print(f'shortest_path-nx: {time() - start}')
    print("nx: ", f)

    start = time()
    algo.shortest_path(1, 2)
    print(f'shortest_path-Python: {time() - start}')
    print("algo: ", algo.shortest_path(1, 2))

    """---------------connected components compare---------------"""

    print("test 1-SCC")
    g = compare_nx.load_from_json('../data/G_10_80_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_10_80_0.json')

    start = time()
    f = nx.kosaraju_strongly_connected_components(g)
    print(f'scc-nx: {time() - start}')

    start = time()
    algo.connected_components()
    print(f'scc-Python: {time() - start}')

    print("test 2-SCC")

    g = compare_nx.load_from_json('../data/G_100_800_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_100_800_0.json')
    start = time()
    f = nx.kosaraju_strongly_connected_components(g)

    print(f'scc-nx: {time() - start}')

    start = time()
    algo.connected_components()
    print(f'scc-Python: {time() - start}')

    print("test 3-SCC")
    g = compare_nx.load_from_json('../data/G_1000_8000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_1000_8000_0.json')
    start = time()
    f = nx.kosaraju_strongly_connected_components(g)

    print(f'scc-nx: {time() - start}')

    start = time()
    algo.connected_components()
    print(f'scc-Python: {time() - start}')

    print("test 4-SCC")
    g = compare_nx.load_from_json('../data/G_10000_80000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_10000_80000_0.json')
    start = time()
    f = nx.kosaraju_strongly_connected_components(g)

    print(f'scc-nx: {time() - start}')

    start = time()
    algo.connected_components()
    print(f'scc-Python: {time() - start}')

    print("test 5-SCC")
    g = compare_nx.load_from_json('../data/G_20000_160000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_20000_160000_0.json')
    start = time()
    f = nx.kosaraju_strongly_connected_components(g)

    print(f'scc-nx: {time() - start}')

    start = time()
    algo.connected_components()
    print(f'scc-Python: {time() - start}')

    print("test 6-SCC")
    g = compare_nx.load_from_json('../data/G_30000_240000_0.json')
    algo = GraphAlgo()
    algo.load_from_json('../data/G_30000_240000_0.json')
    start = time()
    f = nx.kosaraju_strongly_connected_components(g)

    print(f'scc-nx: {time() - start}')

    start = time()
    algo.connected_components()
    print(f'scc-Python: {time() - start}')

    """---------------connected component (id=1) compare---------------"""

    print("test 1- SCC(id=1)")

    algo = GraphAlgo()
    algo.load_from_json('../data/G_10_80_0.json')

    start = time()
    algo.connected_component(1)
    print(f'scc-Python: {time() - start}')

    print("test 2- SCC(id=1)")

    algo.load_from_json('../data/G_100_800_0.json')

    start = time()
    algo.connected_component(1)
    print(f'scc-Python: {time() - start}')

    print("test 3- SCC(id=1)")

    algo.load_from_json('../data/G_1000_8000_0.json')

    start = time()
    algo.connected_component(1)
    print(f'scc-Python: {time() - start}')

    print("test 4- SCC(id=1)")

    algo.load_from_json('../data/G_10000_80000_0.json')

    start = time()
    algo.connected_component(1)
    print(f'scc-Python: {time() - start}')

    print("test 5- SCC(id=1)")

    algo.load_from_json('../data/G_20000_160000_0.json')

    start = time()
    algo.connected_component(1)
    print(f'scc-Python: {time() - start}')

    print("test 6- SCC(id=1)")

    algo.load_from_json('../data/G_30000_240000_0.json')

    start = time()
    algo.connected_component(1)
    print(f'scc-Python: {time() - start}')
