# Reduce - doesn't come with PYTHON Build in tools ,
# to use reduce we need to we import from functools which is tools for working with functions, come with python installation
from functools import reduce

my_list = [1, 2, 3]
test = 'te'.upp

# called by reduce from the data we giving
# when first pass my_list from reduce we get the first item in second parameter item
# the first item will be whatever the first item in the my_list ,
def accumulator(acc, item):
    return acc + item
# first acc will be 0 and item 1
# next acc will be 1 and item 2
# next acc will be 3 and item 3  = 6


# give as many iterables as you want
# reduce(function,sequence which will be data/my_list[,initial])
# the initial is what the accumulator is going to be
print(reduce(accumulator, my_list, 0))  # we accumulated all these values and return to one single digit

# function like map and filter use this reduce underneath the hood
