# Zip - work like zipper , 2 list or iterables where we can zip them together
my_list = [1, 2, 3]
your_list = [10, 20, 30]
tuple = (10, 20, 30)
their_list = (5, 4, 3)

# give as many iterables as you want
print(list(zip(my_list, your_list)))

# take n item from each and add them together
[(1, 10), (2, 20), (3, 30)]

# it can zip the tuple as well as it is iterables
print(list(zip(my_list, tuple)))

# useful when want to collect username from another db and tel no from another db where all in same order, we can combine in tuple using zip
# and create whole new datastructure

# you can keep zipping things together
print(list(zip(my_list, your_list, their_list)))
