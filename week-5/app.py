"""
SWDV 610 - Data Structures
Week 5 - Review
Wyatt Castaneda

1. Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].  Show how this list is sorted by the following algorithms:

1.A - Bubble Sort
--------------------------------------

@link https://www.geeksforgeeks.org/bubble-sort/

Bubble sort is a very straightforward
sorting strategy. It simply loops thru
every item in a list and compares that
item to the next item in the list and
if it is smaller is swaps their positions
in the list.

"""

items = [10, 9, 8, 99, 6, 11, 4, 3, 2, -1]


def bubbleSort(items):

    # Keep track of the pass num
    for pass_num in range(len(items)):

        # Loop thru all item, adjusted for pass number and + 1 for 0 index
        for index in range(len(items) - pass_num - 1):

            if items[index] > items[index + 1]:

                # The current cursor item is larger than next item, swap positions
                items[index], items[index + 1] = items[index + 1], items[index]

    return items


# print(bubbleSort(items))

""""

1.B - Selection Sort
--------------------------------------

@link https://www.geeksforgeeks.org/selection-sort/

Selection sort is another sorting
strategy. It works by looping thru the
list multiple times, each time finding
the item with minimum value and appending
it to the sorted list.

"""

items = [10, 9, 8, 99, 6, 11, 4, 3, 2, -1]


def selectionSort(items):

    # We need to keep track of the unsorted items
    unsorted = items

    # And we need to keep track of the sorted items
    sortedItems = []

    # We need to loop thru all values in the unsorted list
    for pass_num in range(len(unsorted)):

        # We need to track the min value in this pass
        pass_min = unsorted[0]

        # We will loop thru the unsorted list
        for item in unsorted:

            # If the value of the item is less than the pass min
            # we will update the pass min and keep checking
            if item < pass_min:

                pass_min = item

        # We found the pass min, we will append it to
        # the sorted list
        sortedItems.append(pass_min)

        # We will remove that min value from our unsorted list and
        # keep going to find the next min
        unsorted.remove(pass_min)

    return sortedItems


# print(selectionSort(items))


def selectionSort2(items):

    for pass_num in range(len(items)):

        pass_min_index = pass_num

        for index in range(pass_num, len(items)):

            if items[index] < items[pass_min_index]:

                pass_min_index = index

        items[pass_num], items[pass_min_index] = items[pass_min_index], items[pass_num]

    return items


""""

1.C - Insertion Sort
--------------------------------------

@link https://www.geeksforgeeks.org/insertion-sort/

Insertion sort is another sorting 
strategy. It works by looping thru the 
list and inspecting each time. If the 
next item in the list is smaller than 
the current item it will move the next item
to the start of the appropiate spot in the 
list and then continue sorting

"""

items = [10, 9, 8, 100, 6, 11, 4, 3, 2, -1]


def insertionSort(items):

    for index in range(1, len(items)):

        cursor_value = items[index]

        previous_index = index - 1

        while previous_index >= 0 and cursor_value < items[previous_index]:

            items[previous_index + 1] = items[previous_index]

            previous_index = previous_index - 1

        items[previous_index + 1] = cursor_value

    return items


# print(insertionSort(items))

"""
2. What is the difference between a list and a dictionary?  How are they coded differently and what different implementations they have?  Build a script that utilizes at least one list and one dictionary.
"""

# Lists
items = [1, 2, 3, "hello", "world"]

"""
Key details
- Auto indexed
- Auto incrimenting indexes
- Order is determined by insert order
- Stored in sequential memory addresses
- Stores references/pointers to the data in the cell
- Based on a dynamic array
- When a new list is created, python actually requests more 
  storage space than the list needs to allow for appends to the 
  list, if the number of appends exceeds python initial estimate of
  how much memory the list will need, it creates a new list automatically 
  with additional buffer and assigns the values in the original list to the
  same indexes in the new list, and then drops the original list
"""


class DynamicArray:

    def __init__(self):

        self._length = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def __len__(self):

        return self._length

    def __getitem__(self, index):

        if index < 0:
            raise KeyError

        if index > self._length:
            raise KeyError

        return self._array[index]

    def append(self, value):

        if self._length == self._capacity:

            self.resize(self._capacity * 2)

        self._array[self._length] = value

        self._length = self._length + 1

    def resize(self, capacity):

        new_array = self._make_array(capacity)

        for index in range(self._length):

            new_array[index] = self._array[index]

        self._array = new_array

        self._capacity = capacity

    def _make_array(self, capacity):

        import ctypes

        return (capacity * ctypes.py_object)()

    def __str__(self):

        value = ""

        for index in range(self._length):

            if value == "":
                value = str(self._array[index])
            else:
                value = f"{value}, {self[index]}"

        return f"[{value}]"


items = DynamicArray()

items.append(1)
items.append(2)
items.append(3)

# print(items)

# Dictionaries
items = {
    'key': 'value',
    'key2': 'another'
}

"""
@link http://openbookproject.net/thinkcs/python/english3e/dictionaries.html

Key details:
- Dictionary uses a hashed table structure
- Uses key and value pairs
- keys and values can be any data type
- underlying data structure is a hash table
- order in memory is not necessarily the order in which items were added
"""


class HashTable:

    def __init__(self):

        self.size = 10

        self.table = [[] for i in range(0, self.size)]

        return

    def hash_function(self, key):

        return (hash(key) % self.size)

    def set(self, key, value):

        # Int between 0 and the size of our hash table
        hashed_hey = self.hash_function(key)

        bucket = self.table[hashed_hey]

        # We have a bucket
        # We need to see if anythin is in bucket

        if bucket == []:

            bucket.append((key, value))

        else:

            for index, keyValuePair in enumerate(bucket):

                itemKey, itemValue = keyValuePair

                if itemKey == key:

                    bucket[index] = ((key, value))

                else:

                    bucket.append((key, value))

    def get(self, key, default=None):

        hashed_key = self.hash_function(key)

        bucket = self.table[hashed_key]

        if bucket == []:

            raise KeyError("Key does not exists")

        else:

            value = None

            for keyValuePair in bucket:

                itemKey = keyValuePair[0]
                itemValue = keyValuePair[1]

                if key == itemKey:

                    value = itemValue

            if value == None:
                raise KeyError("Key does not exist")
            else:
                return value

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


items = HashTable()

items['key'] = 'value'
items.set(10, 'int 10')
items.set(20, 'int 20')
items.set('hello', 'world')

# print(items['key'])
