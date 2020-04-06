# SWDV 610 - Data Structures
# Wyatt Castaneda
# Week 4 Review - Problem 2

from src import Queue

# 2. Implement a queue using linked lists

queue = Queue()

# Lets start by adding 4 items to the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

# Now lets ensure the queue is not empty
print(queue.isEmpty())  # False

# Now lets get the first item on the queue
print(queue.dequeue())  # 1

# Now lets get the new first item on the queue
print(queue.dequeue())  # 2


# Now lets ensure the size is two
print(queue.size())  # 2

quit()
