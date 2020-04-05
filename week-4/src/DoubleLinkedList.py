from src import Node


class DoubleLinkedList:

    def __init__(self):

        self.head_node = None

        return

    def prepend(self, data):
        """Add an item to the start of the queue"""

        if self.head_node == None:

            current_node = Node(data)

            self.head_node = current_node

        else:

            current_node = Node(data)

            # Make the old head node the next node to
            # the new head node
            current_node.next = self.head_node

            # Update the current head node to ensure
            # its previous node is the new head node
            self.head_node.previous = current_node

            # Now set the head node to the current node
            self.head_node = current_node

        return self

    def append(self, data):
        """Add an item to the end of the queue"""

        new_node = Node(data)

        current_node = self.head_node

        while current_node.next != None:

            current_node = current_node.next

        current_node.next = new_node

        new_node.previous = current_node

        return self

    def remove_start(self):

        if self.head_node == None:

            return

        new_head_node = self.head_node.next

        new_head_node.previous = None

        self.head_node = new_head_node

        return self

    def remove_end(self):

        if self.head_node == None:

            return

        current_node = self.head_node

        while current_node.next != None:

            current_node = current_node.next

        # So we have the last node, we need to delete
        # it, so we need to get the tail nodes previous
        # node and set the next node to none
        new_tail_node = current_node.previous

        new_tail_node.next = None

        return self

    def length(self):

        list_length = 0

        if self.head_node != None:

            list_length = list_length + 1

        else:

            return list_length

        current_node = self.head_node

        while current_node.next != None:

            list_length = list_length + 1

            current_node = current_node.next

        return list_length

    def is_empty(self):
        """Return True/False if the queue is currently empty"""

        return self.length() == 0

    def get_start(self):
        """Get the item at the start of the queue"""

        if self.head_node == None:

            return None

        return self.head_node.data

    def get_end(self):
        """Get the item at the end of the queue"""

        if self.head_node == None:

            return None

        current_node = self.head_node

        while current_node.next != None:

            current_node = current_node.next

        return current_node.data

    def display(self):
        """Display the queue nodes"""

        nodes = []

        if self.head_node == None:

            return nodes

        if self.head_node != None:

            nodes.append(self.head_node.data)

        current_node = self.head_node

        while current_node.next != None:

            current_node = current_node.next

            nodes.append(current_node.data)

        return nodes
