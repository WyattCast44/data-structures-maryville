# from src import Dequeue, DoubleLinkedList

from collections import deque

# l = DoubleLinkedList()

# l.append(1)
# # l.prepend(0)

# print(l.length(), l.())

queue = deque()

queue.append(1)
queue.appendleft(0)

print(queue.__len__())
