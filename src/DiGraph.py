from typing import Dict

from src.GraphInterface import GraphInteface
from src.Node import Node


class DiGraph(GraphInteface):

    def __init__(self):
        self.__nodes: Dict[int, Node] = {}
        self.__neighbors: Dict[int, Dict[int, float]] = {}
        self.__connect_to_me: Dict[int, Dict[int, float]] = {}
        self.__mc = 0
        self.__count_edges = 0

    def v_size(self):
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.__nodes)

    def e_size(self):
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__count_edges

    def get_all_v(self):
        """
        return a dictionary of all the nodes in the Graph,
        each node is represented using apair  (key, node_data)
        """
        return self.__nodes

    def all_in_edges_of_node(self, id1: int):
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
        """
        if id1 in self.__nodes:
            return self.__connect_to_me.get(id1)

    def all_out_edges_of_node(self, id1: int):
        """
        return a dictionary of all the nodes connected from node_id ,
        each node is represented using a pair (key,weight)
        """
        if id1 in self.__nodes:
            return self.__neighbors.get(id1)

    def get_mc(self):
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float):
        """
        Adds an edge to the graph.
        If the edge already exists or one of the nodes dose not exists the functions will do nothing
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        """
        if id1 == id2:
            return False
        if id1 in self.__nodes.keys() and id2 in self.__nodes.keys():
            if id2 in self.__neighbors[id1].keys() and weight == self.__neighbors.get(id1).get(id2):
                return False

            if id2 not in self.__neighbors.get(id1).keys():
                self.__count_edges += 1
                self.__nodes.get(id2).count_in_edges += 1
                self.__nodes.get(id1).count_out_edges += 1

            self.__mc += 1
            self.__neighbors[id1][id2] = weight
            self.__connect_to_me[id2][id1] = weight

            return True

    def add_node(self, node_id: int, pos: tuple = None):
        """
        Adds a node to the graph.
        if the node id already exists the node will not be added
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        """

        if node_id not in self.__nodes:
            self.__mc += 1
            self.__nodes[node_id] = Node(node_id, pos=pos)
            self.__neighbors[node_id] = {}
            self.__connect_to_me[node_id] = {}
            return True
        else:
            return False

    def remove_node(self, node_id: int):
        """
        Removes a node from the graph.
        if the node id does not exists the function will do nothing
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        """
        if node_id in self.__nodes:
            self.__mc += 1

            for key in self.__connect_to_me.keys():
                if node_id in self.__connect_to_me[key].keys():
                    del self.__connect_to_me[key][node_id]

            for key in self.__neighbors.keys():
                if node_id in self.__neighbors[key].keys():
                    del self.__neighbors[key][node_id]

            self.__count_edges -= len(self.__connect_to_me[node_id])
            self.__count_edges -= len(self.__neighbors[node_id])

            del self.__neighbors[node_id]
            del self.__nodes[node_id]
            del self.__connect_to_me[node_id]

            return True

        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int):
        """
        Removes an edge from the graph.
        If such an edge does not exists the function will do nothing
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        """
        if node_id2 in self.__neighbors[node_id1]:
            del self.__neighbors[node_id1][node_id2]
            del self.__connect_to_me[node_id2][node_id1]
            self.__mc += 1
            self.__count_edges -= 1
            self.__nodes.get(node_id2).count_in_edges -= 1
            self.__nodes.get(node_id1).count_out_edges -= 1
            return True

        else:
            return False

    def __repr__(self):
        return 'Graph: |V|= ' + str(self.v_size()) + ', |E|= ' + str(self.e_size()) + ''

    def __eq__(self, other):
        return self.__nodes == other.__nodes and self.__neighbors == other.__neighbors


