"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        # Use available method which is already defined in HashTable()
        hashVal = self.calculate_hash_value(string)
        # Check if hashVal exists in the table
        if self.table[hashVal] != None:
            # hashValue already exists so append string to the array
            self.table[hashVal].append(string)
        else:
            # If hashVal is not there, assign it to the string
            self.table[hashVal] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hashVal = self.calculate_hash_value(string)
        # Check if hashVal exists in the table
        if self.table[hashVal] != None:
            # Check if string exists in the table at hashVal key
            if string in self.table[hashVal]:
                return hashVal
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hashVal = (ord(string[0]) * 100) + ord(string[1])
        return hashVal


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
