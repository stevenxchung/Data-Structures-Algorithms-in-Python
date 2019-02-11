## Lesson 6: Graphs

### What is a Graph?
* The purpose of a graph is to show how different things are connected to one another (sometimes called a network)
* A tree is actually a specific type of graph
* Nodes (circles) and edges (lines) could contain data, edges typically contain data about the strength of node A to node B

### What typs of properties do graphs have?
* Direction - relationship between two nodes only applies one way, it's important to make sure all directional graphs are DAG (Directed Acyclic Graph)
* Connectivity - measures the minimum number of edges to be removed for a graph to be disconnected
* Using connectivity, we can describe connections as:
  * Disconnected - Some node or group of nodes have no connection with the rest of the graph
  * Weakly connected - Only replacing all of the directed edges with undirected edges can cause the directed graph to be connected
  * Connected - There is some path between one node and every other node (undirect graphs)
  * Strongly connected - Strongly connected directed graphs must have a path from every node and every other node. So, there must be a path from A to B and B to A.

### In what ways can we represent a graph?
* Edge lists - each edge in the graph has nodes associated with it and can be stored in an array, e.g. [[0, 1], [1, 2], [1, 3], [2, 3]], where [0, 1] is one edge
* Adjacency lists - each node in the graph has nodes associated with it and can be stored in an array, e.g. [[1], [0, 2, 3], [1, 3], [1, 2]], where [1] at index 0 corresponds to node 0
* Adjacency matrices - similar to the adjacency list, these matrices have indexes which correspond to a particular node and matrix lists which corresponds to connected nodes, e.g. [[0, 1, 0, 0], [1, 0, 0, 0]] means that only node 1 is connected to node 0

### What are some methods for graph traversal?
* DFS on graphs operates under the same principles as DFS on trees, DFS will search until there are no longer any new nodes
  * DFS will add new nodes to the stack
  * The efficiency for DFS on graphs are *O(|m edges| + |n nodes|)*
* BFS on graphs are very similar to DFS except it will look through every edge connected to a particular node before moving on
  * BFS will add new nodes to a queue
  * The efficiency for BFS on graphs are also *O(|m edges| + |n nodes|)*

### What are some notable paths for graphs?
* There are Eulerian paths:
  * Travels through every edge in a graph at least once
  * An Eulerian cycle traverses each edge at least once and end up at the same node
  * Even degree - every node in the graph has an even number of edges connected
  * Graphs can only have Eulerian cycles if they have an even degree
  * The efficiency of Eulerian path is *O(|n edges|)*
* There are also Hamiltonian paths:
  * Travels through every node in a graph at least once
  * A Hamiltonian cycle will start and end at the same node
