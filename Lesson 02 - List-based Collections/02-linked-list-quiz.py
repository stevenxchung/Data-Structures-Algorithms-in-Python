"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Need counter since this is a linked-list to keep track
        counter = 1
        node = self.head
        if position < 1:
            return None
        while node and counter <= position:
            # Return element if counter matches requested position
            if counter == position:
                return node
            node = node.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        node = self.head
        if position > 1:
            # Begin going through linked-list
            while node and counter < position:
                # When true insert new element before element at position index
                if counter == position - 1:
                    # Points to the next node (referenced from initial element at position-1)
                    new_element.next = node.next
                    # Points to new element (referenced from initial element at position-1)
                    node.next = new_element
                node = node.next
                counter += 1
        # If position is the head node insert new element behind the head
        elif position == 1:
            # New element's neighbor will be the old head node at a new position
            new_element.next = self.head
            # New element will be at position 1
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        node = self.head
        previous = None
        while node.value != value and node.next:
            # Points to node
            previous = node
            # Node points to node.next
            node = node.next
        if node.value == value:
            if previous:
                # Previous's neighbor will be node.next
                previous.next = node.next
            else:
                # Otherwise the head node will point to node.next
                self.head = node.next


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
