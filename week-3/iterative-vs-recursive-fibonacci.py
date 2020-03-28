import timeit


def iterative_fibonacci(number=10000):

    if number <= 1:
        return number

    seq = [0, 1]

    for index in range(2, number + 1):
        seq.append(seq[index-1] + seq[index-2])

    return seq[number]


def recursive_fibonacci(number=10000):

    if number <= 1:
        return number

    return (recursive_fibonacci(number-1) + recursive_fibonacci(number-2))


print(timeit.timeit('iterative_fibonacci', number=1000, globals=globals()))

print(timeit.timeit('recursive_fibonacci', number=1000, globals=globals()))
