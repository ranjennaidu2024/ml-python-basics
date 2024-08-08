# Tuple similar to list
my_tuple = (1,2,3,4,5,6,5,5)
new_tuple = my_tuple[1:2]

print(new_tuple) # if single item , it still have coma at end but still a tuple (2,)

x,y,z, *other = (1,2,3,4,5)
print(x)
print(z)
print(other)

# Tuples only have two methods , count and index
# count to find how many occurance of 5 in the tuple
print(my_tuple.count(5))


# give length of the tuple - 8
print(len(my_tuple))
print(my_tuple)
# return the index position of the value from the tuple , value 2 return index 1
print(my_tuple.index(2))