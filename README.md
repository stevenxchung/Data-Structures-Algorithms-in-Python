# Data-Structures-Algorithms-in-Python

All notes from Data Structures & Algorithms offered by Grow With Google on Udacity

# Lesson 1: Introduction and Efficiency

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

# Lesson 2: List-based Collections

### What is a collection?
* A collection or container is a grouping of some variable number of data items (possibly zero) that have some shared significance to the problem being solved and need to be operated upon together in some controlled fashion

### What is a list?
* A list has all the properties of a collection but the object have an order
* There are different type of lists:
  * Arrays - Ordered list with indexes
  * Linked lists - Ordered list with no indexes
  * Stacks - List where last in first out applies
  * Queues - List where first in first out applies

# Lesson 3 Searching and Sorting

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
