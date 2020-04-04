# SWDV 610 - Data Structures
# Wyatt Castaneda
# Week 4 Review

from src import Stack

# 1. Implement a stack using linked lists

# Stack => LIFO

stack = Stack()

# Lets start by pushing 4 items onto the stack
stack.push('Wyatt')
stack.push('Castaneda')
stack.push('Hello')
stack.push('World')

# Lets peek at the first value from the stack it
# should be the last value we added to the stack
print(stack.peek())  # World

# Now lets get the size of the stack
print(stack.size())  # 4

# Lets check if its empty, at this
# point it should not be
print(stack.isEmpty())  # False

# Lets pop off the last item off
print(stack.pop())  # World

# Now lets ensure that the new last
# item was the second to last item
print(stack.peek())  # Hello

# 2. Implement a queue using linked lists

# Queue => FIFO

# 3. Implement a deque using linked lists
