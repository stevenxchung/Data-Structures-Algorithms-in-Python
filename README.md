# Data-Structures-Algorithms-in-Python

All notes from Data Structures & Algorithms offered by Grow With Google on Udacity

## Lesson 1: Introduction and Efficiency

### What is efficiency?
* Efficiency or complexity refers to how well you are using the computer's resources to get a particular job done
* We can think about this in terms of space and time:
  * How much storage is needed?
  * How much time does it take for the job to complete?

### How can we describe code efficiency to others?
* Use Big-O notation to do so: *O(n)*
* What does *n* represent in *O(n)*?
  * *n* represents the length of the input
* Normally use approximation when talking about Big-O notation: *O(n + 1) ~= O(n)*
* Big-O is often discussed in the worst case scenario, however there is also a best case and an average case as well
* Big-O can be used to describe space and time efficiency

## Lesson 2: List-based Collections

### What is a collection?
* A collection or container is a grouping of some variable number of data items (possibly zero) that have some shared significance to the problem being solved and need to be operated upon together in some controlled fashion

### What is a list?
* A list has all the properties of a collection but the object have an order
* There are different type of lists:
  * Arrays - Ordered list with indexes
  * Linked lists - Ordered list with no indexes
  * Stacks - List where last in first out applies
  * Queues - List where first in first out applies

## Lesson 3 Searching and Sorting

### What is Binary Search?
* Binary search essentially takes advantage of sorted arrays by initiating a comparison of the value at the middle of the array to see if the computer should search the upper or lower half of the array
* The efficiency of binary search is *O(log(n))*

### What is Recursion?
* Recursion is when a function calls itself

### What is Bubble Sort?
* Bubble sort is a naive approach to sorting (need to compare each element in the array)
* The efficiency of bubble sort is *O(n^2)* for the worst and average case. In the best case, the bubble sort would have an efficiency of *O(n)*

### What is Merge Sort?
* Merge sort is taking a big array, break it down, sort, then build it back up together after sorting is completed (divide and conquer)
* The efficiency of merge sort is *O(n*log(n))*

### What is a Quick Sort?
* Quick sort utilizes pivots to move values around based on whichever number is bigger or smaller
* The efficiency of quick sort is *O(n^2)* for the worst case and *O(n*log(n)) for the average and best case

## Lesson 4: Maps and Hashing

### What are Maps?
* Maps have a key-value structure, you can use a key to get the value at a particular location

### What are Sets?
* Sets are similar to a list but they do not allow for repeated elements, there is no particular order for a set
* Keys in a map are known as a set
* Each key only exists once in a map (think of words in a dictionary)

### What are Hashes?
* Using a hash function will enable one to do look-ups in constant-time *O(1)*, whereas most look-up algorithms are in linear-time *O(n)*
* Hash functions convert a value into a hash value to enable faster look-ups
* Because collisions can happen when hashing we can use buckets to store similar indexes, because this creates an array, time complexity becomes *O(n)*

### What is a Load Factor?
* A load factor is mathematically defined as *Load Factor = Number of Entries / Number of Buckets*
* The purpose of a load factor is to give us a sense of how "full" a hash table is
* Load factor enables one to rehash if the number of empty buckets is much greater than the number of entries or if the number of entries is getting close to the max number of buckets

### What are Hash Maps?
* Hash maps combine maps and hashing to allow for constant-time look-ups, they utilize the property of maps to get values by their key
* You can also use hash maps with string keys by creating a hash function which will convert letters into numbers

## Lesson 5: Trees

### What are Trees?
* Trees are data structures which start from a *root* whereby *branches* can be added
* A tree is really just an extension of a linked-list, there is one node which points to many other nodes
* There are several important terminologies when it comes to trees:
  * *Levels* are how many connections it takes to reach the root + 1
  * Nodes in trees can have *parents* and *childs*, some nodes can be both
  * Nodes at the descendant level (higher level) are called *leaves*
  * Node *height* is the distance from the root to the furthest leaf
  * Node *depth* is the distance from the leaves to the root

### What are some techniques used to traverse trees?
* DFS (Depth-First-Search) suggests exploring children nodes first
  * Pre-order traversals start at the root node and go down the left sub-tree to the right sub-tree
  * In-order traversals start at the left sub-tree to the root node and then to the right sub-tree (starting at the left-most node in that sub-tree finishing at the right-most node)
  * Post-order nodes start at the left sub-tree to the right sub-tree (starting at the left-most node in that sub-tree finishing at the parent node) and then finish at the root node
* BFS (Breadth-First-Search) suggests visiting all nodes on the same level before exploring children nodes
  * Level order algorithms are used to implement BFS, the convention is to start from the top level and move across all elements from left to right
* For more information on tree traversals: [tutorialspoint](https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal.htm)

### What are Binary Trees?
* Binary trees have at most two children for each parent node
* We are stuck with linear-time search, *O(n)* since we have to traverse all nodes
* Delete also has linear-time since we have to search for the element first
* Inserting a node in a tree depends on whether or not the parent node already has two children, the worst case is when one has to traverse down the to the farthest leaf from the root node (efficiency of *O(log(n)*)

### What is a Binary Search Tree?
* A BST (binary search tree) is a particular binary tree which orders nodes starting from the left to right
* A binary search tree efficiency is actually *O(log(n))* (the height of the tree) because of the way it is ordered
* A BST is unbalanced if there is one child for each parent, this causes the efficiency to drop to *O(n)* (the worst case scenario)

### What is a Heap?
* A heap is a tree where elements are arranged in increasing or decreasing order such that the root node is the minimum or maximum in the tree
  * In a max heap the parent value is always greater than the child
  * In a min heap the parent value is always the smallest
* A heap must be *complete* such that all levels except the last are filled, values are filled in from left to right
* Searching a heap is a linear-time operation

### What if a value to be inserted is bigger than the parent value?
* One would *heapify* or reorder the heap such that the inserted value becomes the parent
* Extracting out a value could cause a heap to heapify
* The worst case scenario for inserting and extracting is *O(log(n))*

### How is a Heap implemented?
* Heaps are often sorted as arrays which makes it easy to implement a heap (if sorted in descending order) since the parent is always greater than the child
* Using an array in this case would also save space

### What are Self-balancing Trees?
* Self-balancing trees tries to minimize the number of levels that it uses by filling up all levels before moving to the next level
* A Red-Black Tree is the most common self-balancing tree and is an extension of a BST, there are several of rules which constitute this tree:
 1. Values must be either red or black
 2. Every parent that has only one child must have another null node attached (colored black)
 3. If a node is red both of its children must be black
 4. The root node must be black
 5. Every path to its descendant null nodes must contain the same number of black nodes
* The efficiency of these trees are O(log(n)) due to the balancing rules

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

## Lesson 7: Shortest Path Algorithm

### What is the Shortest Path Problem?
* The shortest path in a graph is where sum of the edges in a path are as small as possible
* If the graph is unweighted, the shortest path is one with the least number of edges
* BFS is actually an optimal algorithm for an unweighted graph

### What is Dijkstra's Algorithm?
* A solution to the shortest path problem, uses *distance* to determine the shortest path
* Distance is the sum of edge weights on a path between the starting point and some node
* Typical implementation of Dijkstra's uses a min priority queue, where minimum distances are removed efficiently, e.g. starting node at 0
* Dijkstra's algorithm is known as a *greedy* algorithm because it picks the best available option at the moment
* The efficiency of Dijkstra's is *O(|n nodes|^2)*

### What is the Knapsack Problem?
* Uses weight constraint to place optimal number of items into a "knapsack"
* A common strategy is to implement a brute force solution where the efficiency is *O(2^(n objects))*

### What would be a faster algorithm?
* Maximize the weight for the smallest weights possible for the brute force solution
* The efficiency of this algorithm becomes *O((weight limit) * (n elements))*, a pseudo-polynomial-time solution

### How is Dynamic Programming used?
* Dynamic programming can be used to solve the knapsack problem by breaking a problem into smaller parts
* A lookup table is typically used in dynamic programming problems to store solutions to subproblems
* Storing precomputed values into a lookup table is also known as memoization, values do not need to be recomputed again for the lookup (kind of like a cache)

### What is the Traveling Salesman Problem?
* TSP (Traveling Salesman Problem) tries to address the fastest way to traverse all nodes (an optimization problem)
* TSP is a NP-hard (Nondeterministic Polynomial-time) problem (problems with no known algorithm to solve in polynomial time, the knapsack problem falls into this category as no true polynomial time solution is known)

### What are Exact and Approximate algorithms?
* Exact algorithms do not happen in polynomial time but will solve the problem, e.g. brute force and dynamic programming
* Approximate algorithms are sometimes able to find a near optimal solution to the problem, e.g.
Christofides Algorithm (turns a graph into a tree where the starting node is the root)
* Christofides guarantees that the produced path will be at most 50% longer than the shortest route
