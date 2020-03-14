
# My example for a control flow
# is a simple way to print the numbers
# 0 to 999, on possible gotcha on this
# code for someone unfamiliar with python
# they expect that all numbers 0 to 1000
# get printed, but because the range function
# is exclusive 1000 will not be included

for number in range(1000):
    print(number)

# In this example, it is a little more explicit
# that the numbers will start at 0, in this
# case it doesn't really provide that much value
# but it is a simple example of how explicitness
# can make code easier to understand for future
# maintainers

for number in range(0, 1000):
    print(number)

# In this last example, this is an extreme example 
# of explicitness, but is some cases this level of 
# detail is the best solution, espicially when the 
# numbers/etc are a seemingly random value.

start = 2
end = 1000

for number in range(start, end):
    print(number)
