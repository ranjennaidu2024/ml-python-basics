my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
other_set = {6, 7, 8}

# intersection
# print(my_set.intersection(your_set))  # return 4,5
# shorthand for this
print(my_set & your_set)

# disjoint - check if have any two set have something in common
print(my_set.isdisjoint(other_set))  # True as both this set don't have anything in common

# union - print both set together but remove any duplicate
# print(my_set.union(your_set))
# shorthand for this
print(my_set | your_set)

# issubset() - other_set 6,7,8 is inside your_set
print(other_set.issubset(your_set))  # True

# issuperset() -
print(other_set.issuperset(your_set))  # False , as it other way around
print(your_set.issuperset(other_set))  # True

# difference of first and second set
print(my_set.difference(your_set))
# differences 4,5 was not removed
print(my_set)

# difference_update - remove all element of another set from this set
my_set.difference_update(your_set)
# differences 4,5 were removed
print(my_set)

# discard a number from the set
my_set.discard(5)
print(my_set)
