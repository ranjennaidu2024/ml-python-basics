# Pure Functions - [1,2,3] -> [2,4,6]
# same input always return same output
# function should not provide side effect
# PURE FUNCTION is more like a guideline than absolute , impossible to have pure function everywhere

# this one we don't care about outside world and it is pure function as mostly is done within the function scope
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))

# for example below the new_list and print inside the function will have side affect with other functions outside
new_list = []


def multiply_by2(li):
    for item in li:
        new_list.append(item * 2)
    return print(new_list)


multiply_by2([1, 2, 3])
