from src import Node


class LinkedList:

    def __init__(self):

        self.head_node = Node()

    def append(self, data):

        current_node = self.head_node

        # Loop thru nodes to get the last node
        while current_node.next != None:

            current_node = current_node.next

        # We are on the last node, lets set the next node
        # to a new node
        current_node.next = Node(data)

        return self

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

    def get(self, index):

        if index > self.length():

            return None

        current_node_index = 0

        current_node = self.head_node

        while current_node != None:

            current_node = current_node.next

            if current_node_index == index:

                return current_node

            current_node_index = current_node_index + 1

    def remove(self, index):

        if index > self.length():

            return

        current_node_index = 0

        current_node = self.head_node

        while current_node.next != None:

            previous_node = current_node

            current_node = current_node.next

            if current_node_index == index:

                previous_node.next = current_node.next

                return self

            current_node_index = current_node_index + 1

        return self
