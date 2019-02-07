import numpy as np
from numpy import arange

# One of your coworkers comes to you with a hash function that divides a group of values by 100, and uses the remainder as a key. The values are 100 numbers that are all multiples of 5. What is the load factor?
# Load factor is 1 since there are 100 values and 100 buckets so 100/100 = 1

# He thinks it's a little slow - what number would you recommend his function to divide by rather than 100 to speed it up?
# 107

# Test code
def loadFactor(buckets):
  arr = np.arange(0, 99)
  print('Using {} buckets'.format(buckets))
  for num in arr:
    print((num * 5) % buckets)
  print('Complete!\n')

# 87 is better than 125 but it's less than 100 so it will have collisions
loadFactor(87)

# The best answer
loadFactor(107)

# 125 will have a lot of collisions
loadFactor(125)

# 1001 is better but it will create a ton of left-over buckets
loadFactor(1001)
