import heapq
import json
import math
import random
from abc import ABC
from typing import List, Dict
import queue
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from src.GraphInterface import GraphInteface
from Node import Node
from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface, ABC):
    def __init__(self, graph: GraphInteface = None):
        super()
        self.__graph = graph

    def get_graph(self):
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        f = open(file_name, "r")
        try:
            g = DiGraph()
            dict_graph = json.load(f)
            for node in dict_graph["Nodes"]:
                if "pos" in node:
                    pos = node['pos']

                    x = float(pos.split(',')[0])
                    y = float(pos.split(',')[1])
                    z = float(pos.split(',')[2])
                    pos_tuple = (x, y, z)
                    g.add_node(node["id"], pos_tuple)
                else:
                    g.add_node(node["id"], None)

            for edge in dict_graph["Edges"]:
                g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.__graph = g
            return True
        except IOError as e:
            print(e)
            return False
        finally:
            f.close()

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        with open('../data/' + file_name, 'w', encoding='utf-8') as f:
            try:
                g = {"Nodes": [], "Edges": []}
                # save nodes
                for n in self.__graph.get_all_v().values():
                    if n.get_pos() is not None:
                        pos_st = str(n.pos)
                        new_str = pos_st[1: -1]

                        g["Nodes"].append({"id": n.get_key(), "pos": new_str})
                    else:
                        g["Nodes"].append({"id": n.get_key()})
                # save edge
                for ni in self.__graph.get_all_v().keys():
                    for ni2, w in self.__graph.all_out_edges_of_node(ni).items():
                        g["Edges"].append({"src": ni, "w": w, "dest": ni2})
                json.dump(g, f, indent=4, ensure_ascii=False)
                return True
            except IOError as e:
                print(e)
                return False
            finally:
                f.close()


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

        if id1 not in self.__graph.get_all_v().keys() or id2 not in self.__graph.get_all_v().keys():
            return float('inf'), []

        if id1 == id2:
            return 0, []

        return self.dijkstra(id1, id2)

    def dijkstra(self, src: int, dest: int) -> (float, list):
        prev = {src: -1}
        """saves for each node the previous node"""
        dist = {i: math.inf for i in self.__graph.get_all_v().keys()}
        """up date the dist"""
        dist[src] = 0
        q = []
        heapq.heappush(q, (0, src))
        """saves for each node his min weight"""
        while q:
            v = heapq.heappop(q)[1]
            for ni, w in self.__graph.all_out_edges_of_node(v).items():
                if dist[ni] > dist[v] + w:
                    dist[ni] = dist[v] + w
                    prev[ni] = v
                    heapq.heappush(q, (dist[ni], ni))
                    """push to the queue the new distance and the node_key"""
            if v == dest:
                break

        if dist[dest] == math.inf:
            """there is no path"""
            return float('inf'), []
        path = []
        p = dest

        while p != -1:
            path.insert(0, p)
            p = prev[p]
        return dist[dest], path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        scc_of_node = []
        if self.__graph.v_size() == 0 or self.__graph is None:
            return scc_of_node

        scc: list[list] = self.connected_components()

        for i in range(len(scc)):
            """go through the SCC list and check which list contains the id """
            if id1 in self.__graph.get_all_v().keys() and scc[i].__contains__(id1):
                scc_of_node = scc[i]
        scc_of_node.sort()
        return scc_of_node

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        scc = []

        if self.__graph.v_size() == 0 or self.__graph is None:
            return scc

        return self.trajan()

    def trajan(self):
        global scc_re, scc_found, index
        scc_re = []
        scc_found = set()
        index = 0
        list_ids = {}
        low_link = {}
        for node in self.__graph.get_all_v():
            if node not in scc_found:
                self.dfs(node, list_ids, low_link)
        return scc_re

    def dfs(self, node, list_ids, low_link):
        global scc_re, scc_found, index
        stack = [node]
        com: Dict[int, list] = {}
        while stack:
            node = stack[-1]
            if node not in list_ids:
                list_ids[node] = index
                low_link[node] = index
                com[index] = [node]
                index += 1
            recursive = True
            for dest in self.__graph.all_out_edges_of_node(node):
                if dest not in list_ids:
                    stack.append(dest)
                    recursive = False
                    break
            if recursive is True:
                low_node = low_link[node]
                for dest in self.__graph.all_out_edges_of_node(node):
                    if dest not in scc_found:
                        low_link[node] = min(low_link.__getitem__(node), low_link[dest])
                stack.pop()
                # found scc
                if low_link[node] == list_ids[node]:
                    com[low_link[node]].sort()
                    scc_re.append((com[low_link[node]]))

                    for key in com[low_link[node]]:
                        scc_found.update([key])
                else:
                    if low_link[node] not in com:
                        com[low_link[node]] = []
                    com[low_link[node]].extend(com[low_node])
                    for key in com[low_node]:
                        low_link[key] = low_link[node]

    def plot_graph(self) -> None:
        """
         Plots the graph.
         If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
         @return: None
        """
        x = []
        y = []
        plt.figure(figsize=(11, 11), facecolor="palevioletred")  # open new win for gui
        win = plt.axes()
        for node in self.__graph.get_all_v().values():  # add pos node to the list
            if node.get_pos() is None:
                node.set_pos(node.random_pos())
            x.append(node.get_pos()[0])
            y.append(node.get_pos()[1])
            plt.annotate(node.get_key(), (node.get_pos()[0], node.get_pos()[1]), color='black', fontsize=15)

        plt.scatter(x, y, c="deeppink", s=260)  # size of win
        xl = win.get_xlim()[1] - win.get_xlim()[0]
        yl = win.get_ylim()[1] - win.get_ylim()[0]

        for node in self.__graph.get_all_v().values():  # add edges node to the list
            for ni in self.__graph.all_out_edges_of_node(node.get_key()).keys():
                node_ni: Node = self.__graph.get_all_v().get(ni)
                dist_x_ni = node_ni.get_pos()[0] - node.get_pos()[0]
                dist_y_ni = node_ni.get_pos()[1] - node.get_pos()[1]
                plt.arrow(node.get_pos()[0], node.get_pos()[1], dist_x_ni, dist_y_ni, head_width=xl * 0.009,
                          length_includes_head=True,
                          head_length=yl * 0.025, width=xl * 0.0001 * yl,
                          color='black', fc="tan")

        plt.title('|V|=' + str(self.__graph.v_size()) + ',' + '|E|= ' + str(self.__graph.e_size()) + ')',
                  fontdict={'color': 'white', 'fontsize': 19, 'fontweight': 980})

        plt.show()

    def __eq__(self, other):
        return self.__graph == other.__graph
