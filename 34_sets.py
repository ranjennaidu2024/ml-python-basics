# Set - no key value pairs , we have only values
# Set - unordered collection of unique object , no duplicate
my_set = {1,2,3,4,5,5,6,6,6}
print(my_set) # only return one and unique value , no duplicate

# set object no supporting indexing
# print(my_set[0])
# need to grab by key
print(1 in my_set)
# check set length
print(len(my_set)) # only count unique things so return 6
# can convert set into list
print(list(my_set))

# copy set
new_set = my_set.copy()
print(new_set)

my_set.add(100)
my_set.add(2)
print(my_set)

# if you want list without any duplicates , you can wrap it with set function
my_list = [1,2,3,4,5,5,6,6,6]
print(set(my_list))


# copy set
new_set = my_set.copy()
my_set.clear() # clear the original set to see the difference
print(new_set)
print(my_set)