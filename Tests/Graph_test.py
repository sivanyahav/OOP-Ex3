import unittest
from src.DiGraph import DiGraph
from unittest import TestCase


class Graph_test(TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()

    def test_v_size(self):
        self.assertEqual(0, self.graph.v_size())
        for i in range(10):
            self.graph.add_node(i)
        self.assertEqual(10, self.graph.v_size())

        self.graph.remove_node(1)
        self.assertEqual(9, self.graph.v_size())

        self.graph.remove_node(1)
        self.assertEqual(9, self.graph.v_size())

        for i in range(10):
            self.graph.remove_node(i)
            self.graph.remove_node(i)
        self.assertEqual(0, self.graph.v_size())

    def test_e_size(self):
        self.assertEqual(0, self.graph.e_size())

        for i in range(20):
            self.graph.add_node(i)
        for i in range(6):
            self.graph.add_edge(1, i, 1)
        self.assertEqual(5, self.graph.e_size())

        self.graph.remove_edge(1, 2)
        self.assertEqual(4, self.graph.e_size())

        self.graph.remove_edge(1, 2)
        self.assertEqual(4, self.graph.e_size())

        self.graph.add_edge(1, 3, 1)
        self.assertEqual(4, self.graph.e_size())

        self.assertFalse(self.graph.add_edge(1, 3, 1))

        for i in range(11):
            self.graph.add_edge(2, i, 1)
        self.assertEqual(14, self.graph.e_size())

        self.graph.remove_node(1)
        self.assertEqual(9, self.graph.e_size())

    def test_get_all_v(self):
        self.assertEqual(0, len(self.graph.get_all_v()))

        for i in range(10):
            self.graph.add_node(i)
        v = self.graph.get_all_v()
        self.assertEqual(10, len(v))

        for i in range(10):
            self.assertIsNotNone(v.get(i))

    def test_all_in_edges_of_node(self):
        self.assertFalse(self.graph.all_in_edges_of_node(81))
        for i in range(10):
            self.graph.add_node(i)
        for j in range(10):
            self.graph.add_edge(j, 0, 3)

        self.assertEqual(9, len(self.graph.all_in_edges_of_node(0)))

        self.graph.add_edge(1, 0, 3)
        self.assertEqual(9, len(self.graph.all_in_edges_of_node(0)))

        self.graph.remove_node(3)
        self.assertEqual(8, len(self.graph.all_in_edges_of_node(0)))

    def test_all_out_edges_of_node(self):
        self.assertFalse(self.graph.all_in_edges_of_node(81))
        for i in range(10):
            self.graph.add_node(i)
        for j in range(10):
            self.graph.add_edge(0, j, 3)

        self.assertEqual(9, len(self.graph.all_out_edges_of_node(0)))

        self.graph.add_edge(0, 1, 3)
        self.assertEqual(9, len(self.graph.all_out_edges_of_node(0)))

        self.graph.remove_node(3)
        self.assertEqual(8, len(self.graph.all_out_edges_of_node(0)))

    def test_get_mc(self):
        for i in range(20):
            self.graph.add_node(i)
        self.assertEqual(20, self.graph.get_mc())

        self.graph.add_node(3)
        self.assertEqual(20, self.graph.get_mc())

        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(1, 3, 2)
        self.graph.add_edge(1, 4, 3)
        self.graph.add_edge(1, 5, 4)
        self.graph.add_edge(1, 7, 5)
        self.assertEqual(25, self.graph.get_mc())

        self.graph.add_edge(1, 3, 8)
        self.assertEqual(26, self.graph.get_mc())

    def create_edge_for_node(self, node_key, edge_size):
        for i in range(edge_size):
            if i == node_key:
                self.graph.add_edge(node_key, ++i, 0)
            self.graph.add_edge(node_key, i, 0)

    def test_add_edge(self):
        for i in range(30):
            self.graph.add_node(i)
        self.create_edge_for_node(0, 8)
        self.assertTrue(1 in self.graph.all_out_edges_of_node(0))
        self.assertFalse(0 in self.graph.all_out_edges_of_node(1))

        self.assertFalse(5 in self.graph.all_out_edges_of_node(4))

        self.graph.add_edge(4, 5, 0)
        self.assertTrue(5 in self.graph.all_out_edges_of_node(4))
        self.assertTrue(4 in self.graph.all_in_edges_of_node(5))
        self.assertFalse(4 in self.graph.all_out_edges_of_node(5))

        before_mc = self.graph.get_mc()
        self.graph.add_edge(4, 5, 0)
        after_mc = self.graph.get_mc()

        self.assertEqual(before_mc, after_mc)

    def test_add_node(self):
        self.graph.add_node(9)
        self.assertTrue(9 in self.graph.get_all_v().keys())

        before_mc = self.graph.get_mc()
        self.graph.add_node(9)
        after_mc = self.graph.get_mc()
        self.assertEqual(before_mc, after_mc)

    def test_remove_node(self):
        for i in range(10):
            self.graph.add_node(i)
        self.graph.add_edge(0, 4, 1)
        self.graph.add_edge(0, 5, 2)
        self.graph.add_edge(0, 1, 3)
        self.graph.add_edge(2, 0, 8)
        self.graph.add_edge(3, 2, 3)
        self.graph.add_edge(1, 0, 8)
        self.graph.add_edge(5, 4, 8)
        self.graph.add_edge(4, 3, 8)
        self.graph.add_edge(1, 2, 8)

        self.graph.remove_node(0)

        self.assertFalse(0 in self.graph.get_all_v())
        self.assertIsNone(self.graph.all_out_edges_of_node(0))
        self.assertIsNone(self.graph.all_in_edges_of_node(0))

        self.assertIsNone(self.graph.all_out_edges_of_node(0))

        self.assertFalse(0 in self.graph.all_out_edges_of_node(1))
        self.assertFalse(0 in self.graph.all_out_edges_of_node(2))

        before_mc = self.graph.get_mc()
        self.graph.remove_node(0)
        after_mc = self.graph.get_mc()
        self.assertEqual(before_mc, after_mc)

    def test_remove_edge(self):
        for i in range(10):
            self.graph.add_node(i)
        self.graph.add_edge(1, 2, 0)
        self.graph.add_edge(2, 1, 0)

        self.graph.remove_edge(1, 2)
        self.assertFalse(1 in self.graph.all_in_edges_of_node(2))
        self.assertFalse(2 in self.graph.all_out_edges_of_node(1))
        self.assertTrue(1 in self.graph.all_out_edges_of_node(2))
        self.assertTrue(2 in self.graph.all_in_edges_of_node(1))

        before_mc = self.graph.get_mc()
        self.graph.remove_edge(0, 1)
        after_mc = self.graph.get_mc()
        self.assertEqual(before_mc, after_mc)

    if __name__ == '_main_':
        unittest.main()
