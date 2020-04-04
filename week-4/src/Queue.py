from src import LinkedList


class Queue:

    def __init__(self):

        self.inner_queue = LinkedList()

        return

    def enqueue(self, item):

        self.inner_queue.append(item)

        return self

    def dequeue(self):

        value = self.inner_queue.get(0).data

        self.inner_queue.remove(0)

        return value

    def isEmpty(self):

        return self.inner_queue.length() == 0

    def size(self):

        return self.inner_queue.length()

    def __len__(self):

        return self.size()
