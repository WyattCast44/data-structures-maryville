"""
SWDV 610 - Data Structures
Week 6 Review
Wyatt Castaneda
"""

import random


class BinaryHeap:
    """Creates a new, empty, binary heap"""

    def __init__(self):

        self.size = 0

        self.heap = [0]

        return

    def __str__(self):

        return str(self.heap[1:])  # Account for zero value

    def __len__(self):

        return self.size

    def _bubble_up(self, index):
        """Keeps heap sort order by bubbling values up to the appropriate spot"""

        while index // 2 > 0:

            # Check if the value in current node is less than
            # parent node (parent node index = index // 2)
            # If it is, swap the values in parent node and current
            # node
            if self.heap[index] < self.heap[index // 2]:

                # Capture the value of the parent node
                parent_value = self.heap[index // 2]

                # Assign the value in the current node to
                # parent node
                self.heap[index // 2] = self.heap[index]

                # Assign the old value of the parent node
                # to the current node
                self.heap[index] = parent_value

            index = index // 2

    def insert(self, value):
        """Adds a new item to the heap"""

        # Add value to the heap
        self.heap.append(value)

        # Increase the size of the heap
        self.size = self.size + 1

        # Keep heap sort order by bubbling up
        # value if needed
        self._bubble_up(self.size)

    def _min_child(self, index):
        """Returns the index of the child node with the minimum value"""

        if index * 2 + 1 > self.size:

            # Node only has left branch, that will be the min value
            return index * 2

        # Compare left and right node values
        if self.heap[index * 2] < self.heap[index * 2 + 1]:

            # Left node smaller
            return index * 2

        else:

            # Right node smaller
            return index * 2 + 1

    def _bubble_down(self, index):
        """Bubbles a value down the tree to the appropriate spot"""

        # While the node has children node
        while (index * 2) <= self.size:

            # Get the index of the child node with
            # the min value
            min_child_index = self._min_child(index)

            if self.heap[index] > self.heap[min_child_index]:

                # Capture the value of the child node
                current_node_value = self.heap[index]

                # Swap the child node and index node values
                self.heap[index] = self.heap[min_child_index]

                self.heap[min_child_index] = current_node_value

            index = min_child_index

    def del_min(self):
        """Returns the item with the minimum key value, removing the item from the heap"""

        # Because of heap sort order the first item in the
        # heap will be the miniumum value, capture the value
        result = self.heap[1]

        # We need to ensure the heap sort order is maintained
        # after we remove the root, so we will move the last item
        # in the heap to the top and bubble that value down the heap
        self.heap[1] = self.heap[self.size]

        # Now that we moved value of last item to the head of heap
        # we need to remove it from the end of heap
        self.heap.pop()

        # Now that we popped off the last item, decrease
        # heap size by 1
        self.size = self.size - 1

        # We now need to restore heap sort order by bubbling
        # top value down
        self._bubble_down(1)

        # Return the original min value
        return result

    def isEmpty(self):
        """Returns true if the heap is empty, false otherwise"""

        return len(self.heap) == 1  # Account for zero in heap

    def size(self):
        """Returns the number of items in the heap"""

        return self.size

    @staticmethod
    def fromList(items):
        """Builds a new heap from a list of values"""

        heap = BinaryHeap()

        for item in items:
            heap.insert(item)

        return heap

# Problem 1:
# ------------------------------------------------------------------------------------------
# Generate a random list of integers.
# Show the binary heap tree resulting from inserting the integers on the list one at a time.

# Problem 2.
# ------------------------------------------------------------------------------------------
# Using the list from the previous question, show the binary search tree resulting from the
# list as a parameter to the buildHeap method. Show both the tree and list form.


# items = random.sample(range(0, 100), 5)
items = [9, 5, 6, 2, 3]

print('\n----------------', 'Random items', '----------------\n')

print(items, '\n')

print('\n----------------', 'From a list', '----------------\n')

list_method = BinaryHeap.fromList(items)

print('List View:', list_method, '\n')

print('\n----------------', 'Inserting items', '----------------\n')

inserted = BinaryHeap()

for item in items:
    inserted.insert(item)

print('List View:', inserted, '\n')
