
# OOP-Ex3

### This project deals with directional weighted graph in python, we used two  interfaces to implement the graph properties in the class. 

#### the interfces and their implements: 

 1. **`GraphInterface.py`** - This interface represents an directional weighted graph.
the class that implements the interface is DiGraph.
in this class, the functions of the actions on the graph are implemented, such as adding a vertex, deleting a vertex, deleting a rib, and more..
The main data structure that we chose to use to implement the project is dictionary.
 
 2.  **`GraphAlgoInterface.py`** - this interface represents the "regular" Graph Theory algorithms including:

 * **connected component(id1)-** Finds the Strongly Connected Component(SCC) that node id1 is a part
 *  **connected components()-** Finds all the Strongly Connected Component(SCC) in the graph.

![explain](https://github.com/sivanyahav/OOP-Ex3/blob/master/data/connected.gif)
 
 * **shortestPath(int src, int dest)-** returns the shortest path between src to dest - as an ordered List of nodes keys, and his length.
  if no such path returns float('inf') and empty list. This function uses dijkstra algorithm .

![explain](https://github.com/sivanyahav/OOP-Ex3/blob/master/data/shortest.gif)
 * **Save(file)-** saves this weighted (directed) graph to the given
file name - in JSON format
 * **Load(file)-**  This method load a graph to this graph algorithm.
if the file was successfully loaded - the underlying graph of this class will be changed to the loaded one, in case the graph was not loaded the original graph should remain "as is".
 *  **plot_graph()-** Plots the graph.  
If the nodes have a position, the nodes will be placed there.  
Otherwise, they will be placed in a random but elegant manner.
exmple: ![](https://github.com/sivanyahav/OOP-Ex3/blob/master/data/readme2.png)
 
    The class that implements this interface is GraphAlgo.

3. Another class is **`Node`** which represents the data of a node in a directed weighted graph. at this department there are function like get node tag or set him, get node info or set him, and get the node key.

# Comparisons
In the wiki you can find running time comparisons between Python, Java and Networkx.
We made the comparisons on 5 graphs of different sizes (10, 100, 1000, 10000, 20,000, 30000 vertices.) For the following functions:

`connected component`

 `connected components.`

`shortest path.`
