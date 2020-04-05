from src import DoubleLinkedList


class Dequeue:

    def __init__(self):

        self.inner_queue = DoubleLinkedList()

        return

    def insertFront(self, data):

        self.inner_queue.prepend(data)

        return self

    def insertRear(self, data):

        self.inner_queue.append(data)

        return self

    def removeFront(self):

        self.inner_queue.remove_start()

        return self

    def removeRear(self):

        self.inner_queue.remove_end()

        return

    def getFront(self):

        return self.inner_queue.get_start()

    def getRear(self):

        return self.inner_queue.get_end()

    def isEmpty(self):

        return self.inner_queue.length == 0

    def size(self):

        return self.inner_queue.length()

    def purge(self):

        return
