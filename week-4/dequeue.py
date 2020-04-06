# SWDV 610 - Data Structures
# Wyatt Castaneda
# Week 4 Review - Part 3

from src import Dequeue


# 3. Implement a deque using linked lists

queue = Dequeue()

# Lets start by adding some data
queue.append(0)
queue.append(1)
queue.append(2)

# Let check that the length is three
print(queue.length())  # 3

# Lets try grabbing the first item
print(queue.get_start())  # 0

# The list length should now be two
print(queue.length())  # 2

# Okay lets try grabbing the end item
print(queue.get_end())  # 2

# And now the queue should only have one item
print(queue.length())

# Now lets prepend to the list
queue.prepend(-1)

# Lets print the queue, should have two items
print(queue.display())  # -1, 1

quit()
