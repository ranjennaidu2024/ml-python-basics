# arguments and keyword arguments

# *args - accept any number of positional arguments
# *args - this can be named as any but standard is to use the *args
def super_func(*args):
    # this will give a tuple (1, 2, 3, 4, 5)
    print(args)
    return sum(args)


super_func(1, 2, 3, 4, 5)


# **kwargs - can add keywords
def super_func(*args, **kwargs):
    # this will give a dictionary {'num1': 5, 'num2': 10}
    print(kwargs)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))


# now super_func can take how many args or keyword args as it wants
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))


# Should follow this position
# Rule : param , * args , default parameters , *kwargs
def super_func(name, *args, i='hi', **kwargs):
    print(f'{i} {name}')
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('Ranjen', 1, 2, 3, 4, 5, num1=5, num2=10))
