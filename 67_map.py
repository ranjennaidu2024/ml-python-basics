# map , filter , zip and reduce
# Map - simplify the code


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))


# Using Map - very useful when want to iterate over , want to change the variable
def multiply_by2(item):
    return item * 2


# map(action, data we want to take action upon)
# this give object that created in memory
print(map(multiply_by2, [1, 2, 3]))

# in order to view it need to turn it into list
# map does not require creation of list and appending of the list
# map is to have function that return item * 2
# this function going to take each of the items in our iterables , and then to return effect with the items
print(list(map(multiply_by2, [1, 2, 3])))

# if let say we create my_list outside

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))
# the map create whole new list and doesn't modify the my_list
print(my_list)
