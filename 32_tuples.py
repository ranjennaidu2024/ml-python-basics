# Tuple - immutable list - can't change
# Use tuple when you don't want to change the list , keep the way it is , make code safer but less flexible
# faster and performance oriented than list
# can create new tuple everytime a user requests a new pickup location
# coordinates constantly chaning for latitude and longitude can use list
my_tuple = (1, 2, 3, 4, 5)
# cant change , reverse or sort like tuple
# my_tuple[1] = 'z'

# can access it
print(my_tuple[1])

# can check if value exist in tuple
print(5 in my_tuple)

# Tuple also valid key in python dictionary as it is immutable
user = {
    (1, 2): [1, 2, 3],
    'greeting': 'hello',
    'age': 20
}

print(user[(1, 2)])
