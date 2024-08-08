# another way how to look for item in dictionary

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('basket' in user)
print('size' in user)

# check for keys in dictionary
print('age' in user.keys())
# check for values in dictionary
print('hello' in user.values())

# check entire items in dictionary
print(user.items())

# Copy the dict
user2 = user.copy()
# Clear and return empty dictionary
print(user.clear())
print(user2)

# pop remove the key and value in the dictionary
print(user2.pop('age')) # return the removed value 20
print(user2)

# remove last item in the dictionary but since it is unordered can remove any key
print(user2.popitem())

# update key value
user3 = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

# update the age value
user3.update({'age': 55})
print(user3)
# if the key not exist it will still update by create it with new key item
user3.update({'ages': 55})
print(user3)