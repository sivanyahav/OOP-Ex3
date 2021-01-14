import random


class Node:
    """
    This class  represents the set of operations applicable on a
    node (vertex) in a directional weighted graph.
    """

    def __init__(self, key: int = -1, pos: tuple = None):
        self.__key = key
        self.count_in_edges = 0
        self.count_out_edges = 0
        self.pos = pos

    def get_key(self):
        return self.__key

    def get_pos(self):
        return self.pos

    def set_pos(self, p: tuple):
        self.pos = p

    def random_pos(self):
        """
        Returns a random location to the Node
        """
        return random.uniform(0, 20), random.uniform(0, 20), 0

    def get_count_in_edges(self):
        """
        Returns the number of edges entering the node
        """
        return self.count_in_edges

    def get_count_out_edges(self):
        """
        Returns the number of edges get out from the node
        """
        return self.count_out_edges

    def __repr__(self):
        return '' + self.__key.__str__() + ': ' + '|edges out| ' + self.count_out_edges.__str__() + \
               ' |edges in| ' + self.count_in_edges.__str__() + ' '

    def __eq__(self, other):
        return other.get_pos() == self.pos and other.get_key() == self.__key
