# Tuple also valid key in python as it is immutable
dictionary = {
    'a': [1,2,3],
    'greeting': 'hello',
    'is_Magic': True,
    123: [1,2,3],
    123: 'meow',
    True: 'hello'
    # [100]: True # key won't work for list as it is mutable
}

# key works if you use integer or keyword True too
# dictionary key need to be immutable , list can be changed and mutable, so we can't assign list as key in the dict
print(dictionary[123])
print(dictionary[True])

# key in dict have to be unique , for eg:123 it overwrites the first and give the last one
print(dictionary[123])