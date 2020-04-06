from src import LinkedList


class Stack:

    def __init__(self):

        self.inner_stack = LinkedList()

    def push(self, data):

        self.inner_stack.append(data)

        return self

    def pop(self):

        index = self.inner_stack.length() - 1

        value = self.inner_stack.get(index).data

        self.inner_stack.remove(index)

        return value

    def peek(self):

        index = self.inner_stack.length() - 1

        return self.inner_stack.get(index).data

    def isEmpty(self):

        return self.inner_stack.length() == 0

    def size(self):

        return self.inner_stack.length()
