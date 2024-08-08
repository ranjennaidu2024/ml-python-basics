# Dictionary - other language might call it object or hashtable or map
# Data type in python but also data structure
# Dictionary - Unordered key-value pair
# key-value , key is string for us to grab the value
dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

# grad the value of key b
print(dictionary['b'])
print(dictionary['a'])
# if we want second item in the list
print(dictionary['a'][1])

my_list = dictionary = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'world',
        'x': False
    },
]

print(my_list[0]['a'][2])  # print 3
print(my_list[1]['a'][2])  # print 6

# Use list - ordered , single value , index-values
# Use dictionary - not sorted , more information , key-values
