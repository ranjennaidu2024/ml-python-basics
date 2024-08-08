# Map always get same amount of item we send
# Filter - we can receive less than what we receive

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0  # evaluate to boolean expression


# take the data (my_list) and run the action (check_odd) function
# if true will be added into the list
# create a new list and doesn't modify the original list
print(list(filter(check_odd, my_list)))
