# SWDV 610
# Week 3 Review
# Wyatt Castaneda

# 1. Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.


def list_bounds(sequence: list):

    sequence.sort()

    return sequence[0], sequence[-1]

# 2. Write a recursive function to reverse a list.


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
    return [sequence[-1]] + reverse_listss(sequence[:-1])
