class Node:

    def __init__(self, data=None):

        self.data = data

        self.next = None

        return

    def last_node(self):
        """Return true/false if this node has a next node"""

        return self.next == None

    def value(self):
        """Get the underlying data for the node"""

        return self.data
