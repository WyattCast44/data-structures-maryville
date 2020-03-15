"""
SWDV 610 - Data Structures
Week 1 - Reinforcement and Punishment
Wyatt Castaneda
"""

"""
Problem 1.
Write a short Python function, is_multiple(n, m), that takes two integer values and returns True is n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
"""


def is_multiple(baseNumber, numberToCheck):
    # If the modulus is not equal
    # to zero, then the number is
    # not an multiple of the base number
    return (int(numberToCheck) % int(baseNumber)) == 0


"""
Problem 2.
A common punishment for school children is to write out a sentence multiple times.  Write a Python stand-alone program that will write the following sentence one hundred times: "I will never spam my friends again."
"""


def print_x_times(numberOfTimes, *values, options={}):

    import sys

    defaults = {
        'sep': ' ',
        'end': '\n',
        'file': sys.stdout,
        'flush': False,
        'before': None,
        'after': None,
    }

    defaults.update(options)

    if defaults['before']:
        print(defaults['before'])

    for index in range(numberOfTimes):

        print(*values, sep=defaults['sep'],
              end=defaults['end'], file=defaults['file'], flush=defaults['flush'])

    if defaults['after']:
        print(defaults['after'])


print_x_times(100, "I will never spam my friends again.")
