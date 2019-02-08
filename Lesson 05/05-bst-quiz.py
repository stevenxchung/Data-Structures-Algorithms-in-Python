class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.recur_insert(self.root, new_val)

    def recur_insert(self, node, new_val):
        if node.value < new_val:
            if node.left:
                self.recur_insert(node.left, new_val)
            else:
                node.left = Node(new_val)
        else:
            if node.right:
                self.recur_insert(node.right, new_val)
            else:
                node.right = Node(new_val)

    def search(self, find_val):
        return self.recur_search(self.root, find_val)

    def recur_search(self, node, find_val):
        if node:
            if node.value == find_val:
                return True
            elif node.value > find_val:
                return self.recur_search(node.left, find_val)
            else:
                return self.recur_search(node.right, find_val)
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        recur_print = self.recur_print(tree.root, '')[:-1]
        return recur_print

    def recur_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.recur_print(start.left, traversal)
            traversal = self.recur_print(start.right, traversal)
        return traversal


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

print(tree.print_tree())
