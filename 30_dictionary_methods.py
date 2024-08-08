user = {
    'greet': [1, 2, 3],
    'basket': 'hello',
}

# to access a key , see if it exist in first place , using get to avoid error if not found
# print(user['age']) # this give error
print(user.get('age'))  # this return None if key not found

# if let say want to return default value instead of none can add extra param
print(user.get('age', 55))  # this return default value we specified if key not found

# create new dict
# not very common but just to say there are built-in function to create dict
user2 = dict(name='JohnJohn')
print(user2)
