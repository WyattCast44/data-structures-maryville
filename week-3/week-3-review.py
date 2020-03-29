# SWDV 610
# Week 3 Review
# Wyatt Castaneda

# 1. Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.


def list_bounds(sequence: list):

    sequence.sort()

    return sequence[0], sequence[-1]


def list_bounds_recursive(sequence: list):

    if len(sequence) == 0:

        # No items in sequence, just return it
        return sequence

    if len(sequence) == 1:

        # Sequence only has one item, it is both the min and the max
        return sequence[0], sequence[0]

    # Sequence has more than one item
    # We need to recusively determine the min and max
    # I chose to wrap the recursive function inside the
    # main function because there is implementation details
    # that end end use does not care about

    def find_min_max(sequence, start, end):

        end = int(end)
        start = int(start)

        # First we will test the case
        # where the end index is less than or
        # equal to the starting index
        # in this case we have one or two
        # items total
        if end <= start + 1:

            if sequence[start] < sequence[end]:
                # If the starting index value is less than
                # the end value then we have our min and max
                return sequence[start], sequence[end]
            else:
                # If the above is not true, then we have
                # one item and it is both the min and max
                return sequence[end], sequence[start]

        # Okay we know we have at least three items in the
        # sequence, we will get the middle index
        mid = (start+end)/2

        # Now we split the sequence into two sequences divided by the
        # middle index and we will find recursivly get each part down
        # to the point where each seq will only have two items and
        # we can then easily determine the min and max value
        (left_min, left_max) = find_min_max(sequence, start, mid)
        (right_min, right_max) = find_min_max(sequence, mid + 1, end)

        # We will assume that the left side of the sequence
        # had both the min and the max values
        min_value = left_min
        max_value = left_max

        # We will now check those assumptions and
        # compare values with the right side and
        # correct min/max as needed
        if right_max > max_value:
            max_value = right_max
        if right_min < min_value:
            min_value = right_min

        return min_value, max_value

    return find_min_max(sequence, 0, len(sequence) - 1)

# 2. Write a recursive function to reverse a list


def reverse_list(sequence: list):

    sequence.reverse()

    return sequence


def reverse_lists_iterative(sequence: list):

    if len(sequence) <= 1:
        return sequence

    leftIndex = 0
    rightIndex = len(sequence)-1

    sequence[leftIndex] = sequence[rightIndex]

    # Loop through all indexes until left is one index before the right
    while leftIndex < rightIndex:

        # Store the left index tmp
        temp = sequence[leftIndex]

        # Assign the left index value to the right index
        sequence[leftIndex] = sequence[rightIndex]

        # Assign the right index to the tmp left index we stored
        sequence[rightIndex] = temp

        # Update the index values
        leftIndex += 1
        rightIndex -= 1

    return sequence


def reverse_list_recursive(sequence: list):

    # If seq is one or zero, no need to reverse just return it
    if len(sequence) <= 1:
        return sequence

    # Take the last element of the list
    # and create a new list
    # Then call reverse_list again but take
    # the last item of the original list
    # So the recursive function will return the
    # last item of the shortended list  
    return [sequence[-1]] + reverse_list_recursive(sequence[:-1])
