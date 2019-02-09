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
