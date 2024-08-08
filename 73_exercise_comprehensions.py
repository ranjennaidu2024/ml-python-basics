# Exercise check duplicates in list:
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# using comprehensions , make the above shorter and cleaner

#duplicates = []

# in order to avoid repeating the same duplicates convert to set
# then convert it to list
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)

