from src import Node


class DoubleLinkedList:

    def __init__(self):

        # head node
        self.head_node = Node()

        # tail node
        self.head_node.next = Node()

        return

    def append(self, data):
        """Add an item to the end of the list"""

        new_tail_node = Node(data)

        current_node = 

        new_tail_node.previous = self.head_node.next

        self.tail_node = new_tail_node

        return self

    def prepend(self, data):
        """Add an item to the start of the list"""

        new_head_node = Node(data)

        new_head_node.next = self.head_node.next

        self.head_node = new_head_node

    def length(self):

        list_length = 0

        current_node = self.head_node

        while current_node.next != None:

            list_length = list_length + 1

            current_node = current_node.next

        return list_length

    def display(self):

        nodes = []

        current_node = self.head_node

        while current_node.next != None:

            current_node = current_node.next

            nodes.append(current_node.data)

        return nodes
