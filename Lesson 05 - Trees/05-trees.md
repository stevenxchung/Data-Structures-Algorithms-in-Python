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
