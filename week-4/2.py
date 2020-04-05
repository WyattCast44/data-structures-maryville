from src import Dequeue, DoubleLinkedList


l = DoubleLinkedList()

l.prepend(0)
l.prepend(0.5)
l.prepend(0.25)
l.append(0.75)
l.append(1)

l.remove_start()
l.remove_end()

print(l.display(), l.length(), l.is_empty(), l.get_start(), l.get_end())
