# Iterable - Object/Collections that can be iterated over
# can be list , dictionary , tuple , set , string
# Iterate -> can go one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# print the keys
for item in user:
    print(item)
for item in user.keys():
    print(item)

# print the values
for item in user.values():
    print(item)

# print the key-values which is items
for item in user.items():
    print(item)

# we can do tuple unpacking
for item in user.items():
    key, value = item;
    print(key, value)
# shorthand to do this
# can use any variable for k,v it will still take the key and value for dict
for k, v in user.items():
    print(k, v)

# give error as int object is not iterable
# for item in 50:
#     print(item)
