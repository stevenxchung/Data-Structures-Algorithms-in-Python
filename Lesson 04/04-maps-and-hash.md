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
